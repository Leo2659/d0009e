words = []
descriptions = []

def main_dic():
  printMenu()
  choice = int(input("Choose alternative:"))
  if(choice == 1):
    insert()
  if(choice == 2):
    lookup()
  if(choice == 3):
    quit()

def printMenu():
  print()
  print("Menu for dictionary")
  print()
  print("1: Insert")
  print("2: Lookup")
  print("3: Exit")

def insert():
  print("insert")
  return main_dic()

def lookup():
  print("lookup")
  return main_dic()

def quit():
  return 0


