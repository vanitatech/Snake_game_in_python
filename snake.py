from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
        self.listen_to_keys()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.all_snakes[-1].position())
        

    def move_snake(self):
        for snake in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[snake - 1].xcor()
            new_y = self.all_snakes[snake - 1].ycor()
            self.all_snakes[snake].goto(x=new_x, y=new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def listen_to_keys(self):
        screen = Screen()
        screen.listen()
        screen.onkey(lambda: self.control_snake("up"), "Up")
        screen.onkey(lambda: self.control_snake("down"), "Down")
        screen.onkey(lambda: self.control_snake("left"), "Left")
        screen.onkey(lambda: self.control_snake("right"), "Right")

    def control_snake(self, direction):
        if direction == "up" and self.head.heading() != DOWN:
            self.head.setheading(UP)
        elif direction == "down" and self.head.heading() != UP:
            self.head.setheading(DOWN)
        elif direction == "left" and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        elif direction == "right" and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.all_snakes:
            segment.goto(1000, 1000)  # Move the segment off-screen
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]




