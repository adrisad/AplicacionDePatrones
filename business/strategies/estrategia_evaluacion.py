# ========== PATRÓN COMPORTAMIENTO: STRATEGY ==========
# Diferentes estrategias para evaluar el desempeño de empleados


class EstrategiaEvaluacion:
    """Interfaz base para estrategias de evaluación"""

    def evaluar(self, empleado):
        """Evalúa el desempeño de un empleado"""
        pass


class EvaluacionEstricta(EstrategiaEvaluacion):
    """Estrategia de evaluación con criterios estrictos"""

    def evaluar(self, empleado):
        if empleado.desempeno >= 9:
            return "EXCELENTE - Supera expectativas"
        elif empleado.desempeno >= 7:
            return "BUENO - Cumple expectativas"
        else:
            return "NECESITA MEJORAR - Plan de desarrollo requerido"


class EvaluacionFlexible(EstrategiaEvaluacion):
    """Estrategia de evaluación con criterios flexibles"""

    def evaluar(self, empleado):
        if empleado.desempeno >= 7:
            return "EXCELENTE - Buen trabajo"
        elif empleado.desempeno >= 5:
            return "BUENO - Desempeño aceptable"
        else:
            return "NECESITA MEJORAR - Requiere seguimiento"
