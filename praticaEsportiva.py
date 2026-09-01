idade = int(input("Insira sua idade: "))
autorizacao = input("Possui Autorização?: ").lower()


if idade >=12 and idade <= 18 and autorizacao == "sim":
    print("Acesso para prátia de esporte liberada!")
elif idade >=12 and idade <= 18 and autorizacao == "nao":
    print("Precisa de Autorização para acesso!")
else:
    print("Idade e Autorização inacessíveis")
