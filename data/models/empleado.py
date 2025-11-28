# ========== CAPA DE DATOS: MODELOS ==========
# Esta capa contiene las entidades del dominio

class Empleado:
    """Clase base para todos los empleados"""
    def __init__(self, nombre, salario=0):
        self.nombre = nombre
        self.salario = salario
        self.desempeno = 5

    def calcular_salario(self):
        return self.salario

    def obtener_cargo(self):
        pass


class Desarrollador(Empleado):
    """Modelo de empleado desarrollador"""
    def __init__(self, nombre, salario=5000):
        super().__init__(nombre, salario)

    def obtener_cargo(self):
        return "Desarrollador"


class Disenador(Empleado):
    """Modelo de empleado diseñador"""
    def __init__(self, nombre, salario=4000):
        super().__init__(nombre, salario)

    def obtener_cargo(self):
        return "Diseñador"
