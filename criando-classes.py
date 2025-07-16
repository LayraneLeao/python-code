# Criando a classe
class Jovens:
  def __init__(self, nome, idade, cidade):
    self.nome = nome
    self.idade = idade
    self.cidade = cidade

  def cidadeAtual(self):
    print(f"\n{self.nome} mora em {self.cidade}.")

  def anoDeNascimento(self):
    ano = 2025 - self.idade
    print(f"{self.nome} nasceu em {ano}.\n")

# Criando os objetos
joao = Jovens("João", 18, "São Paulo")

# Chamando os métodos
joao.cidadeAtual()
joao.anoDeNascimento()

# Input
nomeDoJovem = input("Digite seu nome: ")
idadeDoJovem = int(input("Digite sua idade: "))
cidadeDoJovem = input("Digite sua cidade: ")

segundoJovem = Jovens(nomeDoJovem, idadeDoJovem, cidadeDoJovem)
segundoJovem.cidadeAtual()
segundoJovem.anoDeNascimento()
