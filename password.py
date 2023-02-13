from tkinter import *
import random
import string, hashlib
import os
import re


def connecter() : 
    #recuper les valeur enter sur les entry
    donnee= entry_login.get()
    mdp = entry_password.get()
    #print(mdp)
    #print(len(mdp))
    #print(donnee)
    while True:
        #on verifier si le mot de passe entré repond aux differents critère
        # et afficher un des message d'erreur sur le label erreur si une fois un des critères
        # n'est pas remplit: taille,majuscule, minuscule, chiffre, caractères speciaux
         
        if len(mdp) <= 8 or len(mdp) >= 40:
            erreur.config(text="Erreur: minimum 8 caractères! " )
            entry_login.delete(0, "end")
            entry_password.delete(0, "end")
        elif not re.search("[A-Z]", mdp):
            erreur.config(text="Erreur : Une lettre majuscule au minimun svp")
            entry_login.delete(0, "end")
            entry_password.delete(0, "end")
        elif not re.search("[a-z]", mdp):
            erreur.config(text="Erreur : une lettre miniscule au minimum ")
            entry_login.delete(0, "end")
            entry_password.delete(0, "end")
        elif not re.search("[0-9]", mdp):
            erreur.config(text="Erreur : un chiffre minimum")
            entry_login.delete(0, "end")
            entry_password.delete(0, "end")
        elif not any(char in ["!", "@", "#", "$", "%", "^", "&", "*","="] for char in mdp):
            erreur.config(text="Erreur: Un caractère special au minimum svp")
            entry_login.delete(0, "end")
            entry_password.delete(0, "end")
        else : 
            # suprimer tous les widget, augmenter la taille de la fenetre et afficher le label bienvenue
            # si le mot de passe repond à tous les critères demander
            Canvas.geometry("800x800")
            Canvas.config (bg = "blue")
            login.destroy()
            password.destroy()
            entry_login.destroy()
            entry_password.destroy()
            btn.destroy()
            Exit.destroy()
            label = Label(Canvas, text="BIENVENUE A LA PLATEFORME", font=("Arial", 32)  )
            label.grid(row=800, column=800, padx=30, pady=200)
            #print("Mot de passe valide") #Sinon le mot de passe est valide
        break
Canvas = Tk()
Canvas.title ("password")
Canvas.geometry("300x300")
Canvas.config (bg = "white")
Canvas.resizable(0,0) #fixer la taille de la fenetre
Canvas.minsize(width=250, height=250)

# label login et mot de passe
login = Label( Canvas, text="login: ")
login.grid(row=20, column=0, padx=5, pady=10, sticky="w")
password = Label( Canvas, text="password: ")
password.grid(row=21, column=0, padx=5, pady=10, sticky="w")


# les entry pour écrire le login et mot de passe
entry_login = Entry(Canvas)
entry_login.grid(row=20, column=25)
entry_password = Entry(Canvas, show= "*")
entry_password.grid(row=21, column= 25)
# creation de boutons ok et quitter
btn = Button(Canvas, text="ok", command=connecter)
btn.grid(row=23, column=10, sticky="", pady=15)
Exit = Button(Canvas, text='Quitter', command=Canvas.destroy)
Exit.grid(row=23, column=25, sticky="", pady=16)
#creér un label erreur qui s'affiche lorsque le mot de passe ne repond pas un des caractères
erreur = password = Label( Canvas, text="", fg= "red", font = "Arial")
erreur.grid(row=30, column=25)
Canvas.mainloop()