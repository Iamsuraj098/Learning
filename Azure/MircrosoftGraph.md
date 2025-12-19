## Microsoft Graph


def extract_text_from_file(download_url, file_name):
    response = requests.get(download_url, stream=True)

    if response.status_code != 200:
        return ""

    ext = file_name.lower().split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        for chunk in response.iter_content(8192):
            tmp.write(chunk)
        temp_path = tmp.name

    text_content = ""

    try:
        if ext == "docx":
            doc = Document(temp_path)
            text_content = "\n".join([p.text for p in doc.paragraphs])

        elif ext == "pdf":
            reader = PdfReader(temp_path)
            pages = []
            for page in reader.pages:
                pages.append(page.extract_text() or "")
            text_content = "\n".join(pages)

        else:
            text_content = "Unsupported file type"

    except Exception as e:
        text_content = f"Error extracting text: {e}"

    finally:
        os.remove(temp_path)

    return text_content


def extract_required_fields(text: str):
    """
    Extracts specific fields from the job description.
    """

    position_pattern = r"Position\s*:\s*(.*)"
    experience_pattern = r"Experience Required\s*:\s*(.*)"
    location_pattern = r"Location\s*:\s*(.*)"

    position = None
    experience = None
    location = None

    pos = re.search(position_pattern, text, re.IGNORECASE)
    if pos:
        position = pos.group(1).strip()

    exp = re.search(experience_pattern, text, re.IGNORECASE)
    if exp:
        experience = exp.group(1).strip()

    loc = re.search(location_pattern, text, re.IGNORECASE)
    if loc:
        location = loc.group(1).strip()

    return {
        "position": position,
        "experience": experience,
        "location": location
    }


# @app.get("/extract-files-content")
# def extract_files_content():
#     token = get_access_token()
#     headers = {"Authorization": f"Bearer {token}"}

#     folder_url = (
#         "https://graph.microsoft.com/v1.0/me"
#         "/drive/root:/Altysys Client JDs:/children"
#         "?$select=id,name,lastModifiedDateTime,lastModifiedBy"
#     )

#     folder_res = requests.get(folder_url, headers=headers)
#     if folder_res.status_code != 200:
#         raise HTTPException(status_code=500, detail=folder_res.text)

#     folder_items = folder_res.json().get("value", [])
#     if not folder_items:
#         return {"message": "No folders found"}

#     # Pick first folder
#     first_folder = folder_items[0]
#     folder_name = first_folder["name"]

#     result = {
#         "folderName": folder_name,
#         "lastModifiedDateTime": first_folder.get("lastModifiedDateTime"),
#         "lastModifiedBy": first_folder.get("lastModifiedBy", {}).get("user", {}),
#         "files": []
#     }

#     # List items in the folder including "file" property
#     subfolder_url = (
#         f"https://graph.microsoft.com/v1.0/me"
#         f"/drive/root:/Altysys Client JDs/{folder_name}:/children"
#         f"?$select=id,name,lastModifiedDateTime,lastModifiedBy,file"
#     )

#     sub_res = requests.get(subfolder_url, headers=headers)
#     if sub_res.status_code != 200:
#         raise HTTPException(status_code=500, detail=sub_res.text)

#     items = sub_res.json().get("value", [])
#     files = [item for item in items if "file" in item]

#     if not files:
#         return result

#     # Loop through ALL files
#     for file_item in files:
#         file_id = file_item["id"]

#         meta_url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}"
#         meta_res = requests.get(meta_url, headers=headers).json()

#         download_url = meta_res.get("@microsoft.graph.downloadUrl")
#         if not download_url:
#             continue

#         file_name = meta_res["name"]

#         # Extract full text content
#         extracted_text = extract_text_from_file(download_url, file_name)

#         # Extract position, experience, location
#         extracted_fields = extract_required_fields(extracted_text)

#         result["files"].append({
#             "name": file_name,
#             "lastModifiedDateTime": file_item.get("lastModifiedDateTime"),
#             "lastModifiedBy": file_item.get("lastModifiedBy", {}).get("user", {}),
#             "fields": extracted_fields
#         })

#     return result


@app.get("/extract-files-content")
def extract_files_content():
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    folder_url = (
        "https://graph.microsoft.com/v1.0/me"
        "/drive/root:/Altysys Client JDs:/children"
        "?$select=id,name,lastModifiedDateTime,lastModifiedBy"
    )

    folder_res = requests.get(folder_url, headers=headers)
    if folder_res.status_code != 200:
        raise HTTPException(status_code=500, detail=folder_res.text)

    folder_items = folder_res.json().get("value", [])
    if not folder_items:
        return {"message": "No folders found"}

    all_folders_result = []

    # Loop through every folder under "Altysys Client JDs"
    for folder in folder_items:
        folder_name = folder["name"]

        folder_block = {
            "folderName": folder_name,
            "lastModifiedDateTime": folder.get("lastModifiedDateTime"),
            "lastModifiedBy": folder.get("lastModifiedBy", {}).get("user", {}),
            "files": []
        }

        # List items inside this folder
        subfolder_url = (
            f"https://graph.microsoft.com/v1.0/me"
            f"/drive/root:/Altysys Client JDs/{folder_name}:/children"
            f"?$select=id,name,lastModifiedDateTime,lastModifiedBy,file"
        )

        sub_res = requests.get(subfolder_url, headers=headers)
        if sub_res.status_code != 200:
            raise HTTPException(status_code=500, detail=sub_res.text)

        items = sub_res.json().get("value", [])
        files = [item for item in items if "file" in item]

        # Extract text for every file in the folder
        for file_item in files:
            file_id = file_item["id"]

            meta_url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}"
            meta_res = requests.get(meta_url, headers=headers).json()

            download_url = meta_res.get("@microsoft.graph.downloadUrl")
            if not download_url:
                continue

            file_name = meta_res["name"]

            extracted_text = extract_text_from_file(download_url, file_name)
            extracted_fields = extract_required_fields(extracted_text)

            folder_block["files"].append({
                "name": file_name,
                "lastModifiedDateTime": file_item.get("lastModifiedDateTime"),
                "lastModifiedBy": file_item.get("lastModifiedBy", {}).get("user", {}),
                "fields": extracted_fields
            })

        all_folders_result.append(folder_block)

    return all_folders_result
