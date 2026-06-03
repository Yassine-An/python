import math
import array
import csv
import json
import random
'''
i = 1
s=0
while i<=5 :
   print(i)
   i += 1 '''
'''while i <=5 :
   print(i,end="")
   if i < 5 :
      print("+",end="")
   s+=i
   i+=1
print("=",s)'''
'''
def somme(num1,num2) :
    return num1+num2
def moins(num1,num2) :
    return num1-num2
def multi(num1,num2) :
    return num1*num2
def div(num1,num2) :
    try :
        return num1/num2
    except ZeroDivisionError :
        print("impossible de diriver sur 0")
num1=int(input("entrer num 1 : "))
num2=int(input("entrer num 2 : "))
print(somme(num1,num2))
print(moins(num1,num2))
print(multi(num1,num2))
print(div(num1,num2))
'''
'''
a=int(input("entrer a "))
b=int(input("entrer b "))
c=int(input("entrer c "))
d=int(input("entrer d "))
temp=0
temp=a
a=b
b=c
c=d
d=temp
print(a)
print(b)
print(c)
print(d)
'''
'''
num1=int(input("entrer num 1 : "))
num2=int(input("entrer num 2 : "))
if num1>=num2 :
    print(num1,"est grand")
else :
    print(num2,"est grand")
'''
'''
num1=int(input("entrer num 1 : "))
num2=int(input("entrer num 2 : "))
num3=int(input("entrer num 3 : "))
max=num1
if num2>num1 and num2>num3 :
    print(num2,"est le max")
elif num3>num1 and num3>num2 :
    print(num3,"est le max")
else :
    print(num1,"est le max")
'''
'''
a=int(input("entrer a : "))
b=int(input("entrer b : "))
c=int(input("entrer c : "))
delta=b**2-(4*a*c)
print("delta est : ",delta)
if delta<0:
    print("l'equation n'admait aucun solution")
elif delta == 0 :
    s1=-b/2*a
    print("la solution est",s1)
else :
    s1=(-b-math.sqrt(delta))/2*a
    s2=(-b+math.sqrt(delta))/2*a
    print("Solution 1 est : ",s1)
    print("Solution 2 est : ",s2)
'''
'''
s=0
coeff=1
for i in range(1,6) :
    note=float(input(f"entrer note {i} : "))
    s +=note*coeff
    moy=s/5
print("moyen est : ",moy)
'''
'''
num=int(input("entrer number : "))
for i in range(1,11) :
    print(f"{num}*{i} = ",num*i)
'''
'''
st=""
som=0
num=int(input("entrer number : "))
for i in range(1,num+1) :
    st+=str(i)+"+"
    som +=i
st = st[:-1] #remove last caractere in the chaine
st += "="+str(som)
print(st)
'''
'''
st=""
som=0
num=int(input("entrer number : "))
for i in range(1,num+1) :
   if i%2==0 :
      st+=str(i)+"+"
      som -=i
   else :
      st +=str(i)+"-"
      som+=i
st = st[:-1] #remove last caractere in the chaine
st += "="+str(som)
print(st)
'''
'''
def fact(num) :
   if num==0 :
      return 1
   else :
      return num*fact(num-1)
num=int(input("entrer number : "))
print("le factoriel est : ",fact(num))
'''
'''
note = []
coeff = []
s=0
moy=0
som=0
for i in range(0,5) :
   val = int(input(f"entrer note {i+1}"))
   coef=int(input(f"entrer coef {i+1}"))
   note.append(val)
   coeff.append(coef)
   som+=coef
   s+=note[i]*coeff[i]

moy=s/som
print("le moyen est ",moy)
'''
'''
s=0
i=0
moy=0
num=int(input("entrer des nombres"))
a=num
b=num
if num==0 :
    print("no data insert ")
else:
    while num!=0:
        num=int(input("entrer des nombres"))
        if num>=a :
            a=num
        if num<=b and num!=0 :
            b=num
        s+= num
        i+=1
    moy=s/i
    print(f"le max est {a} et le min est {b} et le moyen est {moy}")
'''

'''
while True :
   num=int(input("entrer nombre : "))
   if num==0 :
    break
'''
'''
bol=True
while bol :
  num=int(input("entrer num : "))
  if num==0 :
    bol=False'''
'''
for i in range(0,101) :
    if i%5==0 :
        continue
    else :
        print(i)
'''
'''
for i in range(0,10) :
    for j in range(0,i) :
        print("*",end="")
    print("")
'''
'''
for i in range(10,0,-1) :
    for j in range(i,0,-1) :
        print("*",end="")
    print("")
'''
'''
for i in range(0,10) :
    for j in range(10,i,-1) :
        print(" ",end="")
    for k in  range(0,2*i-1) :
       print("*",end="") 
    print("")
'''
'''
for i in range(10,0,-1) :
    for j in range(0,10-i+1) :
        print(" ",end="")
    for k in  range(0,2*i-1) :
       print("*",end="") 
    print("")
'''
'''
for i in range(0,10) :
    for j in range(10,i,-1) :
        print(" ",end="")
    for k in  range(0,2*i-1) :
       print("*",end="") 
    print("")
for i in range(8,0,-1) :
    for j in range(1,10-i+1) :
        print(" ",end="")
    for k in  range(0,2*i-1) :
       print("*",end="") 
    print("")
'''
'''
for i in range(9,0,-1) :
    for j in range(1,10-i) :
        print(" ",end="")
    for k in  range(0,2*i-1) :
       print("*",end="")
    print("")
for i in range(1,9) :
    for j in range(8,i,-1) :
        print(" ",end="")
    for k in  range(-2,2*i-1) :
       print("*",end="") 
    print("")
'''
'''
for i in range(3,0,-1):
    for j in range(i-1,0,-1):
        print(" ",end="")
    for k in range(0,(4-i)*3):
        print("*",end="")
    print("")
for i in range(1,5):
    for j in range(0,i):
        print(" ",end="")
    for k in range(8,2*i-1,-1):
        print("*",end="")
    print("")
'''
'''list.sort(reverse=True)#sort() ktreteb tasa3odi , reverse=true ktrtb tanazoli'''
'''
list = []
s=0
for i in range(0,5) :
    x=int(input(f"entrer la valeur {i+1} : "))
    list.append(x)
for x in list :
    s +=x
print(s)
'''
'''
list = []
while True :
    x = input("entrer val : ")
    if x == "stop" :
       break
    else:
      list.append(x)
for x in list :
   print(x)
print(list)
'''
'''
list = [1,2,3,8]
for index,val in enumerate(list,start=0) :
    print(index,val)
'''
'''
list = [1,1,3,4,5,5,7,7]
list2 = []
for x in list :
    if x not in list2 :
        list2.append(x)
print(list2)
'''
'''
list = []
list2 = []
conca = []
for i in range(0,5) :
    list.append(input(f"entrer valeur {i+1} de list 1  : "))
    list2.append(input(f"entrer valeur {i+1} de list 2 : "))
for x in list+list2:
    if x not in conca :
       conca.append(x) 
           
print(conca)
'''
'''
list = []
list2 = []
conca = []
for i in range(0,5) :
    list.append(input(f"entrer valeur {i+1} de list 1  : "))
    list2.append(input(f"entrer valeur {i+1} de list 2 : "))
for x in list+list2:
    if x in list and x in list2 and x not in conca :
       conca.append(x) 
print(conca)
'''
'''
#le nombre exist plus d'un seul fois
list = [1,10,1,5,8,22,100]
val=int(input("entrer un nombre : "))
for i in range(len(list)) :
    if val == list[i] :
       print("exist in ",i)
    else :
       continue
'''
'''
#le nombre exist seul fois
list = [1,10,5,8,22,100]
val=int(input("entrer un nombre : "))
if val in list :
    print("exist in ",list.index(val))
else :
    print("doesn't exist")
'''
'''
list = []
val=int(input("entrer des valeur : "))
list.append(val)
max=list[0]
min=list[0]
i=0
while True :
    val=int(input("entrer des valeur : "))
    list.append(val)
    if max < list[i] :
        max=list[i]
    if min > list[i] :
        min = list[i]
    if val == 0 :
        break
    i +=1
print(f"le max est {max} dans la place {list.index(max)} and le min est {min} dans la place {list.index(min)}")
'''
'''
note = []
nom = []
nom.append(input("entrer nom : 1"))
note.append(float(input("entrer note : 1")))
max=note[0]
min=note[0]
indice=0
ind = 0
for i in range(1,4) :
    nom.append(input("entrer nom : "))
    note.append(float(input("entrer note : ")))
for index,note in enumerate(note,start=0) :
    if note>=10:
        print(f"etudiant {nom[index]} avait la note {note}")
    if max < note :
        max=note
        ind=index
    if min > note :
        min = note
        indice = index
print(f"le premier est {nom[ind]} qui avait la note {max} et le dernier est {nom[indice]} qui avait la note {min}")
'''
'''
t = (12,3,12,5,12,33)
val = int(input("inserer un nombre"))
if val in t :
    print(t.count(val))
else :
    print("n'existe pas")
'''
'''
t = (12,3,12,5,12,33)
val = int(input("inserer un nombre"))
ind=1
if val in t :
    for i in range(len(t)):
        if t[i]==val :
            print(f"{ind} occurance dans la place {i}")
            ind+=1
else :
    print("n'existe pas")
'''
'''
list = [3,5,9,10]
val = int(input("inserer un nombre"))
for x in list :
    if val > x :
        indice = list.index(x)
        
list.insert(indice+1,val)     
print(list)
'''
'''
list = [3,5,9,10]
indice=0
def inserer(ind,val):
    if ind==len(list):
        list.append(val)
    else :
       list.append(val)
       for i in range(len(list)-1,ind,-1):
           temp=list[i]
           list[i]=list[i-1]
           list[i-1]=temp

val = int(input("inserer un nombre"))
for i in range(len(list)) :
    if val < list[i] :
        indice=i
        break
    else:
        indice=len(list)
inserer(indice,val)
print(list)
'''
'''
list = [3,5,9,10]
l = []

while True :
   bol = True
   val = int(input("inserer un nombre"))
   if val == 0:
    break
   else :
    for x in list :
      if x > val and bol == True :
        l.append(val)
        l.append(x)
        bol = False
        print("1")
        
      elif x not in l :
        l.append(x) 
        print("2")    
    if  bol :
      l.append(val)  
      print("3")
print(l)
'''

'''
list = [3,5,9,11,10,11]
max=0
maxx=0
for x in list :
    if x>max:
        maxx=max
        max=x
    elif x>maxx and x!=max  :
        maxx=x
print(maxx)
print(max)
'''
'''
list=[]
bol=True
word=input("entrer une mots : ")
word = word.lower().replace(" ","") 
for i in range(len(word)-1,-1,-1) :
    list.append(word[i])
for i in range(0,len(list)):
    if word[i]!=list[i]:
        bol = False
if bol :
    print("true")
else:
    print("false")
print(word)
print(list)
'''
'''
word=input("entrer une mots : ")
word = word.lower().replace(" ", "") 
word_2=word[::-1]
if word==word_2 :
    print("True")
else:
    print("false")
'''
'''
def somme(i,n):
    if i>n:
        return 0
    else:
        return i+somme(i+1,n)
print(somme(5,10))
'''
'''
def bonjour():
    print("bonjour")
bonjour()
'''
'''
def somme(a,b):
    s=a+b
    p=a*b
    return s,p
t=somme(int(input("entrer num 1 : ")),int(input("entrer num 2 : ")))
for x in t:
    print(x)
'''
'''
def maxim(a,b):
    max=a
    if max<b:
      max=b
    return max
print(maxim(10,12))
'''
'''
def calcul(*a):
    return sum(a),max(a)
x=calcul(1,2,3,4,5,6,7,8)
print(x)
'''
'''
def affich(**list):
    return list
st=affich(name="yassine",prename="anifag",age=20)
for x in st.items():
    print(x)
'''
'''
def est_pair(a):
    return a%2==0
print(est_pair(3))
'''
'''
def care(a):
    return a**2
print(care(3))
'''
'''
def vowels(word):
  vow="aeiyou"
  list = []
  indice=0
  for char in word :
    if char in vow:
        indice+=1
        list.append(char)
  if indice==0:
    print("no vowel exist")
  else :
    for i in range(0,indice) :
       print(f"{i+1} vowel est {list[i]} ")
word=input("entrer une mots : ")
vowels(word)
'''
'''
indice=0
def vowels(word,i=0):
  word.lower()
  vow="aeiyou"
  global indice
  if i>=len(word):
        return indice
  else :
      if word[i] in vow:
        indice+=1
        return vowels(word,i+1)
      else :
         return vowels(word,i+1)
          
print(vowels("yassine"))
'''
'''
list=[]
def plindrome(word,i=0):
   word = word.lower().replace(" ","")
   if i>=len(word):
       word2 = "".join(list)
       return word == word2
   else:
       list.insert(0,word[i])
       return plindrome(word,i+1)
    
word=input("entrer une mots : ")
if plindrome(word) :
    print("plindrome")
else:
    print("not plindrome")
'''


'''
list=[("mohammed",19),("yassine",22),("abderrahim",67),("imad",50)]
max=0
for x in list:
for i in range(len(x)-1) :
        print(x[i])'''
'''for i in range(len(x)-1) :
        if x[i+1]>=21:
            print(x[i])'''
'''
for i in range(len(list)-1):
    for j in range(len(list)-1):
       if list[j][1]>list[j+1][1]:
           temp=list[j]
           list[j]=list[j+1]
           list[j+1]=temp
for i in range(len(list)):
    if list[i][1]>max:
        max=list[i][1]
        max_name=list[i][0]
def count(list):
    i=0
    for x in list:
        i+=1
    return i
print(f"count is : {len(list)}")
list.sort()
'''
'''
list.sort(key=lambda x:x[1])
print(list)
'''
'''
for i in range(len(list)-1):
    for j in range(len(list)-1):
       if list[j][0][0]>list[j+1][0][0]:
           temp=list[j]
           list[j]=list[j+1]
           list[j+1]=temp
print(list)
'''
'''
lst=[]
name=input("entrer nom : ")
age=int(input("entrer age : "))
if age >= 18 :
    lst.append(name)
    lst.append(age)
    t=tuple(lst)
    list.append(t)
else:
    print("mineur")
print(list)
'''
'''
num=int(input("entrer un number : "))
care=lambda x : x**2
print(care(num))
'''
'''
num=int(input("entrer un number : "))
isPositive=lambda x :"positive" if x>=0 else "negative"
print(isPositive(num))
'''
'''
lst=["python","java","c"]
l=tuple(map(lambda x : x.upper(),lst))
print(l)
'''
'''
lst=["3","5","3"]
l=tuple(map(lambda x : int(x)*10,lst))
print(l)
'''
'''
lst=[("mohammed",19),("yassine",22),("abderrahim",67),("imad",50)]
l = list(map(lambda x: x if x[1] >= 21 else None, lst))
l.remove(None)
print(l)
'''
'''
lst=[("mohammed",19),("yassine",22),("abderrahim",67),("imad",50)]
l=list(filter(lambda x: x[1]>20 ,lst))
print(l)
'''
'''
personne={"nom":"zineb",
          "age":20,
          "note":0
          }
for cle,valeur in personne.items():
    print(cle,valeur)
print(personne.items())
'''
'''
indice=0
general=0
personne={"ali":18,
          "ysn":20,
          "abderrahim":15
          }

for cle,valeur in personne.items():
    general+=valeur
    indice+=1
moy=general/indice
print(moy)
'''
'''
personne={"ali":18,
          "ysn":20,
          "abderrahim":15
          }
nom=input("entrer un nom : ")
for cle,valeur in personne.items():
    if cle == nom :
        print(valeur)
    else:
        continue
'''
'''
items=[]
def create_item():
    item={}
    name=input("enter item name : ")
    price=float(input("enter item price : "))
    item["name"]=name
    item["price"]=price
    items.append(item)
def delete_item():
    name=input("enter item name : ")
    for x in items:
        for cle,valeur in x.items():
            if valeur==name:
                items.remove(x)
def update_item():
    name=input("enter item name : ")
    for x in items:
        for cle,valeur in x.items():
            if valeur==name:
                name=input("enter new item name : ")
                price=float(input("enter new item price : "))
                x["name"]=name
                x["price"]=price
while True:
    print("1-create item")
    print("2-show items")
    print("3-delete item")
    print("4-update item")
    print("5-exit")
    choix=int(input("enter ur choise : "))
    match(choix):
        case 1 :create_item()
        case 2 :print(items)
        case 3:delete_item()
        case 4:update_item()
        case 5 :break
'''

'''
for x in items:
    for cle,value in x.items():
        myfile.write(str(value))
        myfile.write("  :  ")
'''
'''
indice=1
myfile=open('exe.txt','r')
content = myfile.read()
for char in content :
    if char == " ":
       indice+=1
print(indice)
myfile.close()
'''
'''
word=input("entrer une mot : ")
myfile=open('exe.txt','r')
content=myfile.read()
words=content.split()
if word not in words:
    myfile=open('exe.txt','a')
    myfile.write(word+"\n")
else:
    print("exist deja")
'''
'''
word = input("entrer un mot : ")
rep = input("entrer le mot pour remplacer : ")

myfile=open('exe.txt', 'r') 
content = myfile.read()

if word in content:
    content = content.replace(word, rep)
myfile=open('exe.txt', 'w')
myfile.write(content)
print(content)
myfile.close()
'''
'''
myfile = open('exe.txt', 'r')
content = myfile.read()
words = content.split()
item = {}
for word in words:
    if word not in item:
        item[word] = 1
    else:
        item[word] += 1
print(item)
'''
'''
myfile = open('exe.txt', 'r')
content = myfile.read()
myfile.close()
myfile2 = open('file', 'r')
content2 = myfile2.read()
myfile.close()
merge=open('merged.txt','w')
merge.write(content+"\n"+content2)
merge.close
merge=open('merged.txt','r')
full_content=merge.read()
print(full_content)
merge.close()
'''

# class Person:
#     def __init__(self,nom,prenom):
#         self.name=nom
#         self.prename=prenom
#     def show_info(self):
#         return f"hello {self.name} {self.prename} "
# class Man(Person):
#     def __init__(self, nom, prenom,gender):
#         super().__init__(nom, prenom)
#         self.genre=gender
#     def show_info(self):
#         str = super().show_info()
#         return str+f" u are a {self.genre}"
# class Women(Person):
#     def __init__(self, nom, prenom,gender):
#         super().__init__(nom, prenom)
#         self.genre=gender
#     def show_info(self):
#         return f"hello Miss {self.name} {self.prename} u are a {self.genre} "
# man=Man("imad","elhandi","man")
# women=Women("hafsa","elidrissi","women")
# print(man.show_info());
# fichier=open("test.csv","r")
# lecteurcsv=csv.reader(fichier,delimiter=";")
# lst=list(lecteurcsv)
# lst.sort(key=lambda row:int(row[1]))
# fichier.close()
# lst=[["prénom",17],["abderrahim",18],["imad",21],["yassine",22]]
# fichier=open("test.csv","w",newline='',encoding="utf-8")
# writercsv=csv.writer(fichier,delimiter=";")
# for line in lst:
#     writercsv.writerow(line)
#     print
# fichier.close()
# def addEtudiant():
#     donnes=[]
#     with open("exe.json","r",encoding="utf-8") as fichier:
#         donnes=json.load(fichier)
#     name=input("entrer le nom de l'étudiant : ")
#     age=int(input("entrer l'age de l'étudiant : "))
#     new_donnes={"name":name,"age":age}
#     donnes.append(new_donnes)
#     with open("exe.json","w",encoding="utf-8") as fichier:
#             json.dump(donnes,fichier,indent=4)
# def update():
#     name=input("entrer le nom de l'étudiant : ")
#     with open("exe.json","r",encoding="utf-8") as fichier:
#         donnes=json.load(fichier)
#         for item in donnes:
#             if item["name"]==name:
#                 name=input("new name : ")
#                 age=int(input("new age : "))
#                 item["name"]=name
#                 item["age"]=age
#     with open("exe.json","w",encoding="utf-8") as fichier:
#         json.dump(donnes,fichier,indent=4)
# def delete():
#     new_donnes=[]
#     name=input("entrer le nom de l'étudiant : ")
#     with open("exe.json","r",encoding="utf-8") as fichier:
#         donnes=json.load(fichier)
#         for item in donnes :
#             if name!=item["name"]:
#                 new_donnes.append(item)
#     with open("exe.json","w",encoding="utf-8") as fichier:
#         json.dump(new_donnes,fichier,indent=4)        
# def affiche():
#     i=1
#     with open("exe.json","r",encoding="utf-8") as fichier:
#         donnes=json.load(fichier)
#     for item in donnes:
#         print(f"etudiant {i} : ",item)
#         i+=1
# while True:
#     print("1_Ajouter Etudiant")
#     print("2_Update")
#     print("3_delete")
#     print("4_afficher")
#     print("0_break")
#     choix=int(input("entrer votre choix : "))
#     match(choix):
#         case 1:addEtudiant()
#         case 2:update()
#         case 3:delete()
#         case 4:affiche()
#         case 0:break
<<<<<<< HEAD



    
=======
# try:
#     num1=int(input("enter first number : "))
#     num2=int(input("enter second number : "))
#     result=num1/num2
#     print(result)
# except ZeroDivisionError:
#     print("impossible de diriver par 0")
# except ValueError:
#     print("invalid input")
# while True:
#     num1=int(input("enter first number : "))
#     num2=int(input("enter second number : "))
#     try:
#        result=num1/num2
#        print(result)
#        break
#     except ZeroDivisionError:
#        print("impossible de diriver par 0")
# def drivier():
#     a=int(input("enter first number : "))
#     b=int(input("enter second number : "))
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("impossile de diriver par 0")
#         return drivier()
# print(drivier())
# ////////////////////////////////
# while True:
#     num1=int(input("enter first number : "))
#     num2=int(input("enter second number : "))
#     try:
#        result=num1/num2
#        print(result)
#     except ZeroDivisionError:
#        print("impossible de diriver par 0")
    # finally:
    #     print("abc")
    #     executed in all cases
# num1=int(input("enter first number : "))
# num2=int(input("enter second number : "))
# if num2==0:
#     raise ZeroDivisionError("impossible de diriver par 0")
# else:
#     result=num1/num2
#     print(result)
file_name="users.json"
def read_json(file):
    try:  
        with open(file, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return [] 
def write_json(file,data):
    with open(file,"w",encoding="utf-8") as fichier:
        json.dump(data,fichier,indent=4)
    return 
def show_menu():
    print("HEELLOOOO USEEEEEER")
    print("1_Login as admin")
    print("2_Create account")
    print("0_Exit")
    while True:
        try:
            choix=int(input("Enter ur choise... "))
            if choix in [0,1,2]:
               return choix
            else:
               print("Please choose :) ")
        except ValueError:
           print("input invalid")
def login():
    username=input("Enter usename : ")
    passwd=input("Enter ur password : ")
    info=read_json(file_name)
    for user in info:
        if user["username"]==username and user["password"]==passwd:
            print("Hello admin :) ")
            exit()
    print("Email or password inccorect")
    try:
        choix=input("Did u forget ur passwd y/n ...")
    except ValueError:
        print("invalid input")
    if choix=="y":
        return reset_passwd()
    elif choix=="n":
        return
def reset_passwd():
    try:
        code=int(input("Enter ur verification code : "))
    except ValueError:
        print("invalid input")
        return
    info=read_json(file_name)
    for user in info:
        if user["verif-code"]==code:
            try:
                user["password"] = input("enter new password : ")
            except ValueError:
                print("input invalid")
                return
            write_json(file_name, info)
            print("Password updated successfully!")
            return
    print("User not found :( ")
def create_account():
    while True:
        username=input("Enter usename : ")
        passwd=input("Enter ur password : ")
        code=random.randint(100000,999999)
        is_exist=False
        users=read_json(file_name)
        for user in users:
            if user['username']==username:
                is_exist=True
        if is_exist:
            print("Username already exist :) ")
        elif username.isalpha():
           info=read_json(file_name)
           new_info={"username":username,"password":passwd,"verif-code":code}
           info.append(new_info)
           write_json(file_name,info)
           return new_info
        else:
            print("username must only have letters")
def main():
    while True:
        choix=show_menu()
        if choix==0 :
           print("Are u leaving :) ")
           break
        elif choix==1:
           login()
        elif choix==2:
           user=create_account()
           print(f"{user['username']} ur account has been created this is ur verification code {user['verif-code']}")
           print("Don't forget it !!!!! took a screen :) ")
main()
>>>>>>> 6fe5e16c0018c0e8eea1defcc7986d665244c9f7
