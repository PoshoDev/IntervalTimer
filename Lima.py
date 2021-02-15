import time, tkinter as tk

# Properties
prop_stayontop =    True
prop_borderless =   True

root = tk.Tk()

but = tk.Button(root, text="Lol")
but.pack()

if (prop_stayontop):
    root.call('wm', 'attributes', '.', '-topmost', '1')

root.mainloop()
