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

c = 40                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH

racine = tk.Tk()
racine.title("Projet robot ricochet")

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row =1, column =0, rowspan=4)

#création grille
for ligne in range(n):
    transit = []
    for colonne in range(n):
        transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)

#création des mur (obstacle)
mur_vertical1 = canvas.create_rectangle(200-2, 0, 200+5, 40+2, fill="black")
mur_vertical2 = canvas.create_rectangle(480-2, 0, 480+5, 40+2, fill="black")
mur_vertical3 = canvas.create_rectangle(280-2, 40+2, 280+5, 80+2, fill="black")
mur_vertical4 = canvas.create_rectangle(40-2, 80+2, 40+5, 120+2, fill="black")
mur_vertical5 = canvas.create_rectangle(480-2, 80+2, 480+5, 120+2, fill="black")
mur_vertical6 = canvas.create_rectangle(560-2, 120+2, 560+5, 160+2, fill="black")
mur_vertical7 = canvas.create_rectangle(400-2, 160+2, 400+5, 200+2, fill="black")
mur_vertical8 = canvas.create_rectangle(280-2, 200+2, 280+5, 240+2, fill="black")
mur_vertical9 = canvas.create_rectangle(480-2, 200+2, 480+5, 240+2, fill="black")
mur_vertical10 = canvas.create_rectangle(80-2, 240+2, 80+5, 240+2, fill="black")
mur_vertical11 = canvas.create_rectangle(520-2, 360+2, 520+5, 400+2, fill="black")
mur_vertical12 = canvas.create_rectangle(160-2, 400+2, 160+5, 440+2, fill="black")
mur_vertical13 = canvas.create_rectangle(240-2, 440+2, 240+5, 480+2, fill="black")
mur_vertical14 = canvas.create_rectangle(80-2, 480+2, 80+5, 520+2, fill="black")
mur_vertical15 = canvas.create_rectangle(360-2, 480+2, 360+5, 520+2, fill="black")
mur_vertical16 = canvas.create_rectangle(160-2, 520+2, 160+5, 560+2, fill="black")
mur_vertical17 = canvas.create_rectangle(560-2, 520+2, 560+5, 560+2, fill="black")
mur_vertical18 = canvas.create_rectangle(480-2, 560+2, 480+5, 600+2, fill="black")
mur_vertical19 = canvas.create_rectangle(160-2, 600+2, 160+5, 640, fill="black")
mur_vertical20 = canvas.create_rectangle(560-2, 600+2, 560+5, 640, fill="black")

mur_horizontal1 = canvas.create_rectangle(40+2, 80-2, 80+2, 80+5, fill="black")
mur_horizontal2 = canvas.create_rectangle(240+2, 80-2, 280+2, 80+5, fill="black")
mur_horizontal3 = canvas.create_rectangle(440+2, 120-2, 480+2, 120+5, fill="black")
mur_horizontal4 = canvas.create_rectangle(520+2, 120-2, 560+2, 120+5, fill="black")
mur_horizontal5 = canvas.create_rectangle(240+2, 200-2, 280+2, 200+5, fill="black")
mur_horizontal6 = canvas.create_rectangle(400+2, 200-2, 440+2, 200+5, fill="black")
mur_horizontal7 = canvas.create_rectangle(480+2, 200-2, 520+2, 200+5, fill="black")
mur_horizontal8 = canvas.create_rectangle(0,240-2, 40+2, 240+5, fill="black")
mur_horizontal9 = canvas.create_rectangle(600+2, 240-2, 640+2, 240+5, fill="black")
mur_horizontal10 = canvas.create_rectangle(80+2, 280-2, 120+2, 280+5, fill="black")
mur_horizontal11 = canvas.create_rectangle(480+2, 360-2, 520+2, 360+5, fill="black")
mur_horizontal12 = canvas.create_rectangle(0, 400-2, 40+2, 400+5, fill="black")
mur_horizontal13 = canvas.create_rectangle(600+2, 400-2, 640+2, 400+5, fill="black")
mur_horizontal14 = canvas.create_rectangle(120+2, 440-2, 160+2, 440+5, fill="black")
mur_horizontal15 = canvas.create_rectangle(200+2, 440-2, 240+2, 440+5, fill="black")
mur_horizontal16 = canvas.create_rectangle(360+2, 480-2, 400+2, 480+5, fill="black")
mur_horizontal17 = canvas.create_rectangle(80+2, 520-2, 120+2, 520+5, fill="black")
mur_horizontal18 = canvas.create_rectangle(160+2, 520-2, 200+2, 520+5, fill="black")
mur_horizontal19 = canvas.create_rectangle(560+2, 560-2, 600+2, 560+5, fill="black")
mur_horizontal20 = canvas.create_rectangle(440+2, 600-2, 480+2, 600+5, fill="black")

carre_restart = canvas.create_rectangle(280+2, 280+2, 360+2, 360+2, fill="black")


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

#Fait recommencer le jeu
def reset():
    """ Redémarre le programme """
    python = sys.executable
    os.execl(python,python, * sys.argv)

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




#Bouton label etc...
# Création d'un widget Button (bouton Quitter)
quitter = tk.Button(racine, text ='Quitter', command = racine.destroy)
quitter.grid(row=6, column=0)

recommencer = tk.Button(racine, text="Reset", command=reset)
recommencer.grid(row=2, column= 0, rowspan=2)




racine.mainloop()
