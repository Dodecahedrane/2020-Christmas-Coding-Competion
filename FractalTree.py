from tkinter import *
import math

canvas = Canvas(width=1000, height=800, bg='black')
canvas.pack(expand=YES, fill=BOTH)


#canvas.create_line(XStart, YStart, XEnd, YEnd, width, fill)

def DrawBranch(startX, startY, angle, length, width):
    #print(str(startX) + "  " + str(startY) + "    " + str(width))
    angleRads = angle * math.pi / 180
    endX = startX + length * math.cos(angleRads)
    endY = startY + length * math.sin(angleRads)
    angle1, angle2 = angle, angle
    length1, length2 = length, length
    offset = -35

    if (length > 15):
        canvas.create_line(startX, startY, endX, endY, width=width, fill='green')

        DrawBranch(endX,endY, angle1+offset, length*0.5, width*0.75)

        endX = startX + length * math.cos(angleRads)
        endY = startY + length * math.sin(angleRads)

        DrawBranch(endX,endY, angle2-offset, length*0.5, width*0.75)

        endX = startX + length * math.cos(angleRads)
        endY = startY + length * math.sin(angleRads)

        DrawBranch(endX,endY, 270, length*0.8, width*0.75)


#Recusion Start
DrawBranch(500,475,270,75,10)
mainloop()
