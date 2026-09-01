numero1 = int(input("\nInsira um número -->  "))
numero2 = int(input("\nInsira um segundo número -->  "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

perguntaOperacao = str(input("\nQual operação deseja realizar?\nescolha entre(+,-,*,/)  --> ").lower())

if perguntaOperacao == "+":
    print(soma)
elif perguntaOperacao == "-":
    subtracao
    print(subtracao)
elif perguntaOperacao == "multiplicação" or perguntaOperacao == "multiplicacao":
    print(multiplicacao)

elif perguntaOperacao == "/":
    if numero2 == 0:
        print("Divisor 0, impossível calcular!")
    else:
        divisao = numero1 / numero2
        print(divisao)
else:
    print("Operação Inexistente")