###################################################
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
from enum import Enum

c = 50  # Longueur d'un côté d'une case
n = 16  # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n * c + 2
HEIGHT = WIDTH
stop = False

# Coordonnées initiales robot rouge
x0_r = 5 + 2
x1_r = 45 + 2
y0_r = 305 + 2
y1_r = 345 + 2

# Coordonnées initiales robots verts
x0_v = 55 + 2
x1_v = 95 + 2
y0_v = 55 + 2
y1_v = 95 + 2

# Coordonnées initiales robot bleu
x0_b = 605 + 2
x1_b = 645 + 2
y0_b = 205 + 2
y1_b = 245 + 2

# Coordonnées initiales robot jaune
x0_j = 155 + 2
x1_j = 195 + 2
y0_j = 105 + 2
y1_j = 145 + 2


# Création de fonctions

def quitter():
    """Fermer fenêtre"""
    racine.destroy()
    pass


def generate_wall():
    walls = [[0] * n for _ in range(n)]
    walls[0][4] = generate_binary_wall([Direction.RIGHT])
    walls[0][5] = generate_binary_wall([Direction.LEFT])
    walls[0][11] = generate_binary_wall([Direction.RIGHT])
    walls[0][12] = generate_binary_wall([Direction.LEFT])
    walls[1][1] = generate_binary_wall([Direction.DOWN])
    walls[1][6] = generate_binary_wall([Direction.LEFT, Direction.DOWN])
    walls[1][7] = generate_binary_wall([Direction.LEFT])
    walls[2][0] = generate_binary_wall([Direction.RIGHT])
    walls[2][1] = generate_binary_wall([Direction.LEFT, Direction.UP])
    walls[2][6] = generate_binary_wall([Direction.LEFT])
    walls[2][11] = generate_binary_wall([Direction.DOWN, Direction.RIGHT])
    walls[2][12] = generate_binary_wall([Direction.LEFT])
    walls[2][13] = generate_binary_wall([Direction.DOWN])
    pass


class Direction(Enum):
    UP = 0b1000
    RIGHT = 0b0100
    DOWN = 0b0010
    LEFT = 0b0001
    pass


def generate_binary_wall(directions):
    code = 0
    for direction in directions:
        code |= direction.value
    return code


nbr = 0


def clavier_rouge(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_r, x1_r, y0_r, y1_r, nbr
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   " + str(nbr)
    # déplacement vers le haut
    # déplacement vers le haut
    if touche == 'Up':
        if y0_r > 40:
            y0_r -= 50
            y1_r -= 50
        nbr += 1
    # déplacement vers le bas
    if touche == 'Down':
        if y0_r < 750:
            y0_r += 50
            y1_r += 50
        nbr += 1
    # déplacement vers la droite
    if touche == 'Right':
        if x1_r < 750:
            x0_r += 50
            x1_r += 50
        nbr += 1
    # déplacement vers la gauche
    if touche == 'Left':
        if x1_r > 50:
            x0_r -= 50
            x1_r -= 50
        nbr += 1
    print(x0_r, y0_r, x1_r, y1_r)

    canvas.coords(robot_rouge, x0_r, y0_r, x1_r, y1_r)
    texte_compteur.config(text=cpt)


# Interface graphique
racine = tk.Tk()
racine.title("Projet robot ricochet")
racine.configure(bg="gray")

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=0, column=0, rowspan=5, columnspan=1)

robot_rouge = canvas.create_oval(x0_r, y0_r, x1_r, y1_r, fill="red")
robot_vert = canvas.create_oval(x0_v, y0_v, x1_v, y1_v, fill="green")
# robot_bleu = canvas.create_oval(x0_b, y0_b, x1_b, y1_b, fill="blue")
# robot_jaune = canvas.create_oval(x0_j, y0_j, x1_j, y1_j, fill="yellow")


# Création labels/bouttons
texte_compteur = tk.Label(racine, text="Nombre de déplacements:   0")
texte_compteur.grid(row=0, column=2)

texte_resultat = tk.Label(racine, text="Jeu résolu: NON", bg="red", fg="white")
texte_resultat.grid(row=3, column=2)

boutton_quitter = tk.Button(racine, text='Quitter', command=quitter)
boutton_quitter.grid(row=4, column=2)

# Création grille 16x16 avec carré de côté 50
for ligne in range(n):
    transit = []
    for colonne in range(n):
        transit.append(canvas.create_rectangle(colonne * c + 2, ligne * c + 2,
                                               (colonne + 1) * c + 2, (ligne + 1) * c + 2))
    cases.append(transit)

# Création des murs verticaux et horizontaux et du carré central dans la grille
carre_restart = canvas.create_rectangle(350 + 2, 350 + 2, 450 + 2, 450 + 2,
                                        fill="black")

generate_wall()

canvas.focus_set()
canvas.bind('<Key>', clavier_rouge)
racine.mainloop()
