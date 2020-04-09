import turtle
import os
import gameComponent
        
def setTheMoves():

        
    #Move the bullet
    if gameComponent.bulletstate == "fire":
        y = gameComponent.bullet.ycor()
        y += gameComponent.bulletspeed
        gameComponent.bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if gameComponent.bullet.ycor() > 275:
        gameComponent.bullet.hideturtle()
        gameComponent.bulletstate = "ready"
    
def fire_bullet():
    
    if gameComponent.bulletstate == "ready":
        gameComponent.bulletstate = "fire"
        #Move the bullet to the just above the player
        x = gameComponent.player.xcor()
        y = gameComponent.player.ycor() + 10
        gameComponent.bullet.setposition(x, y)
        gameComponent.bullet.showturtle()

    #Create keyboard bindings
    turtle.onkey(fire_bullet, "space")