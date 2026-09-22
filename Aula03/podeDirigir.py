nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
cnh = input("Possui cnh? (sim/nao): ").lower()

if idade >= 18 and cnh == "sim":
    print(f"{nome}, você pode dirigir")
elif idade >= 18 and cnh == "nao":
    print(f"{nome}, você não pode dirigir.")
elif idade < 18:
    print(f"{nome}, você ainda não pode dirigir.")
