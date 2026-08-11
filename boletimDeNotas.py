aluno = input("Insira o nome do aluno(a): ")
curso = input("Insiro o curso: ")
semestre = int(input("Insira o semestre: "))
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
disciplina = input("Insira a disciplina: ")

media = (nota1 + nota2)/2

if media < 0 and media > 200:
    print("Valor inexistente.")
elif media >= 60:
    status = "Aprovado"
elif media >= 40:
    status = "Recuperação"
else:
    status = "Reprovado"




print("\n" + "-" * 40)
print("||        RELATÓRIO DO ALUNO        ||")
print("-" * 40)
print(f"|| Aluno: {aluno}")
print(f"|| Curso: {curso}")
print(f"|| Semestre: {semestre}")
print(f"|| Disciplina: {disciplina}")
print(f"|| Média: {media}")
print(f"|| Status: {status}")
print("-" * 40)
