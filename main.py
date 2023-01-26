'''
Existen dos categorías de personal: el personal con salario fijo y el personal a comisión.
Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional en función del
número de años que llevan: menos de dos años salario base, de 2 a 3 años: 5% más; de 4 a 7
años: 10% más; de 8 a 15 años: 15% más y más de 15 años: 20% más.
Los empleados a comisión tienen un salario mínimo que será constante para todos los
empleados de este tipo sueldo más comisiones por mes si las comisiones por mes es mayor al
salario mínimo que es 1.000.000, se le dará un bono de 100.000 pesos.

CIPA LUIS C. DOVALE Y WILSON A. HERRERA
'''
from modelos.Empleado.Empleado import Empleado

# instanciamos empleados
PrimerEmpleado = Empleado('Wilson Herrera', 'Fijo', 1000000, 0, 4)
SegundoEmpleado = Empleado('Luis C. Dovale', 'comision', 1000000, 1200000)
# obtenemos informacion de empleados
PrimerEmpleado.ObtieneInfoEmpleado()
SegundoEmpleado.ObtieneInfoEmpleado()
