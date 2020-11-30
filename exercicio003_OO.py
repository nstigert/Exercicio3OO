class Funcionario:

    def __init__(self, nome, salario, totalAcrescimo, totalDesconto):
        self.nome = nome
        self.salario = salario
        self.totalAcrescimo = totalAcrescimo
        self.totalDesconto = totalDesconto

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSalario(self):
        return self.salario

    def setSalario(self, salario ):
        self.salario = salario
    
    def getTotalAcrescimo(self):
        return self.totalAcrescimo
    
    def setTotalAcrescimo(self, totalAcrescimo):
        self.totalAcrescimo = totalAcrescimo
    
    def getTotalDesconto(self):
        return self.totalDesconto

    def setTotalDesconto(self, totalDesconto):
        self.totalDesconto = totalDesconto
    
    def calcularSalarioLiquido(self):
        return (self.salario + self.totalAcrescimo - self.totalDesconto)


print

funcionario = Funcionario("Nathalia",5000, 550, 100)

print(funcionario.getNome())

funcionario.getSalario()
funcionario.getTotalAcrescimo()
funcionario.getTotalDesconto()