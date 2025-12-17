def sort(arr, start, end):
    
    return None

def merge(arr, start, end):
    mid = (end-start)//2
    merge(arr[start, mid], start, mid)
    merge(arr[mid+1, end], mid+1, end)
    sort(arr, start, end)
    return None

def start():
    arr = [1, 2, 3, 4, 0]
    n = len(arr)
    print(arr, n)

start()
