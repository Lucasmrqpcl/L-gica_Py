login_valido =True
senha_valida = True
conta_bloqueada = True

if conta_bloqueada:
     print("Conta Bloqueada")
elif not login_valido:
     print("Login errado")
elif not senha_valida:
     print("Senha errada")
else:
     print("bem-vindo ao Sistema")