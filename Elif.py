usuario = True
senha = False

if usuario and not senha:
     print("Senha errada")
elif usuario and senha:
     print("Conta logada com sucesso")
else: print("Senha/usuario errado")
     