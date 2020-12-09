from colorama import init

from colorama import Fore, Back, Style
import random 

def Tour_Du_Joueur(Mot_A_Trouver)
    Proposition_Du_Joueur = input("Proposez un mot : ")
    if(len(Proposition_Du_Joueur) > 6:
        print("Le mot est trop grand.")
    else:
        print("Le mot est trop petit.")
    else if:
        for i in range(0,6):
            if(Proposition_Du_Joueur[i] == Mot_A_Trouver[i]):
                print(Back.RED + Proposition_Du_Joueur[i],end="")
            else : 
                print(Back.BLUE + Proposition_Du_Joueur[i],end="")
        return Proposition_Du_Joueur

input()       