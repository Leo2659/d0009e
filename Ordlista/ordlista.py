#---------GENERELLA FUNKTIONER---------#

def printMenu():  # Skriver ut menyn
    print()
    print("Menu for dictionary")
    print()
    print("1: Insert")
    print("2: Lookup")
    print("3: Delete")
    print("4: Exit program")

#---------ORDLISA MED LISTOR---------#


words = []  # Lista som innehåller alla ord
descriptions = []  # Lista som innehåller alla förklaringar


def main_list():  # Main funktionen för list versionen av programmet
    printMenu()  # Kallar på menyn
    # Låter användaren välja 1 av 4 val där 4 avslutar programmet
    option = int(input("Choose alternative:"))
    while option != 4:
        if option == 1:
            insert_list()
        elif option == 2:
            lookup_list()
        elif option == 3:
            delete_list()
        else:
            print("Invalid operation.")

        printMenu()
        option = int(input("Choose alternative:"))


def insert_list():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
    word = input("Word to insert:")
    if word in words:  # Kollar om ordet redan finns i listan
        print("That word already exists in your dictionary.")
    else:
        # Lägger till ordet och förklaringen om ordet inte finns i listan
        words.append(word)
        desc = input("Description of word:")  # Tar in förklaringen
        descriptions.append(desc)


def lookup_list():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
    search = input("Word to lookup:")
    if search not in words:  # Kollar om ordet inte finns i listan
        print("Word does not exist in your dictionary.")
    else:
        # Hämtar ordets index för att visa den matchande förklaringen för användaren
        index = words.index(search)
        print("Description for", search, ":", descriptions[index])


def delete_list():  # Anropas om användaren väljer att bort ett ord (Val 3)
    word = input("Type the word you would like to delete:")
    if word not in words:  # Kollar om ordet inte finns i listan
        print("That word is not in your dictionary.")
    else:
        # Hämtar ordets index för att ta bort ordet och förklaringen från listorna
        index = words.index(word)
        words.pop(index)
        descriptions.pop(index)
        print(word, "was sucessfully deleted.")


#---------ORDLISTA MED DICTIONARY---------#
dictionary = {}  # Dictionary med våra ord och förklaringar


def main_dic():  # Huvudfuktionen för dictionary version av programmet
    printMenu()
    option = int(input("Choose alternative:"))
    while option != 4:
        if option == 1:
            insert_dic()
        elif option == 2:
            lookup_dic()
        elif option == 3:
            delete_dic()
        else:
            print("Invalid operation.")

        printMenu()
        option = int(input("Choose alternative:"))


def insert_dic():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
    word = input("Word to insert:")
    if word in dictionary.keys():  # Kollar om ordet matchar en av nycklarna i dictionary
        print("That word already exists in your dictionary.")
    else:  # Lägget till ordet och förklaringen i dictionary
        desc = input("Description of word:")
        dictionary.update({word: desc})


def lookup_dic():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
    search = input("Word to lookup:")
    if search not in dictionary.keys():
        print("Word does not exist in your dictionary.")
    else: 
        print("Description for", search, ":", dictionary[search])


def delete_dic():  # Anropas om användaren väljer att bort ett ord (Val 3)
    word = input("Type the word you would like to delete:")
    if word not in dictionary.keys():  # Kollar om ordet inte finns i dictionary
        print("Word does not exist in your dictionary.")
    else:  # Tar bort ordet och förklaringen från dictionary
        dictionary.pop(word)
        print(word, "was sucessfully deleted.")

#---------ORDLISTA MED TUPLER---------#


tupleList = []


def main_tuple():  # Huvudfuktionen för tuple versionen av programmet
    printMenu()
    option = int(input("Choose alternative:"))
    while option != 4:
        if option == 1:
            insert_tuple()
        elif option == 2:
            lookup_tuple()
        elif option == 3:
            delete_tuple()
        else:
            print("Invalid operation.")

        printMenu()
        option = int(input("Choose alternative:"))


def insert_tuple():  # Anropas om användaren väljer att lägga till ett ord (Val 1)
    word = input("Word to insert:")
    if isInList(word):  # Kollar om ordet redan finns i listan med funktionen isInList()
        print("That word already exists in your dictionary.")
    else:  # Lägger till ordet och förklaringen om ordet inte finns i listan
        desc = input("Description of word:")
        tupleList.append((word, desc,))


def lookup_tuple():  # Anropas om användaren väljer att söka efter ett ord (Val 2)
    search = input("Word to lookup:")
    if not isInList(search):  # Kollar om ordet inte finns i listan med funktionen isInList()
        print("Word does not exist in your dictionary.")
    else:  # Söker igenom listan och om x[0] alltså något av orden matchar det sökta ordet skrivs ordet x[0] och den matchande förklaringen x[1] ut
        for x in tupleList:
            if x[0] == search:
                print("Description for", x[0], ":", x[1])


def delete_tuple():  # Anropas om användaren väljer att bort ett ord (Val 3)
    word = input("Word to delete: ")
    if not isInList(word):  # Kollar om ordet inte finns i listan med funktionen isInList()
        print("Word does not exist in your dictionary.")
    else:  # Söker igenom listan och tar bort hela tuplen med ordet och förklaringen i
        for x in tupleList:
            if x[0] == word:
                tupleList.pop(tupleList.index((x[0], x[1])))
                print(x[0], "was successfully deleted.")


def isInList(word):  # Funktion för att söka igenom listan. Returnerar True om ordet finns och False om det inte gör det
    for x in tupleList:
        if x[0] == word:
            return True
    return False
