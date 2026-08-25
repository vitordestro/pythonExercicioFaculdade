email = str(input("Insira um email --> "))

if "@" in email:
    print("Email cadsatrado!\n")
else:
    print("Insira um email válido!")

    
senhaUsuario = input("Insira um senha --> ")
confirmarSenha = input("Insira a senha novamente --> ")

if senhaUsuario == confirmarSenha:
    print(f"Usuário cadastrado com sucesso!\ne-mail={email}\nsenha:{senhaUsuario}")
else:
    print(f"Erro ao cadastrar o usuário. 404")






