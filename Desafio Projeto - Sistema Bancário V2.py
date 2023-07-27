menu = ''''
------ Escolha a operação desejada ------

[d] = Depositar
[s] = Sacar
[e] = Extrato
[c] = Abrir Conta
[x] = Sair 

'''

saldo = 0 
limite = 500
extrato = " "
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

def cadastrar_usuario():
     usuario = str(input("Digite seu nome completo: "))
     data = str(input("Digite sua data de nascimento: "))
     cpf = int(input("Digite seu cpf - não use pontos e traços: "))
     logradouro=str(input("Informe seu Logradouro: "))
     numero = int(input("Qual é o Número: "))
     cidade_estado = str(input("Informe a cidade/UF: "))
     lista = []
     lista.extend((usuario, data, cpf, logradouro, numero, cidade_estado))

     if cpf in lista:
          print("Cpf já cadastrado.")
     else:
          lista.append(cpf)     

     def abrir_conta():    
          AGENCIA = "0001" 
          from random import randint
          contas = []
          contas.append(1)
          for i in range(4):
               conta = randint(2,9)
               while conta in contas:
                    conta = randint(2,9)
               contas.append(conta)
          conta_corrente = []
          conta_corrente.extend((AGENCIA, contas, usuario))

     print("Conta Criada com sucesso.")
     
def saque(*, valor):
            global saldo, limite, numero_de_saques, extrato
        
            if valor > saldo:
                 print("Saldo Insuficiente.")
            if valor > limite:
                 print("Limite de saque excedido.")
            if numero_de_saques >= LIMITE_DE_SAQUES:
                 print("Limite de saques dário excedido.")
            elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R$ {valor:.2f}\n"
                 numero_de_saques += 1      
            else:
                 print("Opção Inválida")     

def deposito(valor):
      global saldo
      global extrato
      if valor > 0:
            saldo += valor
            extrato +=f"Depósito: R$ {valor:.2f}\n"
      else:
        print("Operação inválida, não é possível depositar valores negativos. Nesse caso você deve fazer um saque!") 
        
      
def historico():
     global saldo
     global extrato
     print("\n---------- Extrato ----------")
     print("Não foram feitas movimentações" if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("\n-------------------------------")
     
                      

while True:
    

    opcao = input(menu)


    if opcao == "d":
        deposito(valor=float(input("Digite o valor desejado para depósito:" )))

    elif opcao == "s":
            saque(valor=float(input("Digite o valor a ser sacado: ")))
                                  
    elif opcao == "e":
         historico()

    if opcao == "c":
         cadastrar_usuario()

    elif opcao == "x":
        print("Obrigado por escolher nosso banco")
        break

    else:
        print("Opção invalida, tente outra vez!")


