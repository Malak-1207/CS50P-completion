filename = input("File name: ").strip().lower()


if '.' in filename:
    extension = filename.rsplit('.', 1)[1]
else:
    extension = ""

if extension == "gif":
    print("image/gif")
elif extension in ["jpg", "jpeg"]:
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
