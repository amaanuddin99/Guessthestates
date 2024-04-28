from turtle import Turtle,Screen
class estate(Turtle):
    def __init__(self,state,x,y):
        super().__init__()
        self.state=state
        self.x=x
        self.y=y
        self.penup()
        self.hideturtle()
        self.goto(self.x,self.y)
        self.write(self.state,align="center",font=("Arial",10,"normal"))
