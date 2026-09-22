numero1 = int(input("\nInsira um número --> "))
numero2 = int(input("\nInsira um segundo número --> "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

perguntaOperacao = input(
    "\nQual operação deseja realizar?\n"
    "Escolha entre (+, -, *, /) --> "
).lower()

if perguntaOperacao == "+":
    print(soma)

elif perguntaOperacao == "-":
    print(subtracao)

elif perguntaOperacao == "*":
    print(multiplicacao)

elif perguntaOperacao == "/":
    if numero2 == 0:
        print("Divisor 0, impossível calcular!")
    else:
        divisao = numero1 / numero2
        print(divisao)

else:
    print("Operação inexistente")
