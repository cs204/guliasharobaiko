s = input("Приветствие: ")

match s:
    case "здравствуйте":
        print("$0")
    case "здравствуйте, человек":
        print("$0")
    case "здрасте":
        print("$20")
    case "привет":
        print("$100")