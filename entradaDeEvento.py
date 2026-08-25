idade = int(input("Insira sua idade: "))
possuiIngresso = input("Possui o ingresso? : ").lower()

if possuiIngresso == "sim" and idade >=18:
    print("Entrada liberada, aproveite!")
elif possuiIngresso == "nao" and idade >= 18:
    print("Acesso restrito, Adquira o Ingresso.")
else:
    print("Entrada Negada!, Acesso apenas para +18.")
