import time, tkinter as tk


def position_window(root, width, height):
    x = root.winfo_screenwidth() - width
    y = root.winfo_screenheight() - height
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))



# Properties
prop_stayontop =    True
prop_borderless =   True
prop_anchor =       "NE"

root = tk.Tk()

width =  250
height = 100
position_window(root, width, height)


but = tk.Button(root, text="Lol")
but.pack()

if (prop_stayontop):
    root.call('wm', 'attributes', '.', '-topmost', '1')

root.overrideredirect(True)
root.mainloop()
