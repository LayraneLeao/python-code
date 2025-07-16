class Calculadora:
  def __init__(self, numero01, numero02):
    self.primeiroNumero = numero01
    self.segundoNumero = numero02

  def soma(self):
    soma = self.primeiroNumero + self.segundoNumero
    print(f"A soma de {self.primeiroNumero} + {self.segundoNumero} = {soma}")

  def subtracao(self):
    if(self.primeiroNumero > self.segundoNumero):
      subtracao = self.primeiroNumero - self.segundoNumero
      print(f"A subtração de {self.primeiroNumero} - {self.segundoNumero} = {subtracao}")
    else:
      subtracao = self.segundoNumero - self.primeiroNumero
      print(f"A subtração de {self.segundoNumero} - {self.primeiroNumero} = {subtracao}")
    
  def multiplicacao(self):
    multiplicacao = self.primeiroNumero * self.segundoNumero
    print(f"A multiplicação de {self.primeiroNumero} * {self.segundoNumero} = {multiplicacao}")

  def divisao(self):
    divisao = self.primeiroNumero / self.segundoNumero
    print(f"A divisão de {self.primeiroNumero} / {self.segundoNumero} = {divisao}")

  def porcentagem(self):
    percentual = (self.primeiroNumero * self.segundoNumero) / 100
    print(f"A porcentagem de {self.primeiroNumero}% de {self.segundoNumero} = {percentual}")


operacao = int(input("""Escolha a operação desejada: 
  | 1 - Soma                                        |
  | 2 - Subtração                                   |
  | 3 - Multiplicação                               |
  | 4 - Divisão                                     |
  | 5 - Porcentagem (do primeiro número informado)  |
"""))

if (operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4 or operacao == 5):
  numero01 = int(input("\nInforme um número: "))
  numero02 = int(input("Informe outro número: "))
  calculo = Calculadora(numero01, numero02)

  if operacao == 1:
    calculo.soma()
  elif operacao == 2:
    calculo.subtracao()
  elif operacao == 3:
    calculo.multiplicacao()
  elif operacao == 4:
    calculo.divisao()
  elif operacao == 5:
    calculo.porcentagem()
    
else:
  print("Você não digitou uma operação válida!")
