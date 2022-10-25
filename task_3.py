import turtle as tl

def draw_fractal(scale):
    if scale >= 5:
        draw_fractal(scale / 2.0)
        tl.left(90)
        draw_fractal(scale / 2.0)
        tl.left(90)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.forward(scale)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.left(90)
        draw_fractal(scale / 2.0)
        tl.left(90)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.forward(scale)
        draw_fractal(scale / 2.0)
        tl.right(90)
        draw_fractal(scale / 2.0)
        tl.left(90)
        draw_fractal(scale / 2.0)
        tl.left(90)
    else:
        tl.left(90)

scale = 250
tl.pensize(2)
tl.penup()
tl.goto(-scale, -scale/4)
tl.pendown()

draw_fractal(scale)
tl.done()
