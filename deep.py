answer= input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
match answer:
    case "42" | "сорок два":
       print("Да")
    case _:
        print("Нет")
