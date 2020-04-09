import turtle
import os
import gameComponent

def setTheMoves(indice):
    
    #Move the enemy
    x = gameComponent.enemies[indice].xcor()
    x += gameComponent.enemyspeed[indice]
    gameComponent.enemies[indice].setx(x)
    
    #Move the enemy back and down
    if gameComponent.enemies[indice].xcor() > 280 or gameComponent.enemies[indice].xcor() < -280:
        y = gameComponent.enemies[indice].ycor()
        y -= 50
        gameComponent.enemies[indice].sety(y)
        gameComponent.enemyspeed[indice] *= -1


  


            