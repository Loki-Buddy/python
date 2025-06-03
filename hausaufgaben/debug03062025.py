#Debug 1
def begrüßung(name):
    print("Hallo", name)
begrüßung("Loki")
#Frage: Warum funktioniert dieser Funktionsaufruf nicht?
#Antwort: Weil die Funktion eine Argument erwartet. 
#In Zeile 3 fehlt ein Lehrzeichen in dem String und
#das Komma nach dem String um die Varable name mit anzuhängen.

#Debug 2
def addiere(x, z, y=0):
    return x + y + z
#Frage: Warum akzeptiert Python diese Funktionsdefinition nicht?
#Antwort: Weil defaultwerte immer am Ende stehen müssen

#Debug 3
x = "global"
def test():
    global x
    x = "lokal"
test()
print(x)
#Frage: Warum bleibt x beim Wert “global”? Wie könnte man x innerhalb der Funktion global verändern?
#Antwort: In dem wir innerhalb der Funktion die global Varaible x explizit mit global deklarieren.

#Debug 4
def rechne(a, b):
    try:
        return a / b
    except ZeroDivisionError: #Um die "durch-0-division" aufzufangen
        print("Es kann nicht durch 0 dividiert werden.")
        return None
    except ArithmeticError: #Um alle anderen mathematischen Fehler aufzufangen
        print("Mathe 6! Setzen!")
        return None
print(rechne(5, 0))
#Frage: Warum wird nichts zurückgegeben? Wie könnte man das verbessern?
#Antwort: In erster Linie nicht durch 0 Teilen.
#Aber in zweiter Linie würde ich die Exceptions verfeinern und None zurückgeben

#Debug 5
def teile(x, y):
    if y == 0:
        #raise ZeroDivisionError("Eine Division durch 0 ist nicht möglich.")
        return x / y
try:    
    teile(4, 0)
except ZeroDivisionError as e:
    print("Eine Division durch 0 ist nicht möglich.", e)
except Exception as e:
    print("Ein unerwarteter Fehler ist aufgetreten!")
#Frage: Ist die Fehlerbehandlung hier sinnvoll? Was fehlt in der Fehlermeldung?
#Antwort: Ich würde den raise raus lassen und es stattdessen von dem try-Block unten behandeln lassen.
#Die Fehlermeldung könnte etwas mehr Kontext vertragen.

#Debug 6
def mache_etwas():
    try:
        x = int("abc")
    except ValueError:
        print("Casting von Buchstaben nach Integer ist nicht möglich.")
    finally:
        print("Fertig")
mache_etwas()
#Frage: Was passiert hier und warum wird kein Fehler angezeigt?
#Antwort: Weil es keinen except-Block gibt der den Fehler behandeln könnte
#finally wird immer ausgeführt egal ob ein Fehler kommt oder nicht.

#Debug 7
def berechne():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Fehler")
    finally:
        return "Fertig"
print(berechne())
#Frage: Warum wird “Fertig” ausgegeben und nicht “Fehler”? Was ist der Einfluss von finally?
#Antwort: Es wird beides ausgegeben. Der print() in Zeile 74 wird ausgegeben weil der Fehler abgefangen wird
#Der finally-Block wird IMMER ausgeführt. Egal ob es einen Fehler gab oder nicht. Hier wird ein String zurückgeben.
#Dieser wird ausgegeben weil die Funktion in einem print() aufgerufen wird.

#Debug 8
def konvertiere(zahl):
    try:
        return int(zahl)
    except ValueError:
        print("Ungültige Eingabe")
        return 0
x = konvertiere("abc")
print(x + 1)
#Frage: Warum gibt es einen neuen Fehler, obwohl der erste abgefangen wurde?
#Antwort: In Zeile 90 wird versucht mit der Rückgabe der Funktion zu rechnen.
#Ein Zwischenschritt vor dem return könnte diesen Fehler beheben. Ein alternativer return nach der Fehlerbehahndlung würde sinn machen.