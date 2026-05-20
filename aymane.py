import json, time, sys
 
 
FILE = "testFile.json"
 
 
def create():
    data = {}
    return data
 
def read(FILE):
    with open(FILE, 'r') as file:
        jData = json.load(file)
    return jData
 
 
def update(data):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    transformInt = input("Do you want to transform the value to int? (Assuming the value you entered is a number). enter value for True, leave empty for False: ")
    data[key] = int(value) if value.isnumeric() and transformInt else value
    return data
def write(FILE, data):
    with open(FILE, 'w') as file:
        json.dump(data, file, indent=4)
 
 
def delete(data):
    try:
        choice = input("Do you want to delete a key/value pair or the whole object?\n k(ey) / o(bject): ")
        if choice == "k":
            key = input("Enter the key/value to delete: ")
            del data[key]
            return
        if choice == "o":
            del data
            return
        else:
            print("Enter a valid Value, or enter ctrl+c to go back to exit.")
            time.sleep(4)
            delete(data)
    except KeyError:
        print("Invalid key. Please enter a valid key to delete.")
        return delete(data)
 
 
def file():
    print("Changing writing file: ")
    return input("Enter file name to write to: ") + ".json"
 
def getChoice():
    choice = input("Do you want to show the help menu? y(es) / n(o) :")
    if choice == "y":
        print("show: shows the menu\ncreate: create a new data array\nread: read data from an existing Json file\nupdate: update data in memory\nwrite: write to file\ndelete: delete key/value or data from memory (Doesn't not delete the value in files)\nfile: change writing file\nexit: exits the program")
    return input("Enter c(reate) / r(ead) / u(pdate) / w(rite) / d(elete) / f(ile) / e(xit): ")
 
def menu(FILE):
    try:
        isCreate  = True
        choice = getChoice()
        file = FILE
        print(f"Currently selected JSON file is {file}")
        if choice == "c":
            data = create()
            isCreate = True
        if choice == "r":
            data = read(FILE)
            isCreate = False
 
        if len(data) == 0:
            print("No keys/values in data currently")
        else:
            for key, value in data.items():
                print(f"{key} : {value}")
 
        if choice == "u":
            update(data)
        if choice == "d":
            delete(data)
        if choice == "w":
            write(file, data)
        if choice == "f":
            file = file()
        if choice == "e":
            print("Exiting the program :) ")
            sys.exit()
    except NameError:
        print("create or read value from file before attempting to u(pdate) / d(elete) / w(rite).")
        return menu(file) if isCreate else menu(FILE)  
    except KeyboardInterrupt:
        print("Exiting the program :) ")
        sys.exit()
    return menu(file)
 
 
menu(FILE)