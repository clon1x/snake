from turtle import Turtle, Screen

snake = []


def setup_turtle():
    turtle = Turtle()
    turtle.shape('square')
    turtle.shapesize(0.5)
    turtle.penup()
    turtle.color('grey')
    return turtle


def setup_screen():
    screen = Screen()
    screen.listen()
    screen.delay(60)
    return screen


def draw_snake():
    for point in [(-10,0),(0,0),(10,0)]:
        jamie.setpos(point)
        snake.append(jamie.stamp())
    print(f'Initial state: {snake}')


def move_snake():
    jamie.forward(10)
    jamie.clearstamp(snake.pop(0))
    snake.append(jamie.stamp())
    screen.update()
    screen.ontimer(fun=move_snake(), t=120)


jamie = setup_turtle()
screen = setup_screen()
draw_snake()
move_snake()

screen.exitonclick()
