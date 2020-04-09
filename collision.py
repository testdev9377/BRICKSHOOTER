import turtle
import os
import gameComponent
import math
import random

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

def checkCollision(indice):

    #Check for a collision between the bullet and the enemy
    
    if isCollision(gameComponent.bullet, gameComponent.enemies[indice]):

        #Reset the bullet
        
        gameComponent.bullet.hideturtle()
        gameComponent.bulletstate = "ready"
        gameComponent.bullet.setposition(0, -400)
  
        #Reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        gameComponent.enemies[indice].setposition(x, y)
        
        #Update the score
        gameComponent.score += 10
        gameComponent.scorestring = "Score: %s" %gameComponent.score
        gameComponent.score_pen.clear()
        gameComponent.score_pen.write(gameComponent.scorestring, False, align="left", font=("Arial", 14, "normal"))
        
    if isCollision(gameComponent.player, gameComponent.enemies[indice]):
        
        gameComponent.player.hideturtle()
        gameComponent.enemies[indice].hideturtle()
        gameComponent.quitterJeu()
    
