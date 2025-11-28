# Sistema de Gestión de Empleados

## Arquitectura de 3 Capas

Este proyecto implementa un sistema de gestión de empleados utilizando la arquitectura de 3 capas y múltiples patrones de diseño.

### Estructura del Proyecto

```
AplicacionDePatrones/
│
├── main.py                          # Punto de entrada de la aplicación
│
├── data/                            # CAPA DE DATOS
│   ├── models/                      # Modelos de dominio
│   │   ├── empleado.py             # Entidades: Empleado, Desarrollador, Diseñador
│   │   └── empleado_decorado.py    # Decoradores: ConBono, ConDescuento
│   │
│   └── repositories/                # Gestión de persistencia
│       └── empleado_repository.py  # Repositorio de empleados
│
├── business/                        # CAPA DE LÓGICA DE NEGOCIO
│   ├── services/                    # Servicios de negocio
│   │   ├── empleado_service.py     # Lógica de gestión de empleados
│   │   └── evaluacion_service.py   # Lógica de evaluación de desempeño
│   │
│   ├── factories/                   # Patrón Factory
│   │   └── empleado_factory.py     # Factory para crear empleados
│   │
│   └── strategies/                  # Patrón Strategy
│       └── estrategia_evaluacion.py # Estrategias de evaluación
│
└── presentation/                    # CAPA DE PRESENTACIÓN
    ├── views/                       # Vistas de usuario
    │   ├── menu_view.py            # Vista del menú principal
    │   ├── empleado_view.py        # Vista de empleados
    │   └── estadisticas_view.py    # Vista de estadísticas
    │
    └── controllers/                 # Controladores
        └── menu_controller.py      # Controlador principal del menú
```

## Descripción de las Capas

### 1. Capa de Datos (`data/`)
Responsable de la gestión de datos y persistencia.

- **Modelos**: Definen las entidades del dominio (Empleado, Desarrollador, Diseñador)
- **Repositorios**: Manejan el almacenamiento y recuperación de datos

**Principio**: Esta capa no conoce la lógica de negocio ni la presentación.

### 2. Capa de Lógica de Negocio (`business/`)
Contiene toda la lógica de negocio de la aplicación.

- **Servicios**: Implementan las reglas de negocio
- **Factories**: Patrón creacional para instanciar objetos
- **Strategies**: Patrón comportamental para algoritmos intercambiables

**Principio**: Esta capa no conoce la presentación, solo usa la capa de datos.

### 3. Capa de Presentación (`presentation/`)
Maneja la interacción con el usuario.

- **Vistas**: Muestran información al usuario y capturan entrada
- **Controladores**: Coordinan entre las vistas y los servicios

**Principio**: Esta capa solo usa la capa de negocio y se encarga de la UI.

## Patrones de Diseño Implementados

### 1. Factory Method (Creacional)
**Ubicación**: `business/factories/empleado_factory.py`

Permite crear diferentes tipos de empleados sin especificar sus clases exactas.

```python
empleado = EmpleadoFactory.crear_empleado("dev", "Juan", 6000)
```

### 2. Decorator (Estructural)
**Ubicación**: `data/models/empleado_decorado.py`

Permite agregar funcionalidad (bonos, descuentos) a empleados dinámicamente.

```python
empleado_con_bono = ConBono(empleado)
empleado_con_descuento = ConDescuento(empleado)
```

### 3. Strategy (Comportamental)
**Ubicación**: `business/strategies/estrategia_evaluacion.py`

Permite cambiar el algoritmo de evaluación de desempeño en tiempo de ejecución.

```python
evaluacion = EvaluacionService(EvaluacionEstricta())
evaluacion.cambiar_estrategia(EvaluacionFlexible())
```

## Flujo de Datos

```
Usuario
  ↓
[Presentation Layer]
  Controllers ← Views
  ↓
[Business Layer]
  Services ← Factories/Strategies
  ↓
[Data Layer]
  Repositories ← Models
  ↓
Datos
```

## Ventajas de esta Arquitectura

1. **Separación de Responsabilidades**: Cada capa tiene una responsabilidad clara
2. **Mantenibilidad**: Cambios en una capa no afectan las otras
3. **Testabilidad**: Cada capa puede probarse independientemente
4. **Escalabilidad**: Fácil agregar nuevas funcionalidades
5. **Reutilización**: Los componentes pueden reutilizarse
6. **Flexibilidad**: Fácil cambiar implementaciones (ej: cambiar repositorio de memoria a base de datos)

## Cómo Ejecutar

```bash
python main.py
```

## Funcionalidades

1. Crear empleados (Desarrollador/Diseñador)
2. Ver lista de empleados
3. Eliminar empleados
4. Editar empleados (nombre/salario)
5. Aplicar bonos (+$1000)
6. Aplicar descuentos (-$500)
7. Calificar desempeño (1-10)
8. Ver estadísticas con evaluación estricta o flexible

## Autor

Sistema educativo para demostrar arquitectura de 3 capas y patrones de diseño.
