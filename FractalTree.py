import turtle



def DrawBranch(branchLen):

    if branchLen > 10:
        t.forward(branchLen)
        t.right(40)
        DrawBranch(branchLen-15)
        t.left(80)
        DrawBranch(branchLen-15)
        t.right(40)
        t.backward(branchLen)



s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.color("green")
t.speed(5000)

t.width(5)
t.left(90)

DrawBranch(100)
turtle.done()
