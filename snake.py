from turtle import Turtle, Screen
import time
MOVE_DISATANCE=20
STARTING_SNAKE=3
STARTING_POS=0
SNAKE_DIRECTION="right"

class Snake:
    def __init__(self):
        self.pos_x = STARTING_POS
        self.snake_body=[]
        self.create_snake()

    def create_snake(self):
        self.direction=SNAKE_DIRECTION
        position_x = 0
        for _ in range(STARTING_SNAKE):
            self.add_body((position_x, 0))
            position_x -= MOVE_DISATANCE
        self.head = self.snake_body[0]

    def add_body(self, position):
        snake_block = Turtle(shape="square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.goto(position)
        self.snake_body.append(snake_block)
    
    def move(self):
        prev_body = None
        for index, body in enumerate(self.snake_body):
            if index == 0: #First block
                prev_body = body.position()
                body.forward(MOVE_DISATANCE)
            else:
                current_position = body.position()
                body.goto(prev_body)
                prev_body = current_position
    
    def extend(self):
        self.add_body(self.snake_body[-1].position())
    
    def snake_set_heading(self, direction):
        if direction == "right" and self.direction != "left":
            self.snake_body[0].setheading(0)
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.snake_body[0].setheading(180)
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.snake_body[0].setheading(90)
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.snake_body[0].setheading(270)
            self.direction = "down"

    def left(self):
        self.snake_set_heading("left")

    def right(self):
        self.snake_set_heading("right")

    def up(self):
        self.snake_set_heading("up")

    def down(self):
        self.snake_set_heading("down")