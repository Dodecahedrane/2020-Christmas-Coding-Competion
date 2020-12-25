from tkinter import *

canvas = Canvas(width=1000, height=500, bg='black')
canvas.pack(expand=YES, fill=BOTH)

#canvas.create_line(XStart, YStart, XEnd, YEnd, width, fill)

def DrawBranch(start,angle,length, width):

    
    if (width > 0):
        canvas.create_line(500, 480, 500, 450, width, fill='green')





#Draw main trunk
canvas.create_line(500, 480, 500, 450, width=10, fill='green')
#Initial Params
DrawBranch():

mainloop()
