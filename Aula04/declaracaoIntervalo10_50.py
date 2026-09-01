numeroIntervalo = int(input("Insira um número entre 10 a 50 : "))

if numeroIntervalo >= 10 and numeroIntervalo <= 50:
    print(f"O Número é {numeroIntervalo} ACEITO!\n10 <- {numeroIntervalo} -> 50")
else:
    print("Número não aceite pelo Intervalo!")