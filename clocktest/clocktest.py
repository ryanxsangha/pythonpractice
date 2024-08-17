from tkinter import *
from time import strftime

#adjust window for clock
myWindow = Tk()
myWindow.title('Ryan\'s Clock')

#clock function definition
def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

#formatting
clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'black',
                                foreground = 'dark green')
clock.pack(anchor = 'center')

#call time function
time()

#infinite tkinder main function loop
mainloop()