print("CLASSIFICAÇÃO DO TRIÂNGULO\n")

lado1 = float(input("Insira o valor do primeiro lado -> "))
lado2 = float(input("Insira o valor do segundo lado -> "))
lado3 = float(input("Insira o valor do terceiro lado -> "))

if lado1 == lado2 == lado3:
    print("\nTriângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("\nTriângulo Isósceles")
else:
    print("\nTriângulo Escaleno")
