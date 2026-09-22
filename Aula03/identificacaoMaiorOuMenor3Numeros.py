numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o maior número.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} é o maior número.")
elif numero3 > numero1 and numero3 > numero2:
    print(f"{numero3} é o maior número.")
else:
    print("Existem números iguais entre os maiores.")
