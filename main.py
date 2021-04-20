##################################################
# Projet Robot Ricochet
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# Yanis MERBAH
# https://github.com/uvsq21915611/projet_robot
###################################################

import tkinter as tk

c = 50                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH

racine = tk.Tk()
racine.title("Projet robot ricochet")

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid()

def grille():
    for ligne in range(n):
        transit = []
        for colonne in range(n):
            transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
        cases.append(transit)
#Crée le robot et ses paramètres
def robot():
    pass

#Définit la couleur du robot / On se réfère au robot en fonction de sa couleur
def couleur_Robot():
    pass

#Définit quel robot de couleur est actuellement sélectionné
def selectionne():
    pass

#Associe les touches directionnelles du clavier "haut","bas","gauche","droite" au déplacement du robot
def bind():
    pass

#Permet de faire arrêter le robot s'il rencontre un obstacle / distance maximale de déplacement autorisé
def bounce():
    pass

#Affiche un rectangle de couleur permettant de montrer les directions possibles par le robot 
def show_Path():
    pass

#Permet de revenir une action en arrière (créer un bouton et une variable "old_Action qui stocke la position précédente et se faisant remplacer par "new_Action")
def back():
    pass

#Affiche le score / liste des meilleurs scores
def score():
    pass

#Affiche le nombre de mouvements effectués
def compteur():
    pass

#Permet d'enregistrer l'état de la partie (position des robots/nombres de mouvements/ ect ... )
def save():
    pass

#Permet de charger les éléments précédemment sauvegardés
def load():
    pass

#Permet d'éditer le plateau en rajoutant des éléments 
def editor():
    pass

racine.mainloop()