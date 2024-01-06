saldo = 0;
extrato = ""
quantidade_saque = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_VALOR_SAQUE = 500

print("""
==========Menu========== 
      
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
      
========================
      """)

operacao = int(input())

while True:
    if operacao == 1:
        print("Deseja realizar um depósito de que valor?")
        deposito = float(input())

        if deposito > 0:
            saldo += deposito
            print("Depósito realizado!")
            extrato += f"Depósito realizado no valor de R$ {deposito:.2f}\n"

        else:
            print("Depósito não realizado: valor indisponível.")

    elif operacao == 2:
        print("Deseja realizar um saque de que valor?")
        saque = float(input())

        if saque > LIMITE_VALOR_SAQUE:
            print("Saque não realizado: valor maior que o limite de saque.")
        
        elif quantidade_saque > LIMITE_SAQUE_DIARIO:
            print("Saque não realizado: limite diário de saque atingido.")

        elif saque > saldo:
            print("Saque não realizado: saldo insuficiente.")

        else:
            saldo -= saque
            print("Saque realizado!")
            quantidade_saque += quantidade_saque + 1
            extrato += f"Saque realizado no valor de R$ {saque:.2f}\n"

    elif operacao == 3:
        print("=========Extrato=========")
        if extrato == "":
            print("Não foram realizadas movimentações.\n")
        else:
            print(extrato)
            
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=========================")

    elif operacao == 0:
        break

    else:
        print("Opção desconhecida, por favor digite novamente.")

    print("""
==========Menu========== 
        
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
        
========================
        """)

    operacao = int(input())