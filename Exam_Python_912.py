from colorama import init

from colorama import Fore, Back, Style
import random 

def Tour_Du_Joueur(Mot_A_Trouver):
    n=len(Mot_A_Trouver)
    print(Style.RESET_ALL)
    Proposition_Du_Joueur = input("Proposez un mot : ")
    if len(Proposition_Du_Joueur) > 6:
        print("Le mot est trop grand.")
    if len(Proposition_Du_Joueur) < 6 :
        print("Le mot est trop petit.")
    else:
        for i in range(0,6):
            for j in range(0,0+1):
                if Proposition_Du_Joueur[i] == Mot_A_Trouver[i] :
                    print(Back.RED + Proposition_Du_Joueur[i], end="")
                elif Proposition_Du_Joueur[i] == Mot_A_Trouver[j+1] :
                    print(Back.YELLOW + Proposition_Du_Joueur[i], end="")
                else :
                    print(Back.BLUE + Proposition_Du_Joueur[i], end="")

    return Proposition_Du_Joueur  
                
                
def Test_Victoire(Proposition_Du_Joueur, Mot_A_Trouver):
        if(Proposition_Du_Joueur == Mot_A_Trouver):
            Victoire = True
        else :
            Victoire = False
        return Victoire
        
def Explication_Motus():
        print("Dans motus, il faut rechercher un mots d'un nombre fixé de lettres.\n")
        print("Le mot doit contenir le bon nombre de lettres, sinon il est refusé.\n")
        print("Les lettres ont un code couleur : ")
        print("Une lettre bien placée sera indiquée en rouge.\n")
        print("Une lettre mal placée mais présente dans le mot sera indiquée en jaune.\n")
        print("Une lettre ne se trouvant pas dans le mot sera indiquée en bleu.\n")
        print("Vous avez 8 tentatives.", end="")



Liste_De_Mots = ["Cretes", "Campez", "Armure", "Argent", "Lingot", "Tondre", "Manger", "Wagons"]
Mot_Aleatoire = random.randint(0,9)
Mot_A_Trouver = Liste_De_Mots[Mot_Aleatoire]
Nombre_Tentative = 1
Victoire = False
Explication_Motus()
  
while Nombre_Tentative < 9 and Victoire != True :
    print(Style.RESET_ALL)
    print("\nTentative", Nombre_Tentative)
    Proposition_Du_Joueur = Tour_Du_Joueur(Mot_A_Trouver)
    
    Victoire=Test_Victoire(Proposition_Du_Joueur,Mot_A_Trouver)
    Nombre_Tentative = Nombre_Tentative + 1
    
    if Victoire == False :
        print("\nPerdu")
    if Victoire == True :
        print("\nBien joué")
 
input()       