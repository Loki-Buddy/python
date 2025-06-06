## Aufgabe
""" 1. Lies vom Benutzer eine Zeile mit Ganzzahlen, getrennt durch Leerzeichen, ein  
   (Beispiel: `3 3 1 4 3 2 1`).
2. Speichere die Zahlen in einer **Liste**.
3. Erstelle anschließend  
   * eine **Menge** (`set`) mit allen einzigartigen Zahlen und  
   * ein **Dictionary**, das jeder Zahl ihre Häufigkeit (Count) zuordnet.
4. Gib aus  
   * die Gesamtzahl der eingegebenen Werte,  
   * die Menge der eindeutigen Zahlen,  
   * die Häufigkeit jeder Zahl, aufsteigend nach der Zahl sortiert. """
   
from collections import Counter

## Loesung
zahlen = []
while True:
    user_input = input("Gib eine Reihe von Zahlen, mit Leerzeichen als Trennung: ")
    try:
        zahlen = [int(zahl) for zahl in user_input.split()]
        break
    except ValueError:
        print("Bitte gib nur Zahlen ein")
#3.
unique_num = set(zahlen)
freq = dict(Counter(zahlen))
print(len(zahlen))
print(unique_num)
print(sorted(freq.items()))

""" for n in sorted(freq):            
    print(f"{n}: {freq[n]}×") """