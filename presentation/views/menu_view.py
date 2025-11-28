# ========== CAPA DE PRESENTACIÓN: VISTA DE MENÚ ==========
# Esta capa maneja la interacción con el usuario


class MenuView:
    """Vista para mostrar y gestionar el menú principal"""

    @staticmethod
    def mostrar_menu():
        """Muestra el menú principal"""
        print("\n=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")
        print("1. Crear empleado")
        print("2. Ver empleados")
        print("3. Eliminar empleado")
        print("4. Editar empleado")
        print("5. Aplicar bono: $1000")
        print("6. Aplicar descuento: -$500")
        print("7. Calificar desempeño")
        print("8. Ver estadísticas")
        print("9. Salir")

    @staticmethod
    def solicitar_opcion():
        """Solicita una opción al usuario"""
        return input("Seleccione opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje):
        """Muestra un mensaje al usuario"""
        print(mensaje)

    @staticmethod
    def mostrar_exito(mensaje):
        """Muestra un mensaje de éxito"""
        print(f"✓ {mensaje}")

    @staticmethod
    def mostrar_error(mensaje):
        """Muestra un mensaje de error"""
        print(f"✗ {mensaje}")
