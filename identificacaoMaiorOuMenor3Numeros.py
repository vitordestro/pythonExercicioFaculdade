numero1 = int(input("Insira um número --> "))
numero2 = int(input("Insira um segundo número --> "))
numero3 = int(input("Insira um terceiro número --> "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} > {numero2} E O {numero3}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} > {numero1} E O {numero3}")
else:
    print(f"{numero3} > {numero1} E O {numero2}")