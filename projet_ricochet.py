###################################################
# Projet Robot Ricochet
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHAN
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

p = WIDTH // 16 


# Création de fonctions

def quitter():
    """Fermer fenêtre"""
    racine.destroy()
    pass

def clique(event):
    clique_x = event.x // p 
    clique_y = event.y // p
    position = (clique_x, clique_y)
    if clique_x == x0_r // p and clique_y == y0_r // p :
       canvas.bind('<Key>', clavier_rouge)
    if clique_x  == x0_v // p and clique_y  == y0_v // p :
       canvas.bind('<Key>', clavier_vert) 
    if clique_x  == x0_b // p and clique_y  == y0_b // p :
       canvas.bind('<Key>', clavier_bleu) 
    if clique_x  == x0_j // p and clique_y  == y0_j // p:
       canvas.bind('<Key>', clavier_jaune) 
   
    print(position)


def generate_wall():
    walls = [[0] * n for _ in range(n)]
    walls[0][4] = generate_binary_wall([Direction.RIGHT])
    walls[0][5] = generate_binary_wall([Direction.LEFT])
    walls[0][11] = generate_binary_wall([Direction.RIGHT])
    walls[0][12] = generate_binary_wall([Direction.LEFT])
    walls[1][1] = generate_binary_wall([Direction.DOWN])
    walls[1][6] = generate_binary_wall([Direction.DOWN, Direction.RIGHT])
    walls[1][7] = generate_binary_wall([Direction.LEFT])
    walls[2][0] = generate_binary_wall([Direction.RIGHT])
    walls[2][1] = generate_binary_wall([Direction.LEFT, Direction.UP])
    walls[2][6] = generate_binary_wall([Direction.UP])
    walls[2][11] = generate_binary_wall([Direction.DOWN, Direction.RIGHT])
    walls[2][12] = generate_binary_wall([Direction.LEFT])
    walls[2][13] = generate_binary_wall([Direction.DOWN])
    walls[3][11] = generate_binary_wall([Direction.UP])
    walls[3][13] = generate_binary_wall([Direction.RIGHT, Direction.UP])
    walls[3][14] = generate_binary_wall([Direction.LEFT])
    walls[4][6] = generate_binary_wall([Direction.DOWN])
    walls[4][9] = generate_binary_wall([Direction.RIGHT])
    walls[4][10] = generate_binary_wall([Direction.DOWN, Direction.LEFT])
    walls[4][12] = generate_binary_wall([Direction.DOWN])
    walls[5][0] = generate_binary_wall([Direction.DOWN])
    walls[5][6] = generate_binary_wall([Direction.RIGHT, Direction.UP])
    walls[5][7] = generate_binary_wall([Direction.LEFT])
    walls[5][10] = generate_binary_wall([Direction.UP])
    walls[5][11] = generate_binary_wall([Direction.RIGHT])
    walls[5][12] = generate_binary_wall([Direction.UP, Direction.LEFT])
    walls[5][15] = generate_binary_wall([Direction.DOWN])
    walls[6][0] = generate_binary_wall([Direction.UP])
    walls[6][1] = generate_binary_wall([Direction.RIGHT])
    walls[6][2] = generate_binary_wall([Direction.LEFT, Direction.DOWN])
    walls[6][7] = generate_binary_wall([Direction.DOWN])
    walls[6][8] = generate_binary_wall([Direction.DOWN])
    walls[6][15] = generate_binary_wall([Direction.UP])
    walls[7][2] = generate_binary_wall([Direction.UP])
    walls[7][6] = generate_binary_wall([Direction.RIGHT])
    walls[7][9] = generate_binary_wall([Direction.LEFT])
    walls[8][6] = generate_binary_wall([Direction.RIGHT])
    walls[8][9] = generate_binary_wall([Direction.LEFT])
    walls[8][12] = generate_binary_wall([Direction.DOWN])
    walls[9][0] = generate_binary_wall([Direction.DOWN])
    walls[9][7] = generate_binary_wall([Direction.UP])
    walls[9][8] = generate_binary_wall([Direction.UP])
    walls[9][12] = generate_binary_wall([Direction.UP, Direction.RIGHT])
    walls[9][13] = generate_binary_wall([Direction.LEFT])
    walls[9][15] = generate_binary_wall([Direction.DOWN])
    walls[10][0] = generate_binary_wall([Direction.UP])
    walls[10][3] = generate_binary_wall([Direction.DOWN, Direction.RIGHT])
    walls[10][4] = generate_binary_wall([Direction.LEFT])
    walls[10][5] = generate_binary_wall([Direction.DOWN])
    walls[10][15] = generate_binary_wall([Direction.UP])
    walls[11][3] = generate_binary_wall([Direction.UP])
    walls[11][5] = generate_binary_wall([Direction.UP, Direction.RIGHT])
    walls[11][6] = generate_binary_wall([Direction.LEFT])
    walls[11][9] = generate_binary_wall([Direction.DOWN])
    walls[12][1] = generate_binary_wall([Direction.RIGHT])
    walls[12][2] = generate_binary_wall([Direction.LEFT, Direction.DOWN])
    walls[12][4] = generate_binary_wall([Direction.DOWN])
    walls[12][8] = generate_binary_wall([Direction.RIGHT])
    walls[12][9] = generate_binary_wall([Direction.LEFT, Direction.UP])
    walls[13][2] = generate_binary_wall([Direction.UP])
    walls[13][3] = generate_binary_wall([Direction.RIGHT])
    walls[13][4] = generate_binary_wall([Direction.LEFT, Direction.UP])
    walls[13][13] = generate_binary_wall([Direction.RIGHT])
    walls[13][14] = generate_binary_wall([Direction.LEFT, Direction.DOWN])
    walls[14][11] = generate_binary_wall([Direction.RIGHT, Direction.DOWN])
    walls[14][12] = generate_binary_wall([Direction.LEFT])
    walls[14][14] = generate_binary_wall([Direction.UP])
    walls[15][3] = generate_binary_wall([Direction.RIGHT])
    walls[15][4] = generate_binary_wall([Direction.LEFT])
    walls[15][11] = generate_binary_wall([Direction.UP])
    walls[15][13] = generate_binary_wall([Direction.RIGHT])
    walls[15][14] = generate_binary_wall([Direction.LEFT])
    
    return walls


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


def get_robot_coords(x, y):
    return int((x - 7) / c), int((y - 7) / c)


nbr = 0


def clavier_rouge(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_r, x1_r, y0_r, y1_r, nbr, walls
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   " + str(nbr)
    # déplacement vers le haut
    if touche == 'Up':
        if y0_r > 40:
            x, y = get_robot_coords(x0_r, y0_r)
            if not walls[y][x] & Direction.UP.value:
                y0_r -= 50
                y1_r -= 50
                nbr += 1
        if y0_r == 407 and y1_r == 447 and x0_r == 357 and x1_r == 397:
            y0_r = 457
            y1_r = 497
        if y0_r == 407 and y1_r == 447 and x0_r == 407 and x1_r == 447:
            y0_r = 457
            y1_r = 497
        # condition mur vert
        if x0_r == x0_v and x1_r == x1_v and y0_r == y0_v and y1_r == y1_v:
            y0_r = y0_v+50
            y1_r = y1_v+50
        # condition mur jaune
        if x0_r == x0_j and x1_r == x1_j and y0_r == y0_j and y1_r == y1_j:
            y0_r = y0_j+50
            y1_r = y1_j+50
        # condition mur bleu
        if x0_r == x0_b and x1_r == x1_b and y0_r == y0_b and y1_r == y1_b:
            y0_r = y0_b+50
            y1_r = y1_b+50
    # déplacement vers le bas
    if touche == 'Down':
        if y0_r < 750:
            x, y = get_robot_coords(x0_r, y0_r)
            if not walls[y][x] & Direction.DOWN.value:
                y0_r += 50
                y1_r += 50
                nbr += 1
        if y0_r == 357 and y1_r == 397 and x0_r == 357 and x1_r == 397:
            y0_r = 307
            y1_r = 347
        if y0_r == 357 and y1_r == 397 and x0_r == 407 and x1_r == 447:
            y0_r = 307
            y1_r = 347
        # condition mur vert
        if x0_r == x0_v and x1_r == x1_v and y0_r == y0_v and y1_r == y1_v:
            y0_r = y0_v-50
            y1_r = y1_v-50
        # condition mur bleu
        if x0_r == x0_b and x1_r == x1_b and y0_r == y0_b and y1_r == y1_b:
            y0_r = y0_b-50
            y1_r = y1_b-50
        # condition mur jaune
        if x0_r == x0_j and x1_r == x1_j and y0_r == y0_j and y1_r == y1_j:
            y0_r = y0_j-50
            y1_r = y1_j-50
    # déplacement vers la droite
    if touche == 'Right':
        if x1_r < 750:
            x, y = get_robot_coords(x0_r, y0_r)
            if not walls[y][x] & Direction.RIGHT.value:
                x0_r += 50
                x1_r += 50
                nbr += 1
        if y0_r == 357 and y1_r == 397 and x0_r == 357 and x1_r == 397:
            x0_r = 307
            x1_r = 347
        if y0_r == 407 and y1_r == 447 and x0_r == 357 and x1_r == 397:
            x0_r = 307
            x1_r = 347
        # condition mur vert
        if x0_r == x0_v and x1_r == x1_v and y0_r == y0_v and y1_r == y1_v:
            x0_r = x0_v-50
            x1_r = x1_v-50
        # condition mur bleu
        if x0_r == x0_b and x1_r == x1_b and y0_r == y0_b and y1_r == y1_b:
            x0_r = x0_b-50
            x1_r = x1_b-50
        # condition mur jaune
        if x0_r == x0_j and x1_r == x1_j and y0_r == y0_j and y1_r == y1_j:
            x0_r = x0_j-50
            x1_r = x1_j-50
    if touche == 'Left':
        if x1_r > 50:
            x, y = get_robot_coords(x0_r, y0_r)
            if not walls[y][x] & Direction.LEFT.value:
                x0_r -= 50
                x1_r -= 50
                nbr += 1
        if y0_r == 407 and y1_r == 447 and x0_r == 407 and x1_r == 447:
            x0_r = 457
            x1_r = 497
        if y0_r == 357 and y1_r == 397 and x0_r == 407 and x1_r == 447:
            x0_r = 457
            x1_r = 497
        # condition mur vert
        if x0_r == x0_v and x1_r == x1_v and y0_r == y0_v and y1_r == y1_v:
            x0_r = x0_v+50
            x1_r = x1_v+50
        # condition mur bleu
        if x0_r == x0_b and x1_r == x1_b and y0_r == y0_b and y1_r == y1_b:
            x0_r = x0_b+50
            x1_r = x1_b+50
        # condition mur jaune
        if x0_r == x0_j and x1_r == x1_j and y0_r == y0_j and y1_r == y1_j:
            x0_r = x0_j+50
            x1_r = x1_j+50
    print(x0_r, y0_r, x1_r, y1_r)
    canvas.coords(robot_rouge, x0_r, y0_r, x1_r, y1_r)
    texte_compteur.config(text=cpt)

def clavier_vert(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_v, x1_v, y0_v, y1_v, nbr
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   " + str(nbr)
    # déplacement vers le haut
    if touche == 'Up':
        if y0_v > 40:
            x, y = get_robot_coords(x0_v, y0_v)
            if not walls[y][x] & Direction.UP.value:
                y0_v -= 50
                y1_v -= 50
                nbr += 1
        if y0_v == 407 and y1_v == 447 and x0_v == 357 and x1_v == 397:
            y0_v= 457
            y1_v= 497
        if y0_v == 407 and y1_v == 447 and x0_v == 407 and x1_v == 447:
            y0_v = 457
            y1_v = 497
        # condition mur rouge
        if x0_v == x0_r and x1_v == x1_r and y0_v == y0_r and y1_v == y1_r:
            y0_v = y0_r+50
            y1_v = y1_r+50
        # condition mur bleu
        if x0_v == x0_b and x1_v == x1_b and y0_v == y0_b and y1_v == y1_b:
            y0_v = y0_b+50
            y1_v = y1_b+50
        # condition mur jaune
        if x0_v == x0_j and x1_v == x1_j and y0_v == y0_j and y1_v == y1_j:
            y0_v = y0_j+50
            y1_v = y1_j+50
    # déplacement vers le bas
    if touche == 'Down':
        if y0_v < 750:
            x, y = get_robot_coords(x0_v, y0_v)
            if not walls[y][x] & Direction.DOWN.value:
                y0_v += 50
                y1_v += 50
                nbr += 1
        if y0_v == 357 and y1_v == 397 and x0_v == 357 and x1_v == 397:
            y0_v = 307
            y1_v = 347
        if y0_v == 357 and y1_v == 397 and x0_v == 407 and x1_v == 447:
            y0_v = 307
            y1_v = 347
        # condition mur rouge
        if x0_v == x0_r and x1_v == x1_r and y0_v == y0_r and y1_v == y1_r:
            y0_v = y0_r-50
            y1_v = y1_r-50
        # condition mur bleu
        if x0_v == x0_b and x1_v == x1_b and y0_v == y0_b and y1_v == y1_b:
            y0_v = y0_b-50
            y1_v = y1_b-50
        # condition mur jaune
        if x0_v == x0_j and x1_v == x1_j and y0_v == y0_j and y1_v == y1_j:
            y0_v = y0_j-50
            y1_v = y1_j-50
    # déplacement vers la droite
    if touche == 'Right':
        if x1_v < 750:
            x, y = get_robot_coords(x0_v, y0_v)
            if not walls[y][x] & Direction.RIGHT.value:
                x0_v += 50
                x1_v += 50
                nbr += 1
        if y0_v == 357 and y1_v == 397 and x0_v == 357 and x1_v == 397:
            x0_v = 307
            x1_v = 347
        if y0_v == 407 and y1_v == 447 and x0_v == 357 and x1_v == 397:
            x0_v = 307
            x1_v = 347
        # condition mur rouge
        if x0_v == x0_r and x1_v == x1_r and y0_v == y0_r and y1_v == y1_r:
            x0_v = x0_r-50
            x1_v = x1_r-50
        # condition mur bleu
        if x0_v == x0_b and x1_v == x1_b and y0_v == y0_b and y1_v == y1_b:
            x0_v = x0_b-50
            x1_v = x1_b-50
        # condition mur jaune
        if x0_v == x0_j and x1_v == x1_j and y0_v == y0_j and y1_v == y1_j:
            x0_v = x0_j-50
            x1_v = x1_j-50
    # déplacement vers la gauche
    if touche == 'Left':
        if x1_v > 50:
            x, y = get_robot_coords(x0_v, y0_v)
            if not walls[y][x] & Direction.LEFT.value:
                x0_v -= 50
                x1_v -= 50
                nbr += 1
        if y0_v == 407 and y1_v == 447 and x0_v == 407 and x1_v == 447:
            x0_v = 457
            x1_v = 497
        if y0_v == 357 and y1_v == 397 and x0_v == 407 and x1_v == 447:
            x0_v = 457
            x1_v = 497
        # condition mur rouge
        if x0_v == x0_r and x1_v == x1_r and y0_v == y0_r and y1_v == y1_r:
            x0_v = x0_r+50
            x1_v = x1_r+50
        # condition mur bleu
        if x0_v == x0_b and x1_v == x1_b and y0_v == y0_b and y1_v == y1_b:
            x0_v = x0_b+50
            x1_v = x1_b+50
        # condition mur jaune
        if x0_v == x0_j and x1_v == x1_j and y0_v == y0_j and y1_v == y1_j:
            x0_v = x0_j+50
            x1_v = x1_j+50
    print(x0_v, y0_v, x1_v, y1_v)
    canvas.coords(robot_vert, x0_v, y0_v, x1_v, y1_v)
    texte_compteur.config(text=cpt)

def clavier_bleu(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_b, x1_b, y0_b, y1_b, nbr
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   " + str(nbr)
    # déplacement vers le haut
    if touche == 'Up':
        if y0_b > 40:
            x, y = get_robot_coords(x0_b, y0_b)
            if not walls[y][x] & Direction.UP.value:
                y0_b -= 50
                y1_b -= 50
                nbr += 1
        if y0_b == 407 and y1_b == 447 and x0_b == 357 and x1_b == 397:
            y0_b= 457
            y1_b= 497
        if y0_b == 407 and y1_b == 447 and x0_b == 407 and x1_b == 447:
            y0_b = 457
            y1_b = 497
        # condition mur vert
        if x0_b == x0_v and x1_b == x1_v and y0_b == y0_v and y1_b == y1_v:
            y0_b = y0_v+50
            y1_b = y1_v+50
        # condition mur jaune
        if x0_b == x0_j and x1_b == x1_j and y0_b == y0_j and y1_b == y1_j:
            y0_b = y0_j+50
            y1_b = y1_j+50
        # condition mur rouge
        if x0_b == x0_r and x1_b == x1_r and y0_b == y0_r and y1_b == y1_r:
            y0_b = y0_r+50
            y1_b = y1_r+50
    # déplacement vers le bas
    if touche == 'Down':
        if y0_b < 750:
            x, y = get_robot_coords(x0_b, y0_b)
            if not walls[y][x] & Direction.DOWN.value:
                y0_b += 50
                y1_b += 50
                nbr += 1
        if y0_b == 357 and y1_b == 397 and x0_b == 357 and x1_b == 397:
            y0_b = 307
            y1_b = 347
        if y0_b == 357 and y1_b == 397 and x0_b == 407 and x1_b == 447:
            y0_b = 307
            y1_b = 347
        # condition mur vert
        if x0_b == x0_v and x1_b == x1_v and y0_b == y0_v and y1_b == y1_v:
            y0_b = y0_v-50
            y1_b = y1_v-50
        # condition mur jaune
        if x0_b == x0_j and x1_b == x1_j and y0_b == y0_j and y1_b == y1_j:
            y0_b = y0_j-50
            y1_b = y1_j-50
        # condition mur rouge
        if x0_b == x0_r and x1_b == x1_r and y0_b == y0_r and y1_b == y1_r:
            y0_b = y0_r-50
            y1_b = y1_r-50
    # déplacement vers la droite
    if touche == 'Right':
        if x1_b < 750:
            x, y = get_robot_coords(x0_b, y0_b)
            if not walls[y][x] & Direction.RIGHT.value:
                x0_b += 50
                x1_b += 50
                nbr += 1
        if y0_b == 357 and y1_b == 397 and x0_b == 357 and x1_b == 397:
            x0_b = 307
            x1_b = 347
        if y0_b == 407 and y1_b == 447 and x0_b == 357 and x1_b == 397:
            x0_b = 307
            x1_b = 347
        # condition mur vert
        if x0_b == x0_v and x1_b == x1_v and y0_b == y0_v and y1_b == y1_v:
            x0_b = x0_v-50
            x1_b = x1_v-50
        # condition mur jaune
        if x0_b == x0_j and x1_b == x1_j and y0_b == y0_j and y1_b == y1_j:
            x0_b = x0_j-50
            x1_b = x1_j-50
        # condition mur rouge
        if x0_b == x0_r and x1_b == x1_r and y0_b == y0_r and y1_b == y1_r:
            x0_b = x0_r-50
            x1_b = x1_r-50
    # déplacement vers la gauche
    if touche == 'Left':
        if x1_b > 50:
            x, y = get_robot_coords(x0_b, y0_b)
            if not walls[y][x] & Direction.LEFT.value:
                x0_b -= 50
                x1_b -= 50
                nbr += 1
        if y0_b == 407 and y1_b == 447 and x0_b == 407 and x1_b == 447:
            x0_b = 457
            x1_b = 497
        if y0_b == 357 and y1_b == 397 and x0_b == 407 and x1_b == 447:
            x0_b = 457
            x1_b = 497
        # condition mur vert
        if x0_b == x0_v and x1_b == x1_v and y0_b == y0_v and y1_b == y1_v:
            x0_b = x0_v+50
            x1_b = x1_v+50
        # condition mur jaune
        if x0_b == x0_j and x1_b == x1_j and y0_b == y0_j and y1_b == y1_j:
            x0_b = x0_j+50
            x1_b = x1_j+50
        # condition mur rouge
        if x0_b == x0_r and x1_b == x1_r and y0_b == y0_r and y1_b == y1_r:
            x0_b = x0_r+50
            x1_b = x1_r+50
    print(x0_b, y0_b, x1_b, y1_b)
    canvas.coords(robot_bleu, x0_b, y0_b, x1_b, y1_b)
    texte_compteur.config(text=cpt)

def clavier_jaune(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_j, x1_j, y0_j, y1_j, nbr
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   " + str(nbr)
    # déplacement vers le haut
    if touche == 'Up':
        if y0_j > 40:
            x, y = get_robot_coords(x0_j, y0_j)
            if not walls[y][x] & Direction.UP.value:
                y0_j -= 50
                y1_j -= 50
                nbr += 1
        if y0_j == 407 and y1_j == 447 and x0_j == 357 and x1_j == 397:
            y0_j= 457
            y1_j= 497
        if y0_j == 407 and y1_j == 447 and x0_j == 407 and x1_j == 447:
            y0_j = 457
            y1_j = 497
        # condition mur vert
        if x0_j == x0_v and x1_j == x1_v and y0_j == y0_v and y1_j == y1_v:
            y0_j = y0_v+50
            y1_j = y1_v+50
        # condition mur bleu
        if x0_j == x0_b and x1_j == x1_b and y0_j == y0_b and y1_j == y1_b:
            y0_j = y0_b+50
            y1_j = y1_b+50
        # condition mur rouge
        if x0_j == x0_r and x1_j == x1_r and y0_j == y0_r and y1_j == y1_r:
            y0_j = y0_r+50
            y1_j = y1_r+50
    # déplacement vers le bas
    if touche == 'Down':
        if y0_j < 750:
            x, y = get_robot_coords(x0_j, y0_j)
            if not walls[y][x] & Direction.DOWN.value:
                y0_j += 50
                y1_j += 50
                nbr += 1
        if y0_j == 357 and y1_j == 397 and x0_j == 357 and x1_j == 397:
            y0_j = 307
            y1_j = 347
        if y0_j == 357 and y1_j == 397 and x0_j == 407 and x1_j == 447:
            y0_j = 307
            y1_j = 347
        # condition mur vert
        if x0_j == x0_v and x1_j == x1_v and y0_j == y0_v and y1_j == y1_v:
            y0_j = y0_v-50
            y1_j = y1_v-50
        # condition mur bleu
        if x0_j == x0_b and x1_j == x1_b and y0_j == y0_b and y1_j == y1_b:
            y0_j = y0_b-50
            y1_j = y1_b-50
        # condition mur rouge
        if x0_j == x0_r and x1_j == x1_r and y0_j == y0_r and y1_j == y1_r:
            y0_j = y0_r-50
            y1_j = y1_r-50
    # déplacement vers la droite
    if touche == 'Right':
        if x1_j < 750:
            x, y = get_robot_coords(x0_j, y0_j)
            if not walls[y][x] & Direction.RIGHT.value:
                x0_j += 50
                x1_j += 50
                nbr += 1
        if y0_j == 357 and y1_j == 397 and x0_j == 357 and x1_j == 397:
            x0_j = 307
            x1_j = 347
        if y0_j == 407 and y1_j == 447 and x0_j == 357 and x1_j == 397:
            x0_j = 307
            x1_j = 347
        # condition mur vert
        if x0_j == x0_v and x1_j == x1_v and y0_j == y0_v and y1_j == y1_v:
            x0_j = x0_v-50
            x1_j = x1_v-50
        # condition mur bleu
        if x0_j == x0_b and x1_j == x1_b and y0_j == y0_b and y1_j == y1_b:
            x0_j = x0_b-50
            x1_j = x1_b-50
        # condition mur rouge
        if x0_j == x0_r and x1_j == x1_r and y0_j == y0_r and y1_j == y1_r:
            x0_j = x0_r-50
            x1_j = x1_r-50
    # déplacement vers la gauche
    if touche == 'Left':
        if x1_j > 50:
            x, y = get_robot_coords(x0_j, y0_j)
            if not walls[y][x] & Direction.LEFT.value:
                x0_j -= 50
                x1_j -= 50
                nbr += 1
        if y0_j == 407 and y1_j == 447 and x0_j == 407 and x1_j == 447:
            x0_j = 457
            x1_j = 497
        if y0_j == 357 and y1_j == 397 and x0_j == 407 and x1_j == 447:
            x0_j = 457
            x1_j = 497
        # condition mur vert
        if x0_j == x0_v and x1_j == x1_v and y0_j == y0_v and y1_j == y1_v:
            x0_j = x0_v+50
            x1_j = x1_v+50
        # condition mur bleu
        if x0_j == x0_b and x1_j == x1_b and y0_j == y0_b and y1_j == y1_b:
            x0_j = x0_b+50
            x1_j = x1_b+50
        # condition mur rouge
        if x0_j == x0_r and x1_j == x1_r and y0_j == y0_r and y1_j == y1_r:
            x0_j = x0_r+50
            x1_j = x1_r+50
    print(x0_j, y0_j, x1_j, y1_j)
    canvas.coords(robot_jaune, x0_j, y0_j, x1_j, y1_j)
    texte_compteur.config(text=cpt)

# Interface graphique
racine = tk.Tk()
racine.title("Projet robot ricochet")
racine.configure(bg="gray")

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=0, column=0, rowspan=5, columnspan=1)

robot_rouge = canvas.create_oval(x0_r, y0_r, x1_r, y1_r, fill="red")
robot_vert = canvas.create_oval(x0_v, y0_v, x1_v, y1_v, fill="green")
robot_bleu = canvas.create_oval(x0_b, y0_b, x1_b, y1_b, fill="blue")
robot_jaune = canvas.create_oval(x0_j, y0_j, x1_j, y1_j, fill="yellow")


# Création labels/bouttons
texte_compteur = tk.Label(racine, text="Nombre de déplacements:   0")
texte_compteur.grid(row=0, column=2)

texte_resultat = tk.Label(racine, text="Jeu résolu: NON", bg="red", fg="white")
texte_resultat.grid(row=3, column=2)

boutton_quitter = tk.Button(racine, text='Quitter', command=quitter)
boutton_quitter.grid(row=4, column=2)

canvas.bind("<Button-1>", clique)

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

walls = generate_wall()
for y, values in enumerate(walls):
    for x, value in enumerate(values):
        if value == 0:
            continue
        if value & Direction.UP.value:
            canvas.create_rectangle(x * c + 2, y * c + 2, (x + 1) * c + 2, y * c + 4, fill="black")
        if value & Direction.DOWN.value:
            canvas.create_rectangle(x * c + 2, (y + 1) * c, (x + 1) * c + 2, (y + 1) * c + 2, fill="black")
        if value & Direction.LEFT.value:
            canvas.create_rectangle(x * c + 2, y * c + 2, x * c + 4, (y + 1) * c + 2, fill="black")
        if value & Direction.RIGHT.value:
            canvas.create_rectangle((x + 1) * c, y * c + 2, (x + 1) * c + 2, (y + 1) * c + 2, fill="black")

canvas.focus_set()
racine.mainloop()
