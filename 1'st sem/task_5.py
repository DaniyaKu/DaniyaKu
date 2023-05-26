import turtle
hope = turtle.Turtle()
hope.speed(500)
hope.color('blue')
size = 1618//2 - 179
hope.penup()
hope.goto(size//2 - 257,-size + 300)
hope.pendown()
def belief(size):
    if size <= 0.1:
        return
    hope.circle(size//1.618,-90)
    size //= 1.618
    belief(size)
belief(size)
turtle.done()
