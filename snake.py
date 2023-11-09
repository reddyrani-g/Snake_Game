from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(-20,0), (-40,0)]


class Snake:
    def __init__(self):
        self.start = []
        self.create_snake()
        self.head = self.start[0]

    #Creating snake
    def create_snake(self):
        for position in POSITIONS:
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.start.append(t)

    #Increasing size of snake when food is consumed
    def inc_size(self):
        last = len(self.start)-1
        t = Turtle("square")
        t.color("white")
        t.penup()
        x = self.start[last].xcor() - 20
        y = 0
        t.goto(x,y)
        self.start.append(t)
    
    #Moving Snake
    def move(self):
        for i in range(len(self.start)-1,0,-1):
            x = self.start[i-1].xcor()
            y = self.start[i-1].ycor()
            self.start[i].goto(x,y)
        self.head.forward(MOVE_DISTANCE)
        
    #Key Functions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    


        
    
        













