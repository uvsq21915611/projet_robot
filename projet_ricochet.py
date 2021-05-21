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

c = 50                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH
stop = False

# Coordonnées initiales robot rouge
x0_r = 5+2
x1_r = 45+2
y0_r = 305+2
y1_r = 345+2

# Coordonnées initiales robots verts
x0_v = 55+2
x1_v = 95+2
y0_v = 55+2
y1_v = 95+2

# Coordonnées initiales robot bleu
x0_b = 605+2
x1_b = 645+2
y0_b = 205+2
y1_b = 245+2

# Coordonnées initiales robot jaune
x0_j = 155+2
x1_j = 195+2
y0_j = 105+2
y1_j = 145+2

# Création de fonctions

def quitter():
    """Fermer fenêtre"""
    racine.destroy()
    pass

nbr = 0
def clavier_rouge(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global x0_r, x1_r, y0_r, y1_r, nbr
    touche = event.keysym
    print(touche)
    cpt = "Nombre de déplacements:   "+ str(nbr)
    # déplacement vers le haut
    if touche == 'Up':
        if y0_r != 5 and y1_r != 45:
            y0_r -= 800
            y1_r -= 800
            if y0_r < 5:
                y0_r = 5
                y1_r = 45
        #HITBOX
        nbr +=1
    # déplacement vers le bas
    if touche == 'Down':
        if y0_r != 755 and y1_r != 795:
            y0_r += 800
            y1_r += 800
            if y0_r > 755:
                y0_r = 755
                y1_r = 795
        #HITBOX
        nbr +=1
    # déplacement vers la droite
    if touche == 'Right':
        if x0_r != 755 and x1_r != 795:
            x0_r += 800
            x1_r += 800
            if x0_r > 755:
                x0_r = 755
                x1_r = 795
        #HITBOX
        nbr +=1
    # déplacement vers la gauche
    if touche == 'Left':
        if x0_r != 5 and x1_r != 45:
            x0_r -= 800
            x1_r -= 800
            if x0_r < 5:
                x0_r = 5
                x1_r = 45
        #HITBOX
        nbr +=1
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
        transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2,
                                               (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)

# Création des murs verticaux et horizontaux et du carré central dans la grille
carre_restart = canvas.create_rectangle(350+2, 350+2, 450+2, 450+2,
                                        fill="black")
mur_vertical1 = canvas.create_rectangle(250-2, 0, 250+5, 50+2,
                                        fill="black")
mur_vertical2 = canvas.create_rectangle(600-2, 0, 600+5, 50+2,
                                        fill="black")
mur_vertical3 = canvas.create_rectangle(350-2, 50+2, 350+5, 100+2,
                                        fill="black")
mur_vertical4 = canvas.create_rectangle(50-2, 100+2, 50+5, 150+2,
                                        fill="black")
mur_vertical5 = canvas.create_rectangle(600-2, 100+2, 600+5, 150+2,
                                        fill="black")
mur_vertical6 = canvas.create_rectangle(700-2, 150+2, 700+5, 200+2,
                                        fill="black")
mur_vertical7 = canvas.create_rectangle(500-2, 200+2, 500+5, 250+2,
                                        fill="black")
mur_vertical8 = canvas.create_rectangle(350-2, 250+2, 350+5, 300+2,
                                        fill="black")
mur_vertical9 = canvas.create_rectangle(600-2, 250+2, 600+5, 300+2,
                                        fill="black")
mur_vertical10 = canvas.create_rectangle(100-2, 300+2, 100+5, 350+2,
                                         fill="black")
mur_vertical11 = canvas.create_rectangle(650-2, 450+2, 650+5, 500+2,
                                         fill="black")
mur_vertical12 = canvas.create_rectangle(200-2, 500+2, 200+5, 550+2,
                                         fill="black")
mur_vertical13 = canvas.create_rectangle(300-2, 550+2, 300+5, 600+2,
                                         fill="black")
mur_vertical14 = canvas.create_rectangle(100-2, 600+2, 100+5, 650+2,
                                         fill="black")
mur_vertical15 = canvas.create_rectangle(450-2, 600+2, 450+5, 650+2,
                                         fill="black")
mur_vertical16 = canvas.create_rectangle(200-2, 650+2, 200+5, 700+2,
                                         fill="black")
mur_vertical17 = canvas.create_rectangle(700-2, 650+2, 700+5, 700+2,
                                         fill="black")
mur_vertical18 = canvas.create_rectangle(600-2, 700+2, 600+5, 750+2,
                                         fill="black")
mur_vertical19 = canvas.create_rectangle(200-2, 750+2, 200+5, 800,
                                         fill="black")
mur_vertical20 = canvas.create_rectangle(700-2, 750+2, 700+5, 800,
                                         fill="black")
mur_horizontal1 = canvas.create_rectangle(50+2, 100-2, 100+2, 100+5,
                                          fill="black")
mur_horizontal2 = canvas.create_rectangle(300+2, 100-2, 350+2, 100+5,
                                          fill="black")
mur_horizontal3 = canvas.create_rectangle(550+2, 150-2, 600+2, 150+5,
                                          fill="black")
mur_horizontal4 = canvas.create_rectangle(650+2, 150-2, 700+2, 150+5,
                                          fill="black")
mur_horizontal5 = canvas.create_rectangle(300+2, 250-2, 350+2, 250+5,
                                          fill="black")
mur_horizontal6 = canvas.create_rectangle(500+2, 250-2, 550+2, 250+5,
                                          fill="black")
mur_horizontal7 = canvas.create_rectangle(600+2, 250-2, 650+2, 250+5,
                                          fill="black")
mur_horizontal8 = canvas.create_rectangle(0, 300-2, 50+2, 300+5,
                                          fill="black")
mur_horizontal9 = canvas.create_rectangle(750+2, 300-2, 800+2, 300+5,
                                          fill="black")
mur_horizontal10 = canvas.create_rectangle(100+2, 350-2, 150+2, 350+5,
                                           fill="black")
mur_horizontal11 = canvas.create_rectangle(600+2, 450-2, 650+2, 450+5,
                                           fill="black")
mur_horizontal12 = canvas.create_rectangle(0, 500-2, 50+2, 500+5,
                                           fill="black")
mur_horizontal13 = canvas.create_rectangle(750+2, 500-2, 800+2, 500+5,
                                           fill="black")
mur_horizontal14 = canvas.create_rectangle(150+2, 550-2, 200+2, 550+5,
                                           fill="black")
mur_horizontal15 = canvas.create_rectangle(250+2, 550-2, 300+2, 550+5,
                                           fill="black")
mur_horizontal16 = canvas.create_rectangle(450+2, 600-2, 500+2, 600+5,
                                           fill="black")
mur_horizontal17 = canvas.create_rectangle(100+2, 650-2, 150+2, 650+5,
                                           fill="black")
mur_horizontal18 = canvas.create_rectangle(200+2, 650-2, 250+2, 650+5,
                                           fill="black")
mur_horizontal19 = canvas.create_rectangle(700+2, 700-2, 750+2, 700+5,
                                           fill="black")
mur_horizontal20 = canvas.create_rectangle(550+2, 750-2, 600+2, 750+5,
                                           fill="black")




canvas.focus_set()
canvas.bind('<Key>',clavier_rouge)
racine.mainloop()
