from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scoreboard

# Screen
s = Screen()
s.setup(width = 600, height = 600)
s.bgcolor('black')
s.title("Snake Game")
s.tracer(0)
 
#Objects Creation
snak = Snake()
food = Food()
sc = scoreboard()

s.listen()


s.onkey(snak.up,"Up")
s.onkey(snak.down,"Down")
s.onkey(snak.left,"Left")
s.onkey(snak.right,"Right")

game_on = True
        
while game_on:
    s.update()
    time.sleep(0.1)
    snak.move()

    #Detect collision with Food.
    if snak.head.distance(food) < 15:
        food.refresh()
        snak.inc_size()
        sc.inc_score()

    #Detect collision with Wall.
    if snak.head.xcor() >280 or snak.head.ycor() >280 or snak.head.xcor() < -280 or snak.head.ycor() < -280:
        game_on = False
        sc.gameover()

    #Detect Collision with own Tail.
    for segment in snak.start[1:]:
        if snak.head.distance(segment) < 10:
            game_on = False
            sc.gameover()
            

s.exitonclick()

