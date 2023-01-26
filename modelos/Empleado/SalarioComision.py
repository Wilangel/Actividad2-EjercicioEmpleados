class SalarioComision:
    def __init__(self, comision):
        self.salario = 1000000
        self.comision = comision
        # condicional Salario Comision
        if comision > self.salario:
            self.salario = self.salario + comision + 100000
