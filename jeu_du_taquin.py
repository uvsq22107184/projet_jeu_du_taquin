# jeu du taquin projet programation fin d'année l1

import tkinter as tk
import random as rd
from turtle import undo

LARGEUR = 600
HAUTEUR = 400





















racine = tk.Tk()
canvas = tk.Canvas(bg="black", width=LARGEUR, height=HAUTEUR)
bouton = tk.Button(text="Retour arrière", command=undo)
canvas.grid()
bouton.grid(row=1)
racine.mainloop()