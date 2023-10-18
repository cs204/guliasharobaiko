s = (input("File name: "))

match s:
    case "hello.jpg":
        print("image/jpeg")
    case "document.pdf":
        print("application/pdf")