with open('quotes.txt' , 'r' , encoding= "UTF-8") as file:
    for line in file:
        print(line)

author = input("Хто це пише?")
with open('quotes.txt' , 'a' , encoding="UTF-8") as file:
    file.write(f'({author})\n')

while True:
    answer = input("Бажаєте ввести ще одну цитату (так\ні)")
    answer = answer.lower()

    if answer == "так":
        quotes = input("Введіть цитату")
        file = open('quotes.txt' , "a" , encoding="UTF-8")
        file.write(f"{quotes}\n")
        file.close()
    else:
        break

with open('quotes.txt' , 'r' , encoding= "UTF-8") as file:
    for line in file:
        print(line)