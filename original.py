class ContaCorrente:
 def __init__(self, nome,numero,saldo):
  self.nome=nome
  self.numero=numero
  self.saldo=saldo


 def deposito(self, c, account,quantia):
  for i in range(len(conta)):
   if conta[i].numero == account:
    conta[i].saldo += quantia
    return True


 def saque(self, c,account,quantia):
  for i in range(len(conta)):
   if conta[i].numero == account:
    if conta[i].saldo >= quantia:
     conta[i].saldo -= quantia
     return True
    else:
     return False

 def verSaldo(self,c,account):
  for i in range(len(conta)):
   if conta[i].numero == account:
    print('\nNumero da Conta: {}\nSaldo: {}\n'.format(conta[i].numero, conta[i].saldo))
  return True

def imprimeMenu():
 print('='*20)
 print('1 - Criar conta')
 print('2 - Deposito')
 print('3 - Saque')
 print('4 - Ver saldo')
 print('5 - Relatorio')
 print('6 - Sair')
 print('='*20)

def opcaoUm(conta):
 for i in range(1):
   n = input('\nNome do titular: ')
   nc = input('Numero da conta: ')
   #CONTA IGUAL,ATÉ SER UMA CONTA DIFERENTE
   for i in range(len(conta)):
    if nc == conta[i].numero:
     while nc == conta[i].numero:
      print('\nERROR!')
      print('Conta já existe!\n')
      nc = input('Numero da conta: ')
   s = float(input('Saldo inicial: '))
   op = ContaCorrente(n,nc,s)
   conta.append(op)
   print()

conta = list()
op = ContaCorrente(input('\nNome do titular: '), input('Numero da conta: '),float(input('Saldo inicial: ')))
conta.append(op)
print()

while True:
 imprimeMenu()
 opcao = int(input('Opção: '))

 #CRIAR CONTA (OK)
 if opcao == 1:
  opcaoUm(conta)


 #EFETUAR DEPOSITO (OK)
 elif opcao == 2:
  account = input('\nNumero da conta para depósito: ')
  quantia = float(input('Valor do depósito: '))

  if op.deposito(conta,account,quantia) == True:
   print('Deposito realizado com sucesso!\n')


 #REALIZAR SAQUE (OK)
 elif opcao == 3:
  account = input('\nNumero da conta para saque: ')
  quantia = float(input('Valor do saque: '))

  if op.saque(conta,account,quantia) == True:
   print('Saque realizado com sucesso!\n')
  else:
   print('Saldo insuficiente!\n')


 #VER SALDO (OK)
 elif opcao == 4:
  account = input('\nNumero da conta para ver saldo: ')
  op.verSaldo(conta,account)


 #VER RELATORIO (OK)
 elif opcao == 5:
  print()
  for i in range(len(conta)):
   print('Titular: {}\nConta: {}\nSaldo: {}'
    .format(conta[i].nome, conta[i].numero, conta[i].saldo))
   print()


 #SAIR DO PROGRAMA
 elif opcao == 6:
  print()
  break