import os
import gameComponent
import playerMoves  
import ennemiesMoves 
import bulletMoves
import collision

def jeu():
  
    #Definit le terrain de jeu ( fond d'ecran et joueur)
    gameComponent.parametres()

    #Definit les mouvements du joueur
    playerMoves.setTheMoves()

     #Definit les mouvements de la balle
    bulletMoves.fire_bullet()
    global fin
    fin = False

    #Boucle du Jeu
    while(fin == False):

        indice = 0 
            
        #boucle sur chaque ennemies
        for ennemi in gameComponent.enemies:

            #ajoute aleatoirement un ennemi 
            
            #Definit les mouvements des ennemies
            ennemiesMoves.setTheMoves(indice)

            #Determine la collision entre les divers composants
            if collision.checkCollision(indice) == False:
                fin = True
                break
            indice += 1

        #Definit les mouvements de la balle
        bulletMoves.setTheMoves()