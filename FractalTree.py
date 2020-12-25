from tkinter import *
import math

canvas = Canvas(width=1400, height=800, bg='black')
canvas.pack(expand=YES, fill=BOTH)


#canvas.create_line(XStart, YStart, XEnd, YEnd, width, fill)

def DrawBranch(startX, startY, angle, length, width):
    #print(str(startX) + "  " + str(startY) + "    " + str(width))
    angleRads = angle * math.pi / 180
    endX = startX + length * math.cos(angleRads)
    endY = startY + length * math.sin(angleRads)


    if (length > 5):
        canvas.create_line(startX, startY, endX, endY, width=width, fill='green')
        DrawBranch(endX,endY, angle+5,length*0.8,width*0.85)
        endX = startX + width * math.cos(angleRads)
        endY = startY + width * math.sin(angleRads)
        DrawBranch(endX,endY, 90-angle+5,length*0.8,width*0.85)




#Draw main trunk
canvas.create_line(500, 480, 500, 450, width=10, fill='green')
#Recusion Start
DrawBranch(500,450,270,100,10)

mainloop()
