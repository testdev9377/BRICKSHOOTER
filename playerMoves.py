#Move the player left and right and defines the bullet
import turtle
import os
import gameComponent

def setTheMoves():
    

    def move_left():
        x = gameComponent.player.xcor()
        x -= gameComponent.playerspeed
        if x < -280:
            x = - 280
        gameComponent.player.setx(x)
        
    def move_right():
        x = gameComponent.player.xcor()
        x += gameComponent.playerspeed
        if x > 280:
            x = 280
        gameComponent.player.setx(x)
    
    #Create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")



