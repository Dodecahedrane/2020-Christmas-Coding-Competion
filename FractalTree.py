from tkinter import *
import math

canvas = Canvas(width=1000, height=500, bg='black')
canvas.pack(expand=YES, fill=BOTH)


#canvas.create_line(XStart, YStart, XEnd, YEnd, width, fill)

def DrawBranch(startX, startY, angle, length, width):

    angleRads = angle * math.pi / 180
    endX = startX + width * math.cos(angleRads)
    endY = startY + width * math.sin(angleRads)


    if (width > 0):
        canvas.create_line(startX, startY, endX, endY, width=width, fill='green')
        DrawBranch(endX,endY, angle-5,length-1,width-0.25)




#Draw main trunk
canvas.create_line(500, 480, 500, 450, width=10, fill='green')
#Initial Params
DrawBranch(500,450,45,10,10)

mainloop()
