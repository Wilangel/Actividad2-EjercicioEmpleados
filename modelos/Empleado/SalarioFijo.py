class SalarioFijo:
    def __init__(self, salario, años):
        self.salario = salario
        self.años = años
        # Condicional Salario Fijo bono antiguedad
        # condicion menos de dos años
        if años < 2:
            self.salario = salario
            # condicion entre 2 y 3 años
        if años == 2 or años == 3:
            bonoAntiguedad = self.salario * 0.05
            self.salario = bonoAntiguedad + self.salario
            # condicion entre 4 y 7 años
        if años >= 4 and años <= 7:
            bonoAntiguedad = self.salario * 0.1
            self.salario = bonoAntiguedad + self.salario
            # condicion entre 8 y 15 años
        if años >= 8 and años <= 15:
            bonoAntiguedad = self.salario * 0.15
            self.salario = bonoAntiguedad + self.salario
            # condicion mas de 15 años
        if años > 15:
            bonoAntiguedad = self.salario * 0.2
            self.salario = bonoAntiguedad + self.salario
