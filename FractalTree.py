from tkinter import *

canvas = Canvas(width=1000, height=500, bg='black')
canvas.pack(expand=YES, fill=BOTH)




#def DrawBranch():



#Draw main trunk
# (XStart, YStart, XEnd, YEnd)
canvas.create_line(500, 480, 500, 450, width=10, fill='green')
#Initial Params
#DrawBranch():

mainloop()
