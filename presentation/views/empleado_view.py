# ========== CAPA DE PRESENTACIÓN: VISTA DE EMPLEADOS ==========


class EmpleadoView:
    """Vista para gestionar la visualización e interacción de empleados"""

    @staticmethod
    def mostrar_formulario_creacion():
        """Muestra el formulario para crear un empleado"""
        print("\n--- CREAR EMPLEADO ---")
        nombre = input("Nombre del empleado: ")
        print("1. Desarrollador (dev)")
        print("2. Diseñador (design)")
        tipo = input("Tipo: ")
        salario_input = input("Salario (Enter para salario por defecto): ")
        salario = int(salario_input) if salario_input else None
        return nombre, tipo, salario

    @staticmethod
    def mostrar_empleado_creado(empleado):
        """Muestra confirmación de empleado creado"""
        print(f"✓ Empleado {empleado.nombre} creado como {empleado.obtener_cargo()} "
              f"con salario ${empleado.calcular_salario()}")

    @staticmethod
    def mostrar_lista_empleados(empleados):
        """Muestra la lista de empleados"""
        print("\n--- LISTA DE EMPLEADOS ---")
        if not empleados:
            print("No hay empleados registrados")
            return

        for i, emp in enumerate(empleados):
            print(f"{i+1}. {emp.nombre} - {emp.obtener_cargo()} - Salario: ${emp.calcular_salario()}")

    @staticmethod
    def solicitar_numero_empleado(mensaje="Número de empleado"):
        """Solicita el número de un empleado"""
        return int(input(f"\n{mensaje}: ")) - 1

    @staticmethod
    def mostrar_empleado_eliminado(empleado):
        """Muestra confirmación de empleado eliminado"""
        print(f"✓ Empleado {empleado.nombre} eliminado")

    @staticmethod
    def mostrar_menu_edicion():
        """Muestra el menú de edición"""
        print("1. Editar nombre")
        print("2. Editar salario")
        return input("¿Qué desea editar?: ")

    @staticmethod
    def solicitar_nuevo_nombre():
        """Solicita un nuevo nombre"""
        return input("Nuevo nombre: ")

    @staticmethod
    def solicitar_nuevo_salario():
        """Solicita un nuevo salario"""
        return int(input("Nuevo salario: "))

    @staticmethod
    def mostrar_nombre_actualizado(nuevo_nombre):
        """Muestra confirmación de nombre actualizado"""
        print(f"✓ Nombre actualizado a {nuevo_nombre}")

    @staticmethod
    def mostrar_salario_actualizado(nuevo_salario):
        """Muestra confirmación de salario actualizado"""
        print(f"✓ Salario actualizado a ${nuevo_salario}")

    @staticmethod
    def mostrar_bono_aplicado(empleado):
        """Muestra confirmación de bono aplicado"""
        print(f"✓ Bono aplicado a {empleado.nombre}. Nuevo salario: ${empleado.calcular_salario()}")

    @staticmethod
    def mostrar_descuento_aplicado(empleado):
        """Muestra confirmación de descuento aplicado"""
        print(f"✓ Descuento aplicado a {empleado.nombre}. Nuevo salario: ${empleado.calcular_salario()}")

    @staticmethod
    def solicitar_calificacion():
        """Solicita una calificación de desempeño"""
        return int(input("Calificación de desempeño (1-10): "))

    @staticmethod
    def mostrar_calificacion_actualizada(empleado, calificacion):
        """Muestra confirmación de calificación actualizada"""
        print(f"✓ Desempeño de {empleado.nombre} actualizado a {calificacion}/10")

    @staticmethod
    def mostrar_calificacion_invalida():
        """Muestra error de calificación inválida"""
        print("Calificación debe estar entre 1 y 10")
