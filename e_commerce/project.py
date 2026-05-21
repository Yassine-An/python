import json
card=[]
def main_menu():
    print("Hello to our e-commerce website")
    print("1_BUYER")
    print("2_SELLER")
    print("0_EXIT")
    while True:
        try:
            choix=int(input("Entrer votre choix : "))
            if choix in [0,1,2]:
              return choix
            else:
               print("invalid choix")
        except ValueError:
            print("invalid input")
def buyer_menu():
    print("Hello BUYER")
    print("1_Add to card")
    print("2_Remove from card")
    print("0_EXIT")
    while True:
        try:
            choix=int(input("Entrer votre choix : "))
            if choix in [0,1,2]:
              return choix
            else:
               print("invalid choix")
        except ValueError:
            print("invalid input")
def seller_menu():
    print("Hello SELLLER")
    print("1_Add item")
    print("2_update item")
    print("3_delete item")
    print("0_EXIT")
    while True:
        try:
            choix=int(input("Entrer votre choix : "))
            if choix in [0,1,2,3]:
              return choix
            else:
               print("invalid choix")
        except ValueError:
            print("invalid input")
def display_list():
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
        for item in products:
            print(item)
    except FileNotFoundError:
        print("Aucun produit disponible pour le moment.")
def add_to_card():
    global card
    try:
        id=int(input("enter item id : "))
    except ValueError:
        print("invalid input")
        return
    with open("products.json","r") as file:
        products=json.load(file)
    for item in products:
        if item["id"]==id:
            card.append(item)
    validate=input("valider votre commande y/n : ")
    if validate.lower()=="y":
        valide()
    else:
       return
def remove_from_card():
    global card
    if not card:
        print("Your card is empty.")
        return
    print("Current card:", card)
    try:
        idx = int(input("enter item id to remove : "))
    except ValueError:
        print("invalid input")
        return
    initial_length = len(card)
    nouvelle_carte = []
    for item in card:
        if item["id"] != idx:
            nouvelle_carte.append(item)
    card = nouvelle_carte
    if len(card) < initial_length:
        print("Item removed from card.")
    else:
        print("Item not found in your card.")

def valide():
    global card
    with open("card.json","w",encoding="utf-8") as file:
        json.dump(card,file,indent=4)
    card.clear()
def additem():
    donnes=[]
    with open("products.json","r",encoding="utf-8") as fichier:
        donnes=json.load(fichier)
    item_name=input("enter item name : ")
    try :
        item_price=int(input("entrer item price : "))
    except ValueError:
        print("invalid input")
        return
    if len(donnes)==0:
        new_donnes={"id":1,"name":item_name,"price":item_price}
    else:
        new_donnes={"id":len(donnes)+1,"name":item_name,"price":item_price}
    donnes.append(new_donnes)
    with open("products.json","w",encoding="utf-8") as fichier:
            json.dump(donnes,fichier,indent=4)
    return
def update():
    try :
        id=int(input("entrer l'identifiant : "))
    except ValueError:
        print("invalid input")
        return
    with open("products.json","r",encoding="utf-8") as file:
        data=json.load(file)
    for item in data:
        if item["id"]==id:
            item["name"]=input("enter new name : ")
            try:
                item["price"]=int(input("enter new price : "))
            except ValueError:
                print("price invalid")
                return
    with open("products.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4)
    return
def delete():
    try :
        id=int(input("entrer l'identifiant : "))
    except ValueError:
        print("invalid input")
        return
    new_data=[]
    with open("products.json","r",encoding="utf-8") as file:
        data=json.load(file)
    for item in data:
        if item["id"]==id:
            continue
        else:
            new_data.append(item)
    with open("products.json","w",encoding="utf-8") as file:
        json.dump(new_data,file,indent=4)
    return 
def main():
    while True:
        choix_principal = main_menu()
        if choix_principal == 0:
            print("BYEEEEEEEEEEEE")
            break
        elif choix_principal == 1:
            while True:
                display_list()
                choix_buyer = buyer_menu()
                if choix_buyer == 1:
                    add_to_card()
                elif choix_buyer == 2:
                    remove_from_card()
                elif choix_buyer == 0:
                    break  

        elif choix_principal == 2:
            while True:
                choix_seller = seller_menu()
                if choix_seller == 1:
                    additem()
                elif choix_seller == 2:
                    update()
                elif choix_seller == 3:
                    delete()
                elif choix_seller == 0:
                    break
        elif choix_principal == 0:
            exit()
main()