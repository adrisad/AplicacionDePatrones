# ========== CAPA DE PRESENTACIÓN: VISTA DE ESTADÍSTICAS ==========


class EstadisticasView:
    """Vista para mostrar estadísticas y evaluaciones de empleados"""

    @staticmethod
    def solicitar_tipo_evaluacion():
        """Solicita el tipo de evaluación al usuario"""
        print("\nTipo de evaluación:")
        print("1. Evaluación Estricta")
        print("2. Evaluación Flexible")
        return input("Seleccione: ")

    @staticmethod
    def mostrar_encabezado_estadisticas(tipo_eval):
        """Muestra el encabezado de las estadísticas"""
        print("\n" + "="*60)
        print("         ESTADÍSTICAS Y EVALUACIÓN DE EMPLEADOS")
        print("="*60)
        print(f"\n{'='*60}")
        print(f"            EVALUACIÓN {tipo_eval}")
        print(f"{'='*60}\n")

    @staticmethod
    def mostrar_evaluacion_empleado(empleado, resultado):
        """Muestra la evaluación de un empleado"""
        print(f"👤 {empleado.nombre}")
        print(f"   Cargo: {empleado.obtener_cargo()}")
        print(f"   Salario: ${empleado.calcular_salario()}")
        print(f"   Desempeño: {empleado.desempeno}/10")
        print(f"   {resultado}")
        print()

    @staticmethod
    def mostrar_sin_empleados():
        """Muestra mensaje cuando no hay empleados"""
        print("\nNo hay empleados registrados")
