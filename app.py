from fileinput import filename
import tkinter as tk
from tkinter import Tk, filedialog, Text
import os

from numpy import pad

root = tk.Tk()
root.title("Python App Cas")
root.iconbitmap("appicon.ico")
apps = []

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()


    filename= filedialog.askopenfilename(initialdir="/", title="Kies bestand",
    filetypes=(("Executables", ".exe"), ("Alle bestanden", "*.*"))) 
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps ():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=500, width=500, bg="#A779E0")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Kies bestand", padx=10, pady=5, fg="white", bg="#A779E0", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Open app", padx=10, pady=5, fg="white", bg="#A779E0", command=runApps)

runApps.pack()

root.mainloop()