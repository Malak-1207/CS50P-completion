def convert(text):
    text = text.replace(":)", "🙂")
    
    text = text.replace(":(", "🙁")
    return text

message = input("Input: ")

print(convert(message))
