##Debug 1 :
a = [1, 2, 3]
b = list(a)
b[0] = 99
print("a =", a)
print("b =", b)
#Frage: Warum wird a[0] ebenfalls zu 99, obwohl wir nur b verändert haben?
#Antwort: a und b haben die gleiche Speicheradresse im Arbeitspeicher (*Pointer)
#Wie kann man das verhindern?
#Lösung: b = a.copy() oder b = a[:] oder b = list(a)

#Debug 2 :
farben = ["rot", "gruen", "blau"]
print(farben[2])
#Frage: Was passiert hier? Was wäre die korrekte Lösung?
#Antwort: Der Index der in Zeile 14 angesprochen wird existiert nicht
#Lösung: print(farben[2]) oder print(farben[-1])

#Debug 3:
zahlen = [1, 2, 3, 4]
doppelt = [x + x for x in zahlen if x % 2]
print(doppelt)
#Frage: Warum sind nur bestimmte Zahlen im Ergebnis?
#Was macht die Bedingung if x % 2 genau?
#Antwort: x+x wird nur bei den ungraden Zahlen angewand. if x % 2 das ergebnis kann nur 0 oder 1 sein.
#Erklärung: die 0 und die 1 werden in der Informatik auch als Wahrheitswerte verstanden. 0 = FALSCH (false); 1 = WAHR (true)

#Debug 4:
tupel = (1, 2, 3)
#tupel[1] = 5
print(tupel)
#Frage: Warum funktioniert das nicht?
#Antwort: Ein Tupel ist nicht veränderbar.

#Debug 5:
daten = ("Ali", [10, 20])
daten[1].append(30)
#daten[1].clear()
print(daten)
#Frage: Wie kann sich der Inhalt hier verändern, obwohl Tupel eigentlich unveränderlich sind?
#Antwort: Eine Liste innerhalb eines Tupels ist sehr wohl veränderbar.

#Debug 6:
farben = {"rot": "#FF0000", "gruen": "#00FF00", "blau": "#0000FF"}
for eintrag in farben.items():
    print(eintrag)
    
#Frage: Warum wird hier nur der Schlüssel ausgegeben?
#Wie müsste man den Code ändern, um rot = #FF0000 usw. zu sehen?
#Antwort:   Mittels einer normalen iteration über ein Dictionary werden nur die keys ausgeben
#           mit der Funktion .items() werden die Schlüssel mit ihren Werten ausgegeben