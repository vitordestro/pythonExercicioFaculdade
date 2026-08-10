nome = input("Insira o nome do Aluno: ")
disciplina = input("Insira a disciplina: ")
nota = int(input("Nota obtida: "))

if nota > 59 and nota <=100:
    print(f"O aluno {nome}, foi aprovado na disciplina {disciplina}.")
elif nota > 39 and nota <= 59:
    print(f"O aluno {nome}, está de recuperação na disciplina {disciplina}.")
else:
   print(f"O aluno {nome}, foi reprovado na disciplina {disciplina}.")
