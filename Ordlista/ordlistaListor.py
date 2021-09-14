words = []  # Lista som innehåller alla ord
descriptions = []  # Lista som innehåller alla förklaringar


def main_dic():
    printMenu()  # Kallar på menyn
    # Låter användaren välja 1 av 4 val
    choice = int(input("Choose alternative:"))
    if choice == 1:
        insert()
    if choice == 2:
        lookup()
    if choice == 3:
        quit()
    if choice == 4:
        delete()


def printMenu():  # Skriver ut menyn
    print()
    print("Menu for dictionary")
    print()
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")
    print("4: Delete")


def insert():  # Anropas om användaren väljer att lägga till ett ord
    wordInput = input("Word to insert:")
    if isInList(wordInput):
        print("That word already exists in your dictionary")
    else:
        words.append(wordInput)
        descInput = input("Description of word:")
        descriptions.append(descInput)
    return main_dic()  # Gå tillbaka huvudfunktionen


def lookup():  # Anropas om användaren väljer att söka efter ett ord
    searchInput = input("Word to lookup:")
    if not isInList(searchInput):
        print("Word does not exist in your dictionary")
    else:
        index = wordIndex(searchInput)
        print("Description for",searchInput,":",descriptions[index])

    return main_dic()  # Gå tillbaka huvudfunktionen


def quit():
    return 0  # Returnera inget, avsluta programmet


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


def delete():  # Anropas om användaren väljer att bort ett ord
    wordToDelete = input("Type the word you would like to delete:")
    if not isInList(wordToDelete):
        print("That word is not in your dictionary")
    else:
        wordDelete(wordToDelete)
        print("Word was sucessfully deleted")
    return main_dic()
