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
        self.high_score = 0
        self.add_score()
    
    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()