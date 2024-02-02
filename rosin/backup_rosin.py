from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import sys
import random
import json
import webbrowser


anzahlSpieler = list()

#gui functions

def regeln():
    new = Tk()
    new.title("rules")
    file = open('conf/regeln', mode='r')
    contentOfRules = file.read()
    Label(new, text=contentOfRules).pack()

def spielername():
    #anzahlSpieler = list()
    for i in range(int( players)):
        spieler = simpledialog.askstring("Mitspieler","Name?",
            parent=window,)
        anzahlSpieler.append(str(spieler))
    print(anzahlSpieler)
    with open("conf/spielernamen", "a") as f:
        print(anzahlSpieler, file=f)
    return anzahlSpieler

def rollen():
    #line = random.choice(open('conf/trinken').readlines())
    counter = 1
    while counter <= players:
        print (counter)
        line = random.choice(open('conf/trinken').readlines())
        messagebox.showinfo(title="folge", message=[anzahlSpieler[players-counter], line])
        counter = counter + 1

def folge():
    #messagebox youtube
    new = random.choice(open('conf/folgen').readlines())
    global nameDerFolge 
    nameDerFolge = str(new)
    webbrowser.open('https://www.youtube.com/results?search_query='+nameDerFolge)
    messagebox.showinfo(title="folge", message=nameDerFolge)
    if(messagebox.askyesno(title="youtube?", message="Found this episode on youtube?")):
        print()
    else:
        rollen()
        folge()
    return nameDerFolge

def geschlossen():
    print (nameDerFolge)
    webbrowser.open('https://www.google.com/search?q={}'.format(nameDerFolge))
    if(messagebox.askyesno(title="Dauerhaft geschlossen?", message="Dauerhaft geschlossen?")):
        rollen()

#gui

window = Tk()
window.title("Rosin drinking game")
window.maxsize(900,600)

#left frame for layout
left_frame = Frame(window, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)
Label(left_frame, text="Rosin drinking game").grid(row=0, column=0, padx=5, pady=5)

#right frame for layout
right_frame = Frame(window, width=650, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=5)

#toolbar
tool_bar = Frame(left_frame, width=100, height=105)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

#menubar
menubar = Menu(window)
window.config(menu=menubar)

#menu in menubar
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="rules", command=regeln)

#rosin picture
image = PhotoImage(file="Rosin.png")
original_image = image.subsample(3,3)
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)


#question box
players = simpledialog.askinteger("Mitspieler","Wie viele Spieler?",
    parent=window,)
if players is None:
    window.destroy()
elif players  == 0:
    window.destroy()
elif players is not None:
    spielername()
    #print(players)

##buttons

schluecke = Button(right_frame, text="roll sips", command=rollen, height = 2, width = 30)
schluecke.grid(padx=30, pady=10)

task = Button(right_frame, text="special task", height = 2, width = 30)
task.grid(padx=30, pady=10)

question = Button(right_frame, text="special question", height = 2, width = 30)
question.grid(padx=30, pady=10)

addStatement = Button(right_frame, text="add statement", height = 2, width = 30)
addStatement.grid(padx=30, pady=10)


#messagebox youtube
#webbrowser.open('https://www.youtube.com/results?search_query='+nameDerFolge)
folge()

#messagebox geschlossen
geschlossen()

##question box
#players = simpledialog.askinteger("Mitspieler","Wie viele Spieler?",
#    parent=window,)
#if players is None:
#    window.destroy()
#elif players  == 0:
#    window.destroy()
#elif players is not None:
#    spielername()
    #print(players)


window.mainloop()
