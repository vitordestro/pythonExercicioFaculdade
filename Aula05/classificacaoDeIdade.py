print("Verificador de Idade\n")

idade = int(input("Insira sua idade: "))

if idade >= 4 and idade <= 13:
    print("Sua classificação de idade é CRIANÇA")
elif idade >=14 and idade <= 20:
    print("Sua classificação de idade é ADOLESCENTE")
else:
    print("Sua classificação de idade é ADULTO")