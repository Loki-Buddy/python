print("Welche dieser Variablennamen ist in Python nicht erlaubt?\n\n\tA) my_var\n\tB) _var\n\tC) 2var\n\tD) var_2\n")

while True:
    user_input = input("Antwort: ").lower()
    if user_input.lower() not in {"a", "b", "c", "d"}:
        print("Bitte gib nur A, B, C oder D ein!")
        continue
    if user_input.lower() == "c":
        print("Richtig! Variablennamen dürfen nicht mit einer Ziffer beginnen.")
        break
    else:
        print("Falsch! Überleg noch mal!")