from tkinter import *

canvas = Canvas(width=920, height=480, bg='black')
canvas.pack(expand=YES, fill=BOTH)

# (XStart, YStart, XEnd, YEnd)
canvas.create_line(100, 10,200, 10, width=10, fill='green')


mainloop()
