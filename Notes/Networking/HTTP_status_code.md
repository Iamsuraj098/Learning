## HTTP Status Code - 
HTTP Status codes are three digit responses returned by a web server to indicate the result of a client HTTP requests.
They help the client (browser, API consumer, or application) understand whether the request succeeded, failed, or needs further action.

Status codes are grouped into five categories based on the first digit.

| Category | Meaning       |
| -------- | ------------- |
| 1xx      | Informational |
| 2xx      | Success       |
| 3xx      | Redirection   |
| 4xx      | Client Error  |
| 5xx      | Server Error  |

---

### 1. 1xx - Information Response
These codes indicate that the request has been recevied and the server is continuing the process. They are rearly visible to end users.
Common Codes
- 100 - Continue
	- The client can continue sending the request body.
	- Used in large uploads where the client checks if the server is ready.
- 101 - Switching Protocol
	- Server agrees to switch protocol
	- Example: HTTP -> WebSocket upgrade
- 102 - Processing
	- Server has received the request but processing is still ongoing.
- 103 - Early Hint
	- Allows the server to send headers early so the browser can preload resources.

### 2. 2xx - Success
These indicate that the request was successfully received, understood, and processed.
**Important Codes**
- 200 - ok
	- Standard successful response.
	- Most common response in APIs and websites.
- 201 - Created
	- A new resource was successfully created.
- 202 - Accepted
	- Request accepted but not completed yet.
	- Used in asynchronous processing.
	- Example: Background job queue.
- 204 - No Content
	- Request successful but no response body returned.
- 206 - Partial Content
	- Used when downloading part of a resource (range requests).
	- Example - Video streaming, Download resume support

### 3. 3xx - Redirection
These indicate that the client must take additional action (usually follow another URL).
**Important Codes**
- 301 – Moved Permanently
	- Resource permanently moved to a new URL.
	- Example - Search engine updated the link.
- 302 - Found(Temporary redirect)
	- Temporary redirection.
	- Example: Login -> redirect to dashboard
- 303 - See Other
	- Client should use gfet request for the redirected resources.
- 304 - Not Modified
	- Used for browser caching
	- Example: Browser loads from cache instead of downloading again.
- 307 - Temporary redirect
	- Similar to 302 but method must not change.
- 308 - Parmanent Direct
	- Same as 301 but HTTP method preserved.

### 4. 4xx - Client Error
These means client make a bad request
**Important Codes**
- 401 - Bad Request
	- Request is malformed
	- Example: Invalid JSON, Missing parameters.
- 401 - Unauthorized
	- Authentication required.
	- Example: Missing api token
- 403 - Forbidden
	- Server understand request but refuses permission.
	- Example: Accessing admin page without role.
- 404 - Not Found
	- Requested resource does not exist.
	- Example: request: GET /user/9999 but this user not present
- 405 - Method not allowed
	- HTTP method not allowed.
	- Example: user request get method but actually post method required.
- 406 - Not Acceptable
	- Server cannot produce a response matching the Accept header.
- 408 – Request Timeout
	- Client took too long to send request.
- 409 – Conflict
	- Request conflicts with current resource state.
	- Example: Duplicate username.
- 410 – Gone
	- Resource permanently removed.
- 413 – Payload Too Large
	- Request body too large.
	- Example: Upload limit exceeded.
- 415 – Unsupported Media Type
	- Example: Content-Type: XML, API only accepts JSON
- 429 – Too Many Requests
	- Rate limit exceeded.
	- Example: API Rate Limit = 100 requests/min

### 5. 5xx - Server Errors
These indicate the server failed while processing a valid request.
**Important Codes**
- 500 - Internal Server Error 
	- Generic server failure.
	- Example: Unhandled exception, Server crash
- 501 - Not Implemented
	- Server does not support the request method.
- 502 – Bad Gateway
	- Occurs in microservices / proxies.
	- Example:
		```
		Client → Gateway → Service
		Service crashed → 502
		```
- 503 – Service Unavailable
	- Server temporarily overloaded or under maintenance.
	- Example: High traffic, Often used with Retry-After headers
- 504 – Gateway Timeout
	- Upstream server did not respond in time.
	- Example: Load balancer waiting for backend
	
#### Best Practices (Production APIs)
Use correct status codes
Example
```
GET → 200
POST → 201
DELETE → 204
Bad input → 400
Unauthorized → 401
```
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




























