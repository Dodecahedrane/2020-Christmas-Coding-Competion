import turtle



def DrawBranch(branchLen):

    if branchLen > 10:
        t.forward(branchLen)
        t.right(80)
        DrawBranch(branchLen-20)
        t.left(160)
        DrawBranch(branchLen-20)
        t.right(80)
        DrawBranch(branchLen-20)
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
