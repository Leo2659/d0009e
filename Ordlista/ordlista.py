#---------GENERELLA FUNKTIONER---------#

def printMenu():  # Skriver ut menyn
    print()
    print("Menu for dictionary")
    print()
    print("1: Insert")
    print("2: Lookup")
    print("3: Delete")
    print("4: Exit program")


def quit():
    return 0  # Returnera inget, avsluta programmet

#---------ORDLISA MED LISTOR---------#


words = []  # Lista som innehåller alla ord
descriptions = []  # Lista som innehåller alla förklaringar


def main_list():  # Main funktionen för list versionen av programmet
    printMenu()  # Kallar på menyn
    # Låter användaren välja 1 av 4 val
    choice = int(input("Choose alternative:"))
    if choice == 1:
        insert_list()
    if choice == 2:
        lookup_list()
    if choice == 3:
        delete_list()
    if choice == 4:
        quit()


def insert_list():  # Anropas om användaren väljer att lägga till ett ord
    wordInput = input("Word to insert:")
    if isInList(wordInput):
        print("That word already exists in your dictionary")
    else:
        words.append(wordInput)
        descInput = input("Description of word:")
        descriptions.append(descInput)
    return main_list()  # Gå tillbaka huvudfunktionen


def lookup_list():  # Anropas om användaren väljer att söka efter ett ord
    searchInput = input("Word to lookup:")
    if not isInList(searchInput):
        print("Word does not exist in your dictionary")
    else:
        index = wordIndex(searchInput)
        print("Description for", searchInput, ":", descriptions[index])

    return main_list()  # Gå tillbaka huvudfunktionen


def isInList(word):  # Finns ordet i listan?
    for value in words:
        if(word == value):
            return True
    return False


def wordIndex(word):  # Returnerar ordets index
    for index, value in enumerate(words):
        if(word == value):
            return index


def wordDelete(word):  # Tar bort ordet från listan
    for index, value in enumerate(words):
        if(word == value):
            words.pop(index)
            descriptions.pop(index)


def delete_list():  # Anropas om användaren väljer att bort ett ord
    wordToDelete = input("Type the word you would like to delete:")
    if not isInList(wordToDelete):
        print("That word is not in your dictionary")
    else:
        wordDelete(wordToDelete)
        print(wordToDelete, "was sucessfully deleted")
    return main_list()


#---------ORDLISTA MED DICTIONARY---------#

dictronary = {}  # Dictionary med våra ord och förklaringar


def main_dic():
    printMenu()
    choice = int(input("Choose alternative:"))
    if choice == 1:
        insert_dic()
    if choice == 2:
        lookup_dic()
    if choice == 3:
        delete_dic()
    if choice == 4:
        quit()


def insert_dic():
    wordInput = input("Word to insert:")
    if isInDic(wordInput):
        print("That word already exists in your dictionary")
    else:
        descInput = input("Description of word:")
        dictronary.update({wordInput: descInput})
    return main_dic()


def lookup_dic():
    searchInput = input("Word to lookup:")
    if not isInDic(searchInput):
        print("Word does not exist in your dictionary")
    else:
        for key, value in dictronary.items():
            if searchInput == key:
                print("Description for",searchInput,":",value)
    return main_dic()


def delete_dic():
    wordToDelete = input("Type the word you would like to delete:")
    if not isInDic(wordToDelete):
        print("That word is not in your dictionary")
    else:
        dictronary.pop(wordToDelete)
        print(wordToDelete, "was sucessfully deleted")
    return main_dic()


def isInDic(word):
    for key in dictronary.keys():
        if key == word:
            return True
    return False
