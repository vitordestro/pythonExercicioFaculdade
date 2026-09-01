print("-" * 45)
print("| " + "AUMENTO DE 15% NO SALÁRIO DE FUNCIONÁRIOS |  \n|           COM ATÉ R$2000.00               |")
print("-" * 45)

salario = float(input("Insira o valor do seu sálario mensal: "))

aumento = 0.15
salarioComAumento = salario + (salario * aumento)

if salario <= 2000.00:
    print(f"\nAumento Efetivado! --> Seu Salário atual é de: R${salarioComAumento:.2f} ")
else:
    print("Aumento Não Disponível.")
