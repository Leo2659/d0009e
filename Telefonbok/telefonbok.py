# Fixa felhantering
from typing import get_args


class Phonebook:
    def __init__(self):
        self.contacts = {}

    def isInNames(self, key):
        if key in self.contacts.keys():
            return True
        return False

    def isInNumbers(self, value):
        if value in self.contacts.values():
            return True
        return False

    def update(self, name, number):
        self.contacts.update({name: number})

    def changeName(self, name, number):
        self.contacts[name] = number

    def add(self, name, number):
        if self.isInNames(name):
            print(name, "already exists")
        elif self.isInNumbers(number):
            print(number, "already exists")
        else:
            self.update(name, number)

    def lookup(self, name):
        if not self.isInNames(name):
            print(name, "not found")
        else:
            print(self.contacts.get(name))

    def change(self, name, number):
        if not self.isInNames(name):
            print(name, "not found")
        elif self.isInNumbers(number):
            print(number, "already exists")
        else:
            self.changeName(name, number)

    def alias(self, name, name2):
        if not self.isInNames(name) or self.isInNames(name) and self.isInNames(name2):
            print("name not found or duplicate name")
        else:
            self.contacts[name2] = self.contacts.get(name)

    def save(self, filename):
        file = open(filename, "w")
        for x in self.contacts.items():
            file.write(x[1] + ";" + x[0] + ";" + "\n")
        file.close()

    def load(self, filename):
        file = open(filename, "r")
        self.contacts = {}
        for line in file:
            string = line.strip()
            elements = string.split(";")
            number = elements[0]
            name = elements[1]
            self.contacts.update({name: number})
        file.close()

    def main(self):
        cmds = [("add",2),("lookup",2),("alias",2),("change",2),("save",1),("load",1),("quit",1),("view",1)]

        def getArgs(arg):
            for x in cmds:
                if arg == x[0]:
                    return x[1]

        def isInCmd(cmd):
            for x in cmds:
                if cmd == x[0]:
                    return True
            return False

        while True:
            string = input("phoneBook> ")
            args = string.split()

            if args == []:
                continue
            
            elif not isInCmd(args[0]):
                print("Command not found.")

            elif args[0] == "view":
                print(self.contacts)
                
            elif args[0] == "quit":
                break    

            try:
                if args[0] == "add":
                    self.add(args[1], args[2])
                
                elif args[0] == "lookup":
                    self.lookup(args[1])
                
                elif args[0] == "alias":
                    self.alias(args[1], args[2])
                
                elif args[0] == "change":
                    self.change(args[1], args[2])

                elif args[0] == "save":
                    self.save(args[1])
                
                elif args[0] == "load":
                    self.load(args[1])
                    
            except IndexError:
                args_taken = getArgs(args[0])
                args_given = len(args)-1
                print("Command", args[0], "takes", args_taken, "argument.", args_given, "given.")
                continue

            except FileNotFoundError:
                    print("File not found")
                    continue

phonebook = Phonebook()
phonebook.main()