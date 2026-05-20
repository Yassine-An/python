wagon = []
annule = []
wagon.extend([None]*60)
ind_fumeur=0
ind_non_fumeur=30
indice=0
def reserve() :
    global indice
    global ind_fumeur
    global ind_non_fumeur
    name=input("inserer votre nom : ")
    cond=input("Tu es fumeur y/n:")
    if cond=="y" and ind_fumeur<30:
       wagon.pop(ind_fumeur)
       wagon.insert(ind_fumeur,name)
       ind_fumeur +=1
    elif cond=="n" and ind_non_fumeur<60 :
       wagon.pop(ind_non_fumeur)
       wagon.insert(ind_non_fumeur,name)
       ind_non_fumeur +=1
    elif "NULL" in wagon :
        if cond=="y" and indice<30 :
            wagon.pop(indice)
            wagon.insert(indice,name)
        elif cond=="n" and indice>30 and indice<60:
            wagon.pop(indice)
            wagon.insert(indice,name)
    else :
        print("no empty places")
def annuler() :
    global indice
    nom=input("inserer votre nom : ")
    if nom in wagon :
        indice = wagon.index(nom)
        wagon.pop(indice)
        wagon.insert(indice,"NULL")
    else : 
        print("no place reservez pour ce nom")
while True :
    print("1_Reserver")
    print("2_Annuler")
    print("3_Quiter")
    choise = int(input("entrer votre choix : "))
    match(choise) :
        case 1 : reserve()
        case 2 : annuler()
        case 3 :break
        case 4 : print(wagon)

        