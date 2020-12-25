from tkinter import *
import math

canvas = Canvas(width=1000, height=500, bg='black')
canvas.pack(expand=YES, fill=BOTH)


#canvas.create_line(XStart, YStart, XEnd, YEnd, width, fill)

def DrawBranch(startX, startY, angle, length, width):
    #print(str(startX) + "  " + str(startY) + "    " + str(width))
    angleRads = angle * math.pi / 180
    endX = startX + length * math.cos(angleRads)
    endY = startY + length * math.sin(angleRads)
    angle1 = angle
    angle2 = angle
    offset = 45

    if (length > 5):
        canvas.create_line(startX, startY, endX, endY, width=width, fill='green')

        DrawBranch(endX,endY, angle1-offset, length*0.6, width*0.75)

        endX = startX + length * math.cos(angleRads)
        endY = startY + length * math.sin(angleRads)

        DrawBranch(endX,endY, angle2+offset, length*0.6, width*0.75)




#Draw main trunk
canvas.create_line(500, 480, 500, 450, width=10, fill='green')
#Recusion Start
DrawBranch(500,450,270,50,10)

mainloop()
