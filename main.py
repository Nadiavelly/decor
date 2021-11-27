from decor import decor

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

from pprint import pprint

@decor('data.txt')
def name():
    a = 0
    number = input('Введите номер документа')
    for document in documents:
        if number == document["number"]:
            a = document["name"]
            print(a)
    if a == False:
        print("Документ не существует")
    return a


def shelf():
    a = 0
    number = input('Введите номер документа')
    for directory, numbers in directories.items():
        for doc in numbers:
            if number == doc:
                a = directory
                print(a)
    if a == False:
        print("Документ не существует")

def list():
    list_documents = []
    for document in documents:
        str_doc = (f'{document["type"]} {document["number"]} {document["name"]}')
        list_documents.append(str_doc)

    pprint(list_documents)


def add_doc():
    kind = input("Введите тип документа")
    number = input("Введите номер документа")
    name = input("Введите имя владельца")
    shelf = input("Введите номер полки")
    new_doc = {'type': kind, 'number': number, 'name': name}
    documents.append(new_doc)
    a = False
    for directory, numbers in directories.items():
        if shelf == directory:
            numbers.append(number)
            a = True
    if a == False:
        print("Такой полки не существует")


def main():
    while True:
        user_input = input('Введите команду')
        if user_input == 'p':
            name()
        if user_input == 's':
            shelf()
        if user_input == 'l':
            list()
        if user_input == 'a':
            add_doc()
        if user_input == 'q':
            break

name()



