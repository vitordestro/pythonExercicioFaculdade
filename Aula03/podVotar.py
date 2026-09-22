nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
titulo = input("Você possui título de eleitor? (sim/nao): ")

if idade >= 18 and titulo == "sim":
    print(f"{nome}, você pode votar.")
elif idade >= 18 and titulo == "nao":
    print(f"{nome}, você precisa tirar o título de eleitor.")
elif idade < 16:
    print(f"{nome}, você não pode votar.")
else:
    print(f"{nome}, você ainda não pode votar.")
