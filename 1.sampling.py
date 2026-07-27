""" sampling.py
Manual sampling.  """

import tkinter as tk
import matplotlib.pyplot as plt

width = 919
height = 606

# Lists of coordinates
Lx = []
Ly = []

# Window
window = tk.Tk()
window.geometry('2000x800')
canvas = tk.Canvas(window, width=width, height=height, bg='white')

# Image
image = tk.PhotoImage(file='carte_france.png')
canvas.create_image(width//2, height//2, image=image)
canvas.create_text(width-80, 30, text='Sample size : ' + str(len(Lx)))
canvas.pack(expand=False, padx=3, pady=3)

def action_click(event):
    """
    Button left click
    """
    global Lx, Ly
    canvas.focus_set()
    x = event.x
    y = height-event.y
    canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill='red')
    canvas.pack(expand=YES, padx=3, pady=3)
    Lx.append(x)
    Ly.append(y)
    canvas.create_text(width-80, 30, text='Sample size : '+str(len(Lx)))

def plot_curve():
    """
    Button Plot curve.
    """
    plt.plot(Lx, Ly)
    plt.show()

def display_lists():
    """
    Button display lists.
    """
    print(str(len(Lx)), 'points')
    print(Lx)
    print(Ly)

canvas.bind('<Button-1>', action_click)

button_plot_curve = tk.Button(window, text='Plot curve', width=15, command=plot_curve)
button_plot_curve.pack(side=BOTTOM, pady = 10)

button_display_lists = tk.Button(window, text='Display lists', width=15, command=display_lists)
button_display_lists.pack(side=BOTTOM, pady = 10)

window.mainloop()
