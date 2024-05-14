import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Blue')

# feet
t.goto(-100, -150)
rectangle(50, 20, 'AquaMarine')

t.goto(-30, -150)
rectangle(50, 20, 'AquaMarine')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'lemon chiffon')

t.goto(-55, -50)
rectangle(-15, 100, 'lemon chiffon')

# body
t.goto(-90, 100)
rectangle(100, 150, 'deep pink')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'misty rose')

t.goto(-150, 110)
rectangle(15, 40, 'misty rose')

t.goto(10, 70)
rectangle(60, 15, 'misty rose')

t.goto(55, 110)
rectangle(15, 40, 'misty rose')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'light blue')

# head
t.goto(-85, 170)
rectangle(80, 50, 'peach puff')

# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')

t.goto(-55, 155)
rectangle(5, 5, 'black')

t.goto(-40, 155)
rectangle(5, 5, 'black')

# mouth
t.goto(-65, 135)
rectangle(40, 5, 'black')

t.hideturtle()
t.done()
