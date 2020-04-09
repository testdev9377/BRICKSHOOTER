import turtle
import tkinter as tk

import os
import playerMoves  
import ennemiesMoves 
import bulletMoves
import collision
import main


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)


def sauvegarde():

    #now = datetime.now()
    #date1 = now.strftime("%d/%m/%Y %H:%M:%S")
    
    f = open('sauvegarde.txt',"w", encoding = 'utf-8')
    f.write(os.getenv("USERNAME") + ';' + str(donnees[dic_sauvegarde["score"]]) + ';' + str(donnees[dic_sauvegarde["credit"]]) + ';' + str(donnees[dic_sauvegarde["vaisseau"]]) + ';' + str(donnees[dic_sauvegarde["missile"]])+ ';' + str(donnees[dic_sauvegarde["best_score"]]))
    f.close()

def lecture():
    
    #donnes sauvegarder
    global donnees
    donnees = [0] * 6

    global dic_sauvegarde
    dic_sauvegarde = {
    "nom":0, 
    "score":1, 
    "credit":2,
    "vaisseau":3,
    "missile":4,
    "best_score":5
    }     
    
    try:
        with open('sauvegarde.txt', 'r') as f:
            
            for ligne in f:
                donnees = ligne.split(";")
                i = 0
                for elem in donnees:
                    #print("Element " + str(i) + " : " +str(elem))
                    if i != 0:
                        if (i == 3 or i == 4) and int(donnees[i]) == 0:
                            donnees[i] = 1
                        else:
                            donnees[i] = int(donnees[i])
                    i += 1

    except IOError:
        #print("pas de fichier")
        return False

def majEquipement():
    

    #effacement ancien affichage
    turtle.clear()
    
    try:
        credit_pen.clear()
        vaisseau_pen.clear()
        missile_pen.clear()
        list_Button[dic_index["prix"]].clear()
    except:
        pass

    #effacement ancien bouton
    canvas.delete(list_Button[dic_index["bt_vaisseau"]])
    canvas.delete(list_Button[dic_index["bt_vaisseau2"]])
    canvas.delete(list_Button[dic_index["bt_equip"]])
    canvas.delete(list_Button[dic_index["bt_retour"]])
    canvas.delete(list_Button[dic_index["bt_jouer"]])
    canvas.delete(list_Button[dic_index["bt_missile"]])
    canvas.delete(list_Button[dic_index["bt_missile2"]])
    canvas.delete(list_Button[dic_index["bt_quitter"]])
    

def lancementJeu():
    sauvegarde()
    majEquipement()

    main.jeu()
    
def quitterJeu():
    
    #print("clicked Quitter")
    try:
        pass
        #this.finDePartie()
        main.fin = True
        finDePartie
        #affichage score

    except:
        pass
    #finDePartie
    os.sys.exit(2)

def affichageRegle():
    

    #effacement ancien bouton
    canvas.delete(list_Button[dic_index["bt_equip"]])
    canvas.delete(list_Button[dic_index["bt_regle"]])
    canvas.delete(list_Button[dic_index["bt_jouer"]])
    list_Button[dic_index["titre"]].clear()

    #affichage bouton retour
    button4 = tk.Button(parent, text='Retour', command=retour)
    bt_retour = canvas.create_window((-350,275), window=button4)
    list_Button[dic_index["bt_retour"]] = bt_retour

    #affichage regle
    regle = """    Le but de ce jeu est de détruire un maximum de monstre 
    avant de se faire toucher. Chaque monstre tués rapporte 10 points au score.
    Le jeu se finit lorsque vous décider de le quitter ou lorsqu'un monstre vous touche

    A la fin de votre partie , votre est enregistré et est converti en crédit. 
    10 points correspond à 10 Crédits. 
    
    Avec vos Crédits vous pourrez acheter des equipements
    pour ameliorer la vitesse de votre vaisseau et votre vitesse de tir
    Il y a 3 niveaux de vaisseau et de missiles .
    
    Votre score, vos equipements et vos crédits seront sauvegardés lorsque vous quittez le jeu

    Amusez vous bien !!!
    
    """

    turtle.color('black')
    style = ('Verdana', 14, 'italic')
    turtle.write(regle, font=style, align='center')
    turtle.hideturtle()
    
    

    # sample = turtle.Turtle()
    # pen = sample.getpen()
    # # 'Helloworld" text will show up on your screen
    # pen.write(regle) 
    # # 'Helloworld' will be disapeared as you type it on console.
    # pen.clear()
    # pen.delete()


def popupmsg(msg):
    
    popup = tk.Tk()
    popup.wm_title("Felicitations")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def ameliorerMissile():

    if donnees[dic_sauvegarde["credit"]] >= 150:
        
        donnees[dic_sauvegarde["missile"]] += 1
        donnees[dic_sauvegarde["credit"]] -= 150
        popupmsg("Bravo !!! Votre missile passe au niveau {}".format(donnees[dic_sauvegarde["missile"]] ))
        majEquipement()
        sauvegarde()
        choixEquipement()
    else:
        popupmsg("Vous n'avez pas assez de crédit")
        sauvegarde()

def ameliorerVaisseau():
    global donnees
    lecture()
    if donnees[dic_sauvegarde["credit"]] >= 150:
        
        donnees[dic_sauvegarde["vaisseau"]] += 1
        donnees[dic_sauvegarde["credit"]] -= 150
        popupmsg("Bravo !!! Votre vaisseau passe au niveau {}".format(donnees[dic_sauvegarde["vaisseau"]] ))
        majEquipement()
        sauvegarde()
        choixEquipement()
    else:

        popupmsg("Vous n'avez pas assez de crédit")
        sauvegarde()

def desagregerMissile():

    if donnees[dic_sauvegarde["credit"]] >= 150:
        
        donnees[dic_sauvegarde["missile"]] -= 1
        donnees[dic_sauvegarde["credit"]] -= 150
        popupmsg("Votre missile repasse au niveau {}".format(donnees[dic_sauvegarde["missile"]] ))
        majEquipement()
        sauvegarde()
        choixEquipement()
    else:
        popupmsg("Vous n'avez pas assez de crédit")
        sauvegarde()

def desagregerVaisseau():
    global donnees
    lecture()
    if donnees[dic_sauvegarde["credit"]] >= 150:
        
        donnees[dic_sauvegarde["vaisseau"]] -= 1
        donnees[dic_sauvegarde["credit"]] -= 150
        popupmsg("Votre vaisseau repasse au niveau {}".format(donnees[dic_sauvegarde["vaisseau"]] ))
        majEquipement()
        sauvegarde()
        choixEquipement()
    else:

        popupmsg("Vous n'avez pas assez de crédit")
        sauvegarde()

def choixEquipement():


 
    #effacement ancien bouton
    canvas.delete(list_Button[dic_index["bt_equip"]])
    canvas.delete(list_Button[dic_index["bt_regle"]])
    canvas.delete(list_Button[dic_index["bt_quitter"]])
    list_Button[dic_index["titre"]].clear()

    # Recupere les donnes sauvegarder
    lecture() 
    
    #pour le cas ou il n'y a aucune données
    #print("Test " + str(donnees[dic_sauvegarde["vaisseau"]]))
    if donnees[dic_sauvegarde["vaisseau"]] == 0:
        donnees[dic_sauvegarde["vaisseau"]] = 1
    ameVaisseau = donnees[dic_sauvegarde["vaisseau"]]

    if donnees[dic_sauvegarde["missile"]] == 0:
        donnees[dic_sauvegarde["missile"]] = 1
    
    ameMissile = donnees[dic_sauvegarde["missile"]]


    # #Determine les ameliorations
    # ameVaisseau = 0
    # ameMissile = 0
    # if donnees[dic_sauvegarde["vaisseau"]] < 3:
    #     ameVaisseau = donnees[dic_sauvegarde["vaisseau"]]
    # if donnees[dic_sauvegarde["missile"]] < 3:
    #     ameMissile = donnees[dic_sauvegarde["missile"]]

    #affichage bouton retour
    button4 = tk.Button(parent, text='Retour', command=retour)
    bt_retour = canvas.create_window((-350,275), window=button4)
    list_Button[dic_index["bt_retour"]] = bt_retour

    #affichage bouton missile + 
    if ameMissile < 3:
        chaine = 'Ameliorer MISSILE au Niveau ' + str(ameMissile + 1)
        button5 = tk.Button(parent, text= chaine, command=ameliorerMissile)
        bt_missile = canvas.create_window((-100,-130), window=button5)
        list_Button[dic_index["bt_missile"]] = bt_missile

    #affichage bouton vaisseau +
    if ameVaisseau < 3:
        chaine = 'Ameliorer VAISSEAU au Niveau ' + str(ameVaisseau + 1)
        button6 = tk.Button(parent, text=chaine, command=ameliorerVaisseau)
        bt_vaisseau = canvas.create_window((-100,-210), window=button6)
        list_Button[dic_index["bt_vaisseau"]] = bt_vaisseau

    #affichage bouton missile -
    if ameMissile > 1:
        chaine = 'Diminuer niveau MISSILE au ' + str(ameMissile - 1)
        button8 = tk.Button(parent, text= chaine, command=desagregerMissile)
        bt_missile2 = canvas.create_window((200,-130), window=button8)
        list_Button[dic_index["bt_missile2"]] = bt_missile2

    #affichage bouton vaisseau -
    if ameVaisseau > 1:
        chaine = 'Dimminuer Niveau VAISSEAU au ' + str(ameVaisseau - 1)
        button9 = tk.Button(parent, text=chaine, command=desagregerVaisseau)
        bt_vaisseau2 = canvas.create_window((200,-210), window=button9)
        list_Button[dic_index["bt_vaisseau2"]] = bt_vaisseau2

    #affichage bouton jouer
    button7 = tk.Button(parent, text='JOUER !!!', command=lancementJeu)
    bt_jouer = canvas.create_window((0,0), window=button7)
    list_Button[dic_index["bt_jouer"]] = bt_jouer

    #declaration affichage
    global credit_pen
    global vaisseau_pen
    global missile_pen

    #Bouton quitter
    button3 = tk.Button(parent, text='Quitter', command=quitterJeu)
    bt_quitter = canvas.create_window((350,275), window=button3)
    list_Button[dic_index["bt_quitter"]] = bt_quitter


    # Affiche les credits
    credit = donnees[dic_sauvegarde["credit"]]
    credit_pen = turtle.Turtle()
    credit_pen.speed(0)
    credit_pen.color("black")
    credit_pen.penup()
    credit_pen.setposition(-450, 280)
    creditstring = "Crédit = %s" %credit
    credit_pen.write(creditstring, False, align="left", font=("Arial", 14, "normal"))
    credit_pen.hideturtle()


    # Affiche les prix
    prix = 150
    prix_pen = turtle.Turtle()
    prix_pen.speed(0)
    prix_pen.color("black")
    prix_pen.penup()
    prix_pen.setposition(0, 280)
    prix_string = "Prix = %s" %prix + " Crédits"
    prix_pen.write(prix_string, False, align="left", font=("Arial", 14, "normal"))
    prix_pen.hideturtle()
    
    list_Button[dic_index["prix"]] = prix_pen

    # Affiche le niveau du vaisseau
    vaisseau = donnees[dic_sauvegarde["vaisseau"]]
    vaisseau_pen = turtle.Turtle()
    vaisseau_pen.speed(0)
    vaisseau_pen.color("black")
    vaisseau_pen.penup()
    vaisseau_pen.setposition(-450, 200)
    vaisseaustring = "Niveau du vaisseau = %s" %vaisseau
    vaisseau_pen.write(vaisseaustring, False, align="left", font=("Arial", 14, "normal"))
    vaisseau_pen.hideturtle()

    # Affiche le niveau du missile
    missile = donnees[dic_sauvegarde["missile"]]
    missile_pen = turtle.Turtle()
    missile_pen.speed(0)
    missile_pen.color("black")
    missile_pen.penup()
    missile_pen.setposition(-450, 120)
    missilestring = "Niveau du Missile = %s" %missile
    missile_pen.write(missilestring, False, align="left", font=("Arial", 14, "normal"))
    missile_pen.hideturtle()
    

    # if lecture() == True:
    #     #print("yes")
    # else:
    #     #print("yes")


def retour():

    #effacement ancien affichage
    turtle.clear()

    try:
        credit_pen.clear()
        vaisseau_pen.clear()
        missile_pen.clear()
        list_Button[dic_index["prix"]].clear()
    except:
        pass

    #effacement ancien bouton
    canvas.delete(list_Button[dic_index["bt_retour"]])
    canvas.delete(list_Button[dic_index["bt_vaisseau"]])
    canvas.delete(list_Button[dic_index["bt_vaisseau2"]])
    canvas.delete(list_Button[dic_index["bt_missile"]])
    canvas.delete(list_Button[dic_index["bt_missile2"]])
    canvas.delete(list_Button[dic_index["bt_jouer"]])
    

    #affichage Bouton Menu
    button1 = tk.Button(parent, text='Choix Equipement', command=choixEquipement)
    bt_equip = canvas.create_window((0,-50), window=button1)
    
    button2 = tk.Button(parent, text='Règles du jeu', command=affichageRegle)
    bt_regle = canvas.create_window((0,0), window=button2)

    list_Button[dic_index["bt_equip"]] = bt_equip
    list_Button[dic_index["bt_regle"]] = bt_regle

    titre = "BRICK SHOOTER"

    #Draw the score
    titre_pen = turtle.Turtle()
    titre_pen.speed(0)
    titre_pen.color("black")
    titre_pen.penup()
    titre_pen.setposition(0, 200)
    titre_string = titre
    titre_pen.write(titre_string, False, align="center", font=("Verdana", 25, "normal"))
    titre_pen.hideturtle()
    list_Button[dic_index["titre"]] = titre_pen

if __name__ == "__main__":
    #liste des boutons
    global list_Button
    list_Button = [1] * 11

    #index des boutons
    global dic_index
    dic_index = {
        "bt_equip":0, 
        "bt_regle":1, 
        "bt_quitter":2,
        "bt_retour":3,
        "bt_vaisseau":4,
        "bt_missile":5,
        "bt_jouer":6,
        "bt_vaisseau2":7,
        "bt_missile2":8,
        "titre":9,
        "prix":10
    }

    global canvas
    global parent

    canvas = turtle.getcanvas()
    parent = canvas.master
    
    #Bouton equipement
    button1 = tk.Button(parent, text='Choix Equipement', command=choixEquipement)
    bt_equip = canvas.create_window((0,-50), window=button1)
    list_Button[dic_index["bt_equip"]] = bt_equip

    #Bouton Regle
    button2 = tk.Button(parent, text='Règles du jeu', command=affichageRegle)
    bt_regle = canvas.create_window((0,0), window=button2)
    list_Button[dic_index["bt_regle"]] = bt_regle

    #Bouton quitter
    button3 = tk.Button(parent, text='Quitter', command=quitterJeu)
    bt_quitter = canvas.create_window((350,275), window=button3)
    list_Button[dic_index["bt_quitter"]] = bt_quitter
    
  
    titre = "BRICK SHOOTER"

    #Draw the score
    titre_pen = turtle.Turtle()
    titre_pen.speed(0)
    titre_pen.color("black")
    titre_pen.penup()
    titre_pen.setposition(0, 200)
    titre_string = titre
    titre_pen.write(titre_string, False, align="center", font=("Verdana", 25, "normal"))
    titre_pen.hideturtle()
    list_Button[dic_index["titre"]] = titre_pen
    
    turtle.done()