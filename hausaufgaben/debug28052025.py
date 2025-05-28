#Debug 1
#Fehler: Falscher Typ
#Lösung: Entfernen der "" ODER Type Casting
zahl = 10                 #zahl = int("10")
ergebnis = zahl + 5
print(ergebnis)


#Debug 2
#Fehler: Einrückung vergessen
#Lösung: Tabstopp
x = 3
if x > 0:
    print("x ist positiv")


#Debug 3
#Fehler: Tabstop und Doppelpunkt nach der Anweisung
#Lösung: einen Doppelpunkt in Zeile 20 am ende UND Zeile 21 den Tabstop am Anfang
for i in range(5):
    print(i)


#Debug 4
#Fehler: Falscher Operator
#Lösung: == in Zeile 28
alter = 18
if alter == 18:
    print("Volljährig")


#Debug 5
#Antwort:   hier wird aus der 4 und der 2 auf Bitebene das Zweierkomplement gebildet
#           in dem die einzelen Bits mittels XOR verglichen werden
#100
#010
#---
#110
x = 4
y = 2
z = x ^ y
print("Ergebnis ist", z)


#Debug 6
#Fehler: Einrückung wurde nicht eingehalten
#Lösung: Tabstopps einfügen
x = 10
if x > 0:
    if x < 5:
        print("klein")
    else:
        print("gross")


#Debug 7
#Fehler: Endlosschleife
#Lösung: Zu einem bestimmten Zeitpunkt mit break aus der Schleife springen.
#Beispiel: Zeitpunkt mittels Counter festlegen
counter = 0
while True:
    if counter == 3:
        break
    print("Hallo")
    counter += 1

#Debug 8
#Fehler: Mit Srings lässt sich nicht rechnen.
#Lösung: Mittels Type Casting den input Konvertieren
eingabe = input("Gib eine Zahl ein: ")
if int(eingabe) > 10:
    print("größer als 10")