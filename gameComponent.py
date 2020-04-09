import turtle
import os
import random
import tkinter as tk
import main



def sauvegarde():
    

    #now = datetime.now()
    #date1 = now.strftime("%d/%m/%Y %H:%M:%S")
    
    donnees[dic_sauvegarde["score"]] = score
    donnees[dic_sauvegarde["credit"]] += score

    if donnees[dic_sauvegarde["score"]] > donnees[dic_sauvegarde["best_score"]]:
        donnees[dic_sauvegarde["best_score"]] = donnees[dic_sauvegarde["score"]]
    #print("MEILLEUR : " + str((donnees[dic_sauvegarde["best_score"]] )))
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
                    #print(str(elem))
                    if i != 0:
                        donnees[i] = int(donnees[i])
                    i += 1

    except IOError:
        #print("pas de fichier")
        return False



#Definit le terrain de jeu, le joueur, son missile et les ennemies ( fond d'ecran et joueur)
def quitterJeu():
    
     #donnes sauvegarder
    # global donnees
    # donnees = [0] * 6

    # global dic_sauvegarde
    # dic_sauvegarde = {
    # "nom":0, 
    # "score":1, 
    # "credit":2,
    # "vaisseau":3,
    # "missile":4,
    # "best_score":5
    # }        
    # #print("clicked Quitter")
    # turtle.Terminator
    main.fin = True
    #os.sys.exit(2)
    canvas = turtle.getcanvas()
    parent = canvas.master
    border_pen.clear()
    wn.clear()    
    
    lecture()
    sauvegarde()



    #Affichage Fin de Partie
    chaine = """    Partie Terminé !!!
    
    Votre score est de {} points

    Vous gagnez donc {} credits !!! 

    Vous avez en tout {} credits !!! 

    Votre meilleure score est de {} points

    """.format(donnees[dic_sauvegarde["score"]], donnees[dic_sauvegarde["score"]], donnees[dic_sauvegarde["credit"]], donnees[dic_sauvegarde["best_score"]] )
    
    turtle.color('black')
    style = ('Verdana', 14, 'italic')
    turtle.write(chaine, font=style, align='center')
    turtle.hideturtle()
    #print("Fin de partie")


    turtle.done()

    os.sys.exit(2)

    


def parametres():

    """
    ********************************
    * Paramètres fond d'écran du jeu
    ********************************
    """
    #dossier actuelle
    thePath = os.path.abspath(os.path.split(__file__)[0])
    global wn
    wn = turtle.Screen()
    wn.bgpic(thePath + "/background/background.gif")
    #wn.bgpic("background.gif")
    wn.bgcolor("black")
    wn.title("BRICK SHOOTER")
   

    #Register the shapes
    turtle.register_shape(thePath + "/ennemy/invader.gif")
    turtle.register_shape(thePath + "/player/player.gif")

    #turtle.register_shape("player.gif")
    #turtle.register_shape("invader.gif")

    #Draw border
    global border_pen
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()	

    """
    ********************************
    * Paramètres score 
    ********************************
    """
    global score
    global score_pen
    #Set the score to 0
    score = 0

    #Draw the score
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290, 280)
    scorestring = "Score: %s" %score
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    lecture()
    #Draw the Highest score
    best_score_pen = turtle.Turtle()
    best_score_pen.speed(0)
    best_score_pen.color("white")
    best_score_pen.penup()
    best_score_pen.setposition(100, 280)
    scorestring = "Meilleure Score: %s" %donnees[dic_sauvegarde["best_score"]]
    best_score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    best_score_pen.hideturtle()

    """
    ********************************
    * Paramètres du joueur
    ********************************
    """    
    
    global playerspeed
    global player
    

    if donnees[dic_sauvegarde["vaisseau"]] == 1:
        playerspeed = 15
    elif donnees[dic_sauvegarde["vaisseau"]] == 2:
        playerspeed = 30
    elif donnees[dic_sauvegarde["vaisseau"]] == 3:
        playerspeed = 45

    player = turtle.Turtle()
    player.color("blue")
    player.shape(thePath + "/player/player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    """
    ********************************
    * Paramètres du missile du joeur
    ********************************
    """
    global bulletstate
    global bullet
    global bulletspeed
    bulletspeed = 10
    if donnees[dic_sauvegarde["missile"]] == 1:
        bulletspeed = 10
    elif donnees[dic_sauvegarde["missile"]] == 2:
        bulletspeed = 15
    elif donnees[dic_sauvegarde["missile"]] == 3:
        bulletspeed = 20

    bulletstate = "ready"
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    """
    ********************************
    * Paramètres des ennemies
    ********************************
    """

    global enemyspeed
    global enemies
    global number_of_enemies

    enemies = []
    #Choose a number of enemies
    number_of_enemies = 5
    speed = 5
    enemyspeed = []
  

    #Add enemies to the list
    for i in range(number_of_enemies):
        
        #add the enemy speed
        enemyspeed.append(speed)

    #Add enemies speed
    for i in range(number_of_enemies):
        
        #Create the enemy
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("red")
        enemy.shape(thePath + "/ennemy/invader.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

    #Bouton quitter
    canvas = turtle.getcanvas()
    parent = canvas.master

    button3 = tk.Button(parent, text='Quitter', command=quitterJeu)
    bt_quitter = canvas.create_window((350,275), window=button3)
    #list_Button[dic_index["bt_quitter"]] = bt_quitter
    
