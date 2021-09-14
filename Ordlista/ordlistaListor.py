words = [] #Lista som innehåller alla ord
descriptions = [] #Lista som innehåller alla förklaringar

def main_dic():  
  printMenu()#Kallar på menyn
  choice = int(input("Choose alternative:")) #Låter användaren välja 1 av 3 val 
  if(choice == 1):
    insert()
  if(choice == 2):
    lookup()
  if(choice == 3):
    quit()

def printMenu(): #Skriver ut menyn
  print()
  print("Menu for dictionary")
  print()
  print("1: Insert")
  print("2: Lookup")
  print("3: Exit")

def insert():
  print("insert")
  return main_dic() #Gå tillbaka huvudfunktionen

def lookup():
  print("lookup")
  return main_dic() #Gå tillbaka huvudfunktionen

def quit():
  return 0 #Returnera inget, avsluta programmet


