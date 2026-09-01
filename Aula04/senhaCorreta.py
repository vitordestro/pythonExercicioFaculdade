email = str(input("Insira um email --> "))

if "@" in email:
    print("Email cadsatrado!\n")
else:
    print("\nInsira um email válido!")

    
senhaUsuario = input("Insira um senha --> ")
confirmarSenha = input("\nInsira a senha novamente --> ")

if senhaUsuario == confirmarSenha:
    print(f"\nUsuário cadastrado com sucesso!\ne-mail: {email}\nsenha: {senhaUsuario}")
else:
    print(f"Erro ao cadastrar o usuário. 404")






