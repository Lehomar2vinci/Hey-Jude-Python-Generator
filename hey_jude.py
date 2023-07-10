import random

def afficher_couplets():
    couplets = [
        "Make it better",
        "Take a sad song and make it better",
        "Remember to let her into your heart",
        "Then you can start to make it better"
    ]
    
    random.shuffle(couplets)  # Randomise l'ordre des couplets
    
    print("Hey Jude")
    
    for couplet in couplets:
        print(couplet)
    
    print("Better better better better better waaaaaa")

def demander_recommencer():
    while True:
        reponse = input("Voulez-vous réécouter 'Hey Jude' ? (Oui/Non) ")
        if reponse.lower() == "oui":
            return True
        elif reponse.lower() == "non":
            return False
        else:
            print("Veuillez répondre par 'Oui' ou 'Non'.")

recommencer = True

while recommencer:
    afficher_couplets()
    recommencer = demander_recommencer()
