# ========== PATRON ESTRUCTURAL: DECORATOR ==========
# Decoradores para empleados (bonos y descuentos)

from data.models.empleado import Empleado


class ConBono(Empleado):
    """Decorador que agrega un bono al salario del empleado"""
    def __init__(self, empleado):
        self.empleado = empleado
        self.nombre = empleado.nombre
        self.desempeno = empleado.desempeno

    def calcular_salario(self):
        return self.empleado.calcular_salario() + 1000

    def obtener_cargo(self):
        return self.empleado.obtener_cargo() + " [+Bono]"


class ConDescuento(Empleado):
    """Decorador que aplica un descuento al salario del empleado"""
    def __init__(self, empleado):
        self.empleado = empleado
        self.nombre = empleado.nombre
        self.desempeno = empleado.desempeno

    def calcular_salario(self):
        return self.empleado.calcular_salario() - 500

    def obtener_cargo(self):
        return self.empleado.obtener_cargo() + " [-Descuento]"
