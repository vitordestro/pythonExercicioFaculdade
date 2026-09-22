def opcao_pagamento(opcao):
    if opcao == 1:
        print("| Método de Cartão de Crédito SELECIONADO!       |")
        metodo_pagamento = "Crédito"

    elif opcao == 2:
        print("| Método de Cartão de Débito SELECIONADO!        |")
        metodo_pagamento = "Débito"

    elif opcao == 3:
        print("| Método PIX SELECIONADO!                         |")
        metodo_pagamento = "PIX"

    elif opcao == 4:
        print("| Método Boleto SELECIONADO!                      |")
        metodo_pagamento = "Boleto"

    else:
        print("| SELECIONE UMA OPÇÃO DE PAGAMENTO VÁLIDA.        |")
        metodo_pagamento = "Opção inválida"

    return metodo_pagamento


def inicio():
    print("==================================================")
    print("|    Olá, Seja Bem Vindo A Loja SABOR RESENHA!   |")
    print("==================================================")
    print("| [1] Cartão de Crédito                           |")
    print("| [2] Cartão de Débito                            |")
    print("| [3] PIX                                         |")
    print("| [4] Boleto                                      |")
    print("| Para prosseguir a compra                        |")
    print("| Selecione um método:                            |")

    opcao = int(input())

    metodo = opcao_pagamento(opcao)

    print(f"| Método selecionado: {metodo}                    |")
    print("==================================================")


inicio()
