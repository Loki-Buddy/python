def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)

print(fakultaet(5))  # Ausgabe: 120

def summe(n):
    if n == 0:
        return 0
    else:
        return n + summe(n - 1)

print(summe(4))  # Ausgabe: 10 (4+3+2+1+0)

def rueckwaerts(n):
    if n == 0:
        return
    print(n)
    rueckwaerts(n - 1)

rueckwaerts(5)
# Ausgabe:
# 5
# 4
# 3
# 2
# 1

'''
Ich habe mir die Recursion noch einmal Angeschaut.
Verstanden hatte ich es Schon vorher jedoch wollte ich es
nach langer Zeit mal wieder Syntaktisch üben.
Da mein Vorwissen aus C/C++ und Java herkommt, kann es nicht schaden
das ganze auch in python drauf zu haben.
'''