with open("text.txt") as file:
    contents = file.read()
    print(contents)
# not to write file = open("text.txt") & file.close()

with open("text_new.txt", mode="w") as file:
    file.write("Ballerina Cappuccina è la moglie di Cappuccino Assasino")