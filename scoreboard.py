from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()
      

    def increase_score(self):
        self.score += 1
        self.update_score()
   

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 16, "normal"))