nome = input("Insira seu nome: ")
idade = float(input("Insira sua idade: "))
tituloEleitor = input("Possui seu título? ").lower()

if idade >= 16 and tituloEleitor == "sim":
    print(f"{nome}, você pode votar")
elif idade < 16:
    print(f"{nome}, você não pode dirigir")
elif idade >= 16 and tituloEleitor == "nao":
    print(f"{nome}, você precisa tirar seu titulo de eleitor para votar")