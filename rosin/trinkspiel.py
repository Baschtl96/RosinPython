#!/usr/bin/env python3
import sys
import random


print("Willkommen zum Daddy Franky Trinkspiel")
print("Als erstes machen wir uns mit den Regeln vertraut:")

regeln = open('conf/regeln').read()
print(regeln)

print("Als erstes wird entschieden, welche Folge geschaut wird")

while True:

    line = random.choice(open('conf/folgen').readlines())
    print("Die Folge lautet: ",line)
    folge = input("Gibt es diese Folge auf youtube? ")
    if folge.upper() in ["Y", "Yes"]:
        break
    elif folge.upper() in ["N", "No"]:
        print("")
        print("")
        print("Dann wird hier schon getrunken!")
        aufwaermen = random.choice(open('aufwaermen').readlines())
        print("Jeder trinkt: ", aufwaermen)


geschlossen = input("Dauerhaft geschlossen?")
if geschlossen.upper() in ["Y", "Yes"]:
    dauerhaft = random.choice(open('conf/aufwaermen').readlines())
    print("")
    print("")
    print("jeder Trinkt: ", dauerhaft)
elif geschlossen.upper() in ["N", "No"]:
    print("Der Laden hat mit Daddy Franky einen guten Job gemacht. Jeder bekommt einen Joker.")
    print("Mit diesem Joker kann man seine Bestrafung an jemand anderes weitergeben")
    print("")

anzahlSpieler = list()
spieler = input("Anzahl Spieler? ")
for i in range(int( spieler)):
    n = input("Name : ")
    anzahlSpieler.append(str(n))
print("Die Spieler sind: ",anzahlSpieler)

while True:
    answer = input("Gebe y/yes ein um die Anzahl der Schlücke zu bekommen. Bei n/no wird das Spiel beendet")
    if answer.upper() in ["Y", "Yes"]:
        for  x in enumerate(anzahlSpieler):
            line = random.choice(open('conf/trinken').readlines())
            print(x,":",line)

    elif answer.upper() in ["N", "No"]:
        break
