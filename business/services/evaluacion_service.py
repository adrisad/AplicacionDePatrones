# ========== CAPA DE LÓGICA DE NEGOCIO: SERVICIO DE EVALUACIÓN ==========

from business.strategies.estrategia_evaluacion import EstrategiaEvaluacion


class EvaluacionService:
    """Servicio para evaluar el desempeño de empleados usando el patrón Strategy"""

    def __init__(self, estrategia: EstrategiaEvaluacion):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaEvaluacion):
        """Cambia la estrategia de evaluación"""
        self.estrategia = estrategia

    def evaluar_empleado(self, empleado):
        """
        Evalúa a un empleado usando la estrategia configurada

        Args:
            empleado: Empleado a evaluar

        Returns:
            Resultado de la evaluación como string
        """
        return self.estrategia.evaluar(empleado)

    def evaluar_lista_empleados(self, empleados):
        """
        Evalúa una lista de empleados

        Args:
            empleados: Lista de empleados a evaluar

        Returns:
            Lista de tuplas (empleado, evaluación)
        """
        return [(emp, self.evaluar_empleado(emp)) for emp in empleados]
