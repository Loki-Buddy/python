#Debug Aufgabe

#Aufgabe 1:
# Fehler: for ist ein Schlüsselwort und kann daher nicht als Name für eine Variable Verwendet werden
# Lösung: Variable umbenennen

zahl = 7
print(zahl)

#Aufgabe 2:
# Fehler: der print() in der Zeile unter der if-Anweisung muss eingerückt werden
# Lösung: print() Befehl einrücken

name = "Ada"
if name == "Ada":
    print("Hello,", name)

#Aufgabe 3:
# Fehler: Hier sollte eigentlich gerechnet werden, jedoch wurde mit der Brechnung und der Ausgabe, der String lediglich 3 mal ausgegeben
# Lösung: price als float zuweisen ODER mittels Type Casting
 
price  = 19.99
quantity = 3
total = price * quantity
print("Total:", total)

# ODER

price  = float("19.99")
quantity = 3
total = price * quantity
print("Total:", total)


#Recherche für die Auffrischung und/oder neu Erlerntes in python
# Ich habe mich mit Listen(Eindimensional) auseinander gesetzt

fruits = ["Apfel", "Banane", "Kirsche"]
zahlen = [1, 2, 3, 4, 5]

print(fruits[0])
print(zahlen[-1])

fruits.append("Orange")
fruits.insert(1, "Birne")

print(fruits)
fruits.remove(fruits[-1])
print(fruits)

print(fruits.pop())

for fruit in fruits:
    print(fruit)

print(zahlen)
alles_zum_quadrat = [x**2 for x in zahlen]
print(alles_zum_quadrat)
