def main():
    message = input("Message: ")
    converted_message = convert(message)

    print(converted_message)


def convert(text):
    text = text.replace(":)", "🙂").replace(":(","🙁")
    return text


main()
