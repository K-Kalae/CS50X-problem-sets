types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

n = input("File name: ").strip().lower().split(".")[-1]
print(types.get(n, "application/octet-stream"))
