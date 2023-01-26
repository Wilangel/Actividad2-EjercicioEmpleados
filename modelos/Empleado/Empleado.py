from modelos.Empleado.SalarioFijo import SalarioFijo
from modelos.Empleado.SalarioComision import SalarioComision


class Empleado:
    def __init__(self, nombre, tipo, salario, comision=0, años=0):
        self.nombre = nombre
        self.tipo = tipo
        # Condicional tipo de salario
        if tipo == 'Fijo':
            tipoEmpleado = SalarioFijo(salario, años)
            self.salario = tipoEmpleado.salario
        if tipo == 'comision':
            tipoEmpleado = SalarioComision(comision)
            self.salario = tipoEmpleado.salario

     # Metodo Obtencion de Informacion
    def ObtieneInfoEmpleado(self):
        print(
            f'\nNombre: {self.nombre} \ntipo Empleado: {self.tipo} \nSalario: {self.salario}\n ')
        print(
            '------------------------------------------------------------------------------')
