import json
import csv
import random
import string
myfile='students.json'
def readjson(file):
    try:
        with open(file,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def writejson(file,data):
    with open(file,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)


def addStudent():
    students=[]
    students=readjson(myfile)
    try:
        name=input("enter ur name : ")
        age=int(input("enter ur age : "))
        note=float(input("enter ur grade : "))
    except ValueError:
        print("Invalid input")
        return
    caracteres = string.ascii_lowercase + string.digits
    id_unique = "".join(random.choices(caracteres, k=6))
    new_student={"id":id_unique,"name":name,"age":age,"grade":note}
    students.append(new_student)
    writejson(myfile,students)

def affiche():
    students = readjson(myfile)
    if not students:
        print("Aucun étudiant enregistré.")
        return
    print("\n--- Liste des étudiants ---")
    for count, item in enumerate(students, start=1):
        print(count, item["id"], item["name"], item["age"], item["grade"], sep=" - ")

def search():
    id=input("enter the search id : ")
    is_exist=False
    students = readjson(myfile)
    if not students:
        print("Aucun étudiant enregistré.")
        return
    print("\n--- Liste des étudiants ---")
    for count, item in enumerate(students, start=1):
        if item["id"]==id:
            print(count, item["id"], item["name"], item["age"], item["grade"], sep=" - ")
            is_exist=True
    if not is_exist:
        print("student not found")
        return
    else:
        return
def update():
    id=input("enter the update id : ")
    is_exist=False
    students = readjson(myfile)
    if not students:
        print("Aucun étudiant enregistré.")
        return
    for item in students:
        if item["id"]==id:
            item["name"]=input("enter new name : ")
            try:
                item["age"]=int(input("enter new age : "))
                item["grade"]=float(input("enter new grade :"))
            except ValueError:
                print("invalid input")
                return
            is_exist=True
    if not is_exist:
        print("student not found")
        return
    else:
        writejson(myfile,students)
        return
def delete():
    id=input("enter the update id : ")
    is_exist=False
    students = readjson(myfile)
    if not students:
        print("Aucun étudiant enregistré.")
        return
    for item in students:
        if item["id"]==id:
            students.remove(item)
            is_exist=True
    if not is_exist:
        print("student not found")
        return
    else:
        writejson(myfile,students)
        return








