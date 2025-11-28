# ========== CAPA DE DATOS: REPOSITORIO ==========
# Esta capa maneja el almacenamiento y recuperación de datos

class EmpleadoRepository:
    """Repositorio para gestionar la persistencia de empleados"""

    def __init__(self):
        self._empleados = []

    def agregar(self, empleado):
        """Agrega un empleado al repositorio"""
        self._empleados.append(empleado)
        return empleado

    def obtener_todos(self):
        """Obtiene todos los empleados"""
        return self._empleados.copy()

    def obtener_por_indice(self, indice):
        """Obtiene un empleado por su índice"""
        if 0 <= indice < len(self._empleados):
            return self._empleados[indice]
        return None

    def eliminar_por_indice(self, indice):
        """Elimina un empleado por su índice"""
        if 0 <= indice < len(self._empleados):
            return self._empleados.pop(indice)
        return None

    def actualizar_por_indice(self, indice, empleado):
        """Actualiza un empleado por su índice"""
        if 0 <= indice < len(self._empleados):
            self._empleados[indice] = empleado
            return empleado
        return None

    def contar(self):
        """Retorna el número de empleados"""
        return len(self._empleados)

    def esta_vacio(self):
        """Verifica si el repositorio está vacío"""
        return len(self._empleados) == 0
