import turtle

up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            snake_part = turtle.Turtle()
            snake_part.penup()
            snake_part.shape("square")
            snake_part.color("white")
            snake_part.setx(i * -20)
            self.snake.append(snake_part)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            seg_x = self.snake[seg_num - 1].xcor()
            seg_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=seg_x, y=seg_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def reset_snake(self):
        for part in self.snake:
            part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def add_snake_part(self):
        last_snake_part_x = self.snake[len(self.snake) - 1].xcor()
        last_snake_part_y = self.snake[len(self.snake) - 1].ycor()
        snake_part = turtle.Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.setpos(x=last_snake_part_x, y=last_snake_part_y)
        self.snake.append(snake_part)
