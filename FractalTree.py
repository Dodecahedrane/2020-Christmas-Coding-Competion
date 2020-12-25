import turtle
def DrawBranch(branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        angle = 60
        t.right(angle)
        DrawBranch(branchLen*0.5)
        t.left(angle * 2)
        DrawBranch(branchLen*0.5)
        t.right(angle)
        DrawBranch(branchLen*0.5)
        t.backward(branchLen)
s = turtle.Screen()
t = turtle.Turtle()
t.color("green")
t.speed(10000)
t.width(5)
t.left(90)
DrawBranch(200)
turtle.done()
