from turtle import Turtle
STARTING_SCORE=0
SCORE_FONT=("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score = STARTING_SCORE
        self.add_score()
    
    def add_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=SCORE_FONT)