# ========== PATRON CREACIONAL: FACTORY METHOD ==========
# Factory para crear diferentes tipos de empleados

from data.models.empleado import Desarrollador, Disenador


class EmpleadoFactory:
    """Factory para crear empleados según su tipo"""

    @staticmethod
    def crear_empleado(tipo, nombre, salario=None):
        """
        Crea un empleado del tipo especificado

        Args:
            tipo: Tipo de empleado ('dev'/'1' para Desarrollador, 'design'/'2' para Diseñador)
            nombre: Nombre del empleado
            salario: Salario opcional (usa el salario por defecto si no se proporciona)

        Returns:
            Instancia de Empleado del tipo correspondiente

        Raises:
            ValueError: Si el tipo de empleado es desconocido
        """
        tipo = tipo.lower().strip()

        if tipo == "dev" or tipo == "1":
            return Desarrollador(nombre, salario) if salario else Desarrollador(nombre)
        elif tipo == "design" or tipo == "2":
            return Disenador(nombre, salario) if salario else Disenador(nombre)
        else:
            raise ValueError(f"Tipo de empleado desconocido: {tipo}")
