print( "=" * 50)
print("| Olá, Seja Bem Vindo A Loja da Barca do chipre!  |" )
print( "=" * 50)

pagaraAvista = input("Pagamento será a vista? ").lower()
valorCompra = float(input("Valor do Produto: "))
desconto = 0.1

if pagaraAvista == "sim":
    precoFinal = valorCompra - ( valorCompra * desconto)
    print(f"Parabéns! Você recebeu um desconto de 10% na sua compra\nValor da compra de {valorCompra:.2f} de--> R${precoFinal:.2f}")
elif pagaraAvista == "nao":
    print(f"Valor da Compra --> R${valorCompra:.2f}")
