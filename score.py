from turtle import Turtle


class scoreboard(Turtle):

    #Scoreboard
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.write(f"Score :{self.score}", align="center", move=False, font=("Arial", 20 ,"normal"))
        self.hideturtle()

    #Increment Score  
    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score :{self.score}", align="center", move=False, font=("Arial", 20 ,"normal"))
      
    #GameOver
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!!!", align="center", move=False, font=("Arial", 20 ,"normal"))
   
    
    
