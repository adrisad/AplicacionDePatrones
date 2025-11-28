"""
Sistema de Gestión de Empleados
Arquitectura de 3 Capas con Patrones de Diseño

ARQUITECTURA:
1. Capa de Datos (data/):
   - models/: Entidades del dominio (Empleado, Desarrollador, Diseñador)
   - repositories/: Gestión de persistencia de datos

2. Capa de Lógica de Negocio (business/):
   - services/: Lógica de negocio (EmpleadoService, EvaluacionService)
   - factories/: Patrón Factory para crear empleados
   - strategies/: Patrón Strategy para evaluación de desempeño

3. Capa de Presentación (presentation/):
   - views/: Interfaces de usuario y visualización
   - controllers/: Coordinación entre vistas y servicios

PATRONES DE DISEÑO IMPLEMENTADOS:
- Factory Method: Creación de diferentes tipos de empleados
- Decorator: Aplicación de bonos y descuentos
- Strategy: Diferentes estrategias de evaluación de desempeño
"""

from data.repositories.empleado_repository import EmpleadoRepository
from business.services.empleado_service import EmpleadoService
from presentation.controllers.menu_controller import MenuController


def main():
    """Punto de entrada de la aplicación"""
    # Inicializar capa de datos
    empleado_repository = EmpleadoRepository()

    # Inicializar capa de negocio
    empleado_service = EmpleadoService(empleado_repository)

    # Inicializar capa de presentación
    menu_controller = MenuController(empleado_service)

    # Ejecutar aplicación
    menu_controller.ejecutar()


if __name__ == "__main__":
    main()
