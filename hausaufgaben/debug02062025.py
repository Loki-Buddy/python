#Debug 1
liste1 = [4, 5, 6]
liste2 = liste1
liste2.append(7)
print("Liste1:", liste1) # Hier waren wieder die Falschen Anführungszeichen
print("Liste2:", liste2) # Hier waren wieder die Falschen Anführungszeichen
#Frage: Warum enthält auch liste1 das Element 7? Wie kann man liste2 unabhängig kopieren?
#Antwort: Liste2 ist eine Referenz auf Liste1, daher ist Liste2 auch betroffen

#Debug 2
werte = [2, 4, 6, 8]
ergebnis = [x / 2 for x in werte if x < 5]
print(ergebnis)
#Frage: Welche Werte kommen in die neue Liste? Was bewirkt die Bedingung if x < 5?
#Antwort: Nur die Werte die kleine als 5 sind werden in die list ergebnis abgelegt. ergebnis = [1.0, 2.0]

#Debug 3
farben = ["rot", "grün", "blau"]
farben_neu = farben
farben = ["gelb", "lila"]
print(farben_neu)
#Frage: Was wird ausgegeben? Warum ist farben_neu hier nicht betroffen?
#Antwort: Weil farben in Zeile 20 NEU zugewiesen wird. 

#Debug 4
person = (["Max", 28, "Berlin"],)
person[0][2] = "Hamburg"
print(person)
#Frage: Warum funktioniert das nicht? Was müsste man tun, um einen ähnlichen Effekt zu erzielen?
#Antwort: Weil person ein Tupel ist. Man macht aus dem Inhalt des Tupels eine Liste macht. Das
#Komma am ende ist Pflicht damit Python sieht das es sich um ein Tupel handelt. Ohne Komma ist
#es eine Liste in Klammern und mehr nicht.

#Debug 5
daten = ("Ali", [100, 200])
daten[1][0] = 300
print(daten)
#Frage: Warum ist hier trotz eines Tupels eine Veränderung möglich?
#Antwort: Weil es sich um eine Liste innerhalb eines Tupels handelt.

#Debug 6
info = {"stadt": "Köln", "einwohner": 1000000}
print(info.get("fläche", "unbekannt"))
#Frage: Warum gibt es hier einen Fehler? Wie kann man den Zugriff sicherer machen?
#Antwort: Weil der Key "flaeche" nicht existiert. Sicherer Zugriff mittels get() und einem default Wert fals der Key nicht existiert.

#Debug 7
def schreibe(text):
    text = text.upper()
    return text
nachricht = schreibe("hallo")
print(nachricht)
#Frage: Warum ist die Ausgabe None? Wie müsste die Funktion geändert werden?
#Antwort: Weil die Funktion nichts zurueck gibt. return text

#Debug 8
def addiere(x, y):
    return x + y
summe = addiere(3, 4)
print(summe + 3)
#Frage: Warum kann man mit summe später nicht weiterrechnen?
#Antwort: Weil die Funktion nichts zurueck gibt. return x + y

#Debug 9
x = "global"
def test():
    x = "lokal"
    return x
print(test())
#Frage: Warum bleibt x nach dem Funktionsaufruf „global“?
#Antwort: Weil die Funktion nichts zurueck gibt. return x

#Debug 10
def info(stadt, name="Gast"):
    print(name, "aus", stadt)
info("Berlin")
#Frage: Warum funktioniert diese Definition nicht? Wie muss die Reihenfolge der Parameter angepasst werden?
#Antwort: Weil Parameter mit Standartwerten immer am Ende stehen muss und der Funktionsaufruf
#hatte zuviele Argumente