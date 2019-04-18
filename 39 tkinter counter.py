# introduction to Tkinter: create a button counter
import tkinter as tk
root=tk.Tk()
topFrame=tk.Frame(root)
topFrame.pack()

def click():
    counter.set(counter.get()+1)
counter=tk.IntVar()
counter.set(0)
frame=tk.Frame(root)
frame.pack()
button1=tk.Button(topFrame,text="Click", command=click)
button1.pack()
label=tk.Label(frame, textvariable=counter)
label.pack()
root.mainloop()
