class RoundRobin:
  pessoas = [] #Fila de pessoas
  NumEscolhidoPessoas = 0
  quantum = 0 #Numero de contas pra pagar no caixa

  def __init__(self):
    print('>>>>> Round-Robin Caixa Eletrônico <<<<<')

    self.quantum = input('\nDigite o número máximo de contas a pagar no caixa (quantum): ')
    self.NumEscolhidoPessoas = input('\nDigite o número de pessoas na fila: ')

    self.contas()
    self.fila()

    print("\n\n >>>>> Fim <<<<< \n")

  def contas(self):
    pessoas = self.pessoas

    for i in range(1, int(self.NumEscolhidoPessoas) + 1):
      numero = input('\nDigite o numero de contas a pagar da pessoa ' + str(i) + ': ')
      pessoas.insert(i, numero)

  def fila(self):
    contadorFila = int(self.NumEscolhidoPessoas)
    frenteFila = 1

    while (contadorFila != 0):
      while (int(self.pessoas[frenteFila - 1]) <= 0): #Tira pessoas que não tem contas da primeira posição
        frenteFila += 1

        if frenteFila >= int(self.NumEscolhidoPessoas): #Faz a rotação
          frenteFila = 0

      if frenteFila != 0:
        pessoa = str(frenteFila)
      else: 
        pessoa = str(self.NumEscolhidoPessoas)

      print("\n\nA pessoa " + pessoa + " vai para o caixa com "+ str(self.pessoas[frenteFila - 1]) +" contas")
      print("\nPaga até " + str(self.quantum) + " contas")

      self.pessoas[frenteFila - 1] = int(self.pessoas[frenteFila - 1]) - int(self.quantum) #Pagamento de quantum contas

      if int(self.pessoas[frenteFila - 1]) <= 0:
        print("\nE sai da fila.\n")
        contadorFila -= 1
      else:
        print("\nE vai pro final da fila com "+ str(self.pessoas[frenteFila - 1]) +" contas restantes.\n")

      frenteFila += 1 #Atualiza primeira posição

      if frenteFila > int(self.NumEscolhidoPessoas): #Faz a rotação
        frenteFila = 0

      print("PAUSE")

RoundRobin()