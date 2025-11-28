# ========== CAPA DE LÓGICA DE NEGOCIO: SERVICIOS ==========
# Esta capa contiene la lógica de negocio de la aplicación

from business.factories.empleado_factory import EmpleadoFactory
from data.models.empleado_decorado import ConBono, ConDescuento
from data.repositories.empleado_repository import EmpleadoRepository


class EmpleadoService:
    """Servicio para gestionar las operaciones de negocio relacionadas con empleados"""

    def __init__(self, repository: EmpleadoRepository):
        self.repository = repository

    def crear_empleado(self, tipo, nombre, salario=None):
        """
        Crea un nuevo empleado y lo agrega al repositorio

        Args:
            tipo: Tipo de empleado
            nombre: Nombre del empleado
            salario: Salario opcional

        Returns:
            El empleado creado
        """
        empleado = EmpleadoFactory.crear_empleado(tipo, nombre, salario)
        self.repository.agregar(empleado)
        return empleado

    def obtener_todos_empleados(self):
        """Obtiene todos los empleados del repositorio"""
        return self.repository.obtener_todos()

    def eliminar_empleado(self, indice):
        """
        Elimina un empleado por su índice

        Args:
            indice: Índice del empleado a eliminar

        Returns:
            El empleado eliminado o None si el índice es inválido
        """
        return self.repository.eliminar_por_indice(indice)

    def actualizar_nombre_empleado(self, indice, nuevo_nombre):
        """
        Actualiza el nombre de un empleado

        Args:
            indice: Índice del empleado
            nuevo_nombre: Nuevo nombre del empleado

        Returns:
            True si se actualizó correctamente, False en caso contrario
        """
        empleado = self.repository.obtener_por_indice(indice)
        if empleado:
            empleado.nombre = nuevo_nombre
            return True
        return False

    def actualizar_salario_empleado(self, indice, nuevo_salario):
        """
        Actualiza el salario de un empleado

        Args:
            indice: Índice del empleado
            nuevo_salario: Nuevo salario del empleado

        Returns:
            True si se actualizó correctamente, False en caso contrario
        """
        empleado = self.repository.obtener_por_indice(indice)
        if empleado:
            empleado.salario = nuevo_salario
            return True
        return False

    def aplicar_bono_empleado(self, indice):
        """
        Aplica un bono a un empleado usando el patrón Decorator

        Args:
            indice: Índice del empleado

        Returns:
            El empleado decorado con bono o None si el índice es inválido
        """
        empleado = self.repository.obtener_por_indice(indice)
        if empleado:
            empleado_con_bono = ConBono(empleado)
            self.repository.actualizar_por_indice(indice, empleado_con_bono)
            return empleado_con_bono
        return None

    def aplicar_descuento_empleado(self, indice):
        """
        Aplica un descuento a un empleado usando el patrón Decorator

        Args:
            indice: Índice del empleado

        Returns:
            El empleado decorado con descuento o None si el índice es inválido
        """
        empleado = self.repository.obtener_por_indice(indice)
        if empleado:
            empleado_con_descuento = ConDescuento(empleado)
            self.repository.actualizar_por_indice(indice, empleado_con_descuento)
            return empleado_con_descuento
        return None

    def calificar_desempeno_empleado(self, indice, calificacion):
        """
        Califica el desempeño de un empleado

        Args:
            indice: Índice del empleado
            calificacion: Calificación del 1 al 10

        Returns:
            True si se calificó correctamente, False en caso contrario
        """
        if not (1 <= calificacion <= 10):
            return False

        empleado = self.repository.obtener_por_indice(indice)
        if empleado:
            empleado.desempeno = calificacion
            return True
        return False

    def hay_empleados(self):
        """Verifica si hay empleados en el repositorio"""
        return not self.repository.esta_vacio()
