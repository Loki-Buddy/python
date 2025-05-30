#Strings erstellen
text1 = 'Hallo'
text2 = "Welt"


#Index, Slicing, immutable, Maskierung
#Index
wort = "Python"
print(wort[0])   # 'P'
print(wort[-1])  # 'n' (letztes Zeichen)

#Slicing
wort = "Python"
print(wort[1:4])   # 'yth'
print(wort[:2])    # 'Py'
print(wort[2:])    # 'thon'

#Immutable
wort = "Hallo"
#wort[0] = "J"  #Fehler! Strings sind unveränderlich
neues_wort = "J" + wort[1:]  # 'Jallo'

#Maskierung
text = "Zeile 1\nZeile 2"   # \n = Zeilenumbruch
pfad = "C:\\Users\\Name"    # \\ = Backslash im Text

text = "Das ist 'Python'"
text2 = 'Er sagte: "Hallo!"'

#Escape für gleiche Anführungszeichen:
text = 'Das ist ein Apostroph: \''
text2 = "Er sagte: \"Hallo!\""

#Mehrzeilige Strings
mehrzeilig = """Das ist
ein mehrzeiliger
String."""


#Grundlegende Stringfunktionen und -methoden
len("Python")  # 6

"abc".upper()      # 'ABC'
"ABC".lower()      # 'abc'

"Hallo Welt".find("Welt")      # 6
"Hallo Welt".replace("Welt", "Python")  # 'Hallo Python'

"a,b,c".split(",")             # ['a', 'b', 'c']
",".join(['a', 'b', 'c'])      # 'a,b,c'

"  Text  ".strip()             # 'Text'
"  Text  ".lstrip()            # 'Text  ' left
"  Text  ".rstrip()            # '  Text' right
#Wir kennen das bisher als trim()!

"abc".startswith("a")          # True
"abc".endswith("c")            # True
"123".isdigit()                # True
