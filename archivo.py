# ========== PATRON CREACIONAL: FACTORY METHOD ==========
# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, salario=0):
        self.nombre = nombre
        self.salario = salario
        self.desempeno = 5

    def calcular_salario(self):
        return self.salario

    def obtener_cargo(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, salario=5000):
        super().__init__(nombre, salario)

    def obtener_cargo(self):
        return "Desarrollador"

class Disenador(Empleado):
    def __init__(self, nombre, salario=4000):
        super().__init__(nombre, salario)

    def obtener_cargo(self):
        return "Diseñador"

# FACTORY: Esta es la fabrica de empleados
# Use este patron para no tener que hacer "Desarrollador()" o "Disenador()" cada vez
# Ahora solo llamo a crear_empleado y le paso el tipo
class EmpleadoFactory:
    @staticmethod
    def crear_empleado(tipo, nombre, salario=None):
        tipo = tipo.lower().strip()
        if tipo == "dev" or tipo == "1":
            return Desarrollador(nombre, salario) if salario else Desarrollador(nombre)
        elif tipo == "design" or tipo == "2":
            return Disenador(nombre, salario) if salario else Disenador(nombre)
        else:
            raise ValueError("Tipo desconocido")


# ========== PATRON ESTRUCTURAL: DECORATOR ==========
# DECORATOR: Aqui envuelvo empleados para agregarles bonos o descuentos
# En vez de cambiar la clase Empleado, uso decoradores que le agregan funcionalidad

class ConBono(Empleado):
    def __init__(self, empleado):
        self.empleado = empleado
        self.nombre = empleado.nombre
        self.desempeno = empleado.desempeno

    def calcular_salario(self):
        return self.empleado.calcular_salario() + 1000

    def obtener_cargo(self):
        return self.empleado.obtener_cargo() + " [+Bono]"

class ConDescuento(Empleado):
    def __init__(self, empleado):
        self.empleado = empleado
        self.nombre = empleado.nombre
        self.desempeno = empleado.desempeno

    def calcular_salario(self):
        return self.empleado.calcular_salario() - 500

    def obtener_cargo(self):
        return self.empleado.obtener_cargo() + " [-Descuento]"


# ========== PATRÓN COMPORTAMIENTO: STRATEGY ==========
# STRATEGY: Diferentes formas de evaluar el desempeño del empleado
# Permite cambiar el criterio de evaluación

class EstrategiaEvaluacion:
    def evaluar(self, empleado):
        pass

class EvaluacionEstricta(EstrategiaEvaluacion):
    def evaluar(self, empleado):
        if empleado.desempeno >= 9:
            return "EXCELENTE - Supera expectativas"
        elif empleado.desempeno >= 7:
            return "BUENO - Cumple expectativas"
        else:
            return "NECESITA MEJORAR - Plan de desarrollo requerido"

class EvaluacionFlexible(EstrategiaEvaluacion):
    def evaluar(self, empleado):
        if empleado.desempeno >= 7:
            return "EXCELENTE - Buen trabajo"
        elif empleado.desempeno >= 5:
            return "BUENO - Desempeño aceptable"
        else:
            return "NECESITA MEJORAR - Requiere seguimiento"

class SistemaEvaluacion:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def evaluar_empleado(self, empleado):
        return self.estrategia.evaluar(empleado)


# ========== SISTEMA DE GESTIÓN ==========
lista_empleados = []

def crear_empleado():
    print("\n--- CREAR EMPLEADO ---")
    nombre = input("Nombre del empleado: ")
    print("1. Desarrollador (dev)")
    print("2. Diseñador (design)")
    tipo = input("Tipo: ")
    salario_input = input("Salario (Enter para salario por defecto): ")
    salario = int(salario_input) if salario_input else None
    empleado = EmpleadoFactory.crear_empleado(tipo, nombre, salario)
    lista_empleados.append(empleado)
    print(f"✓ Empleado {nombre} creado como {empleado.obtener_cargo()} con salario ${empleado.calcular_salario()}")

def ver_empleados():
    print("\n--- LISTA DE EMPLEADOS ---")
    if not lista_empleados:
        print("No hay empleados registrados")
        return
    for i, emp in enumerate(lista_empleados):
        print(f"{i+1}. {emp.nombre} - {emp.obtener_cargo()} - Salario: ${emp.calcular_salario()}")

def eliminar_empleado():
    ver_empleados()
    if not lista_empleados:
        return
    num = int(input("\nNúmero de empleado a eliminar: ")) - 1
    if 0 <= num < len(lista_empleados):
        eliminado = lista_empleados.pop(num)
        print(f"✓ Empleado {eliminado.nombre} eliminado")

def editar_empleado():
    ver_empleados()
    if not lista_empleados:
        return
    num = int(input("\nNúmero de empleado a editar: ")) - 1
    if 0 <= num < len(lista_empleados):
        print("1. Editar nombre")
        print("2. Editar salario")
        opcion = input("¿Qué desea editar?: ")
        if opcion == "1":
            nuevo_nombre = input("Nuevo nombre: ")
            lista_empleados[num].nombre = nuevo_nombre
            print(f"✓ Nombre actualizado a {nuevo_nombre}")
        elif opcion == "2":
            nuevo_salario = int(input("Nuevo salario: "))
            lista_empleados[num].salario = nuevo_salario
            print(f"✓ Salario actualizado a ${nuevo_salario}")

def aplicar_bono():
    ver_empleados()
    if not lista_empleados:
        return
    num = int(input("\nNúmero de empleado para aplicar bono: ")) - 1
    if 0 <= num < len(lista_empleados):
        empleado = lista_empleados[num]
        lista_empleados[num] = ConBono(empleado)
        print(f"✓ Bono aplicado a {empleado.nombre}. Nuevo salario: ${lista_empleados[num].calcular_salario()}")

def aplicar_descuento():
    ver_empleados()
    if not lista_empleados:
        return
    num = int(input("\nNúmero de empleado para aplicar descuento: ")) - 1
    if 0 <= num < len(lista_empleados):
        empleado = lista_empleados[num]
        lista_empleados[num] = ConDescuento(empleado)
        print(f"✓ Descuento aplicado a {empleado.nombre}. Nuevo salario: ${lista_empleados[num].calcular_salario()}")

def calificar_desempeno():
    ver_empleados()
    if not lista_empleados:
        return
    num = int(input("\nNúmero de empleado a calificar: ")) - 1
    if 0 <= num < len(lista_empleados):
        calificacion = int(input("Calificación de desempeño (1-10): "))
        if 1 <= calificacion <= 10:
            lista_empleados[num].desempeno = calificacion
            print(f"✓ Desempeño de {lista_empleados[num].nombre} actualizado a {calificacion}/10")
        else:
            print("Calificación debe estar entre 1 y 10")

def ver_estadisticas():
    if not lista_empleados:
        print("\nNo hay empleados registrados")
        return

    print("\n" + "="*60)
    print("         ESTADÍSTICAS Y EVALUACIÓN DE EMPLEADOS")
    print("="*60)

    print("\nTipo de evaluación:")
    print("1. Evaluación Estricta")
    print("2. Evaluación Flexible")
    tipo = input("Seleccione: ")

    if tipo == "1":
        sistema = SistemaEvaluacion(EvaluacionEstricta())
        tipo_eval = "ESTRICTA"
    else:
        sistema = SistemaEvaluacion(EvaluacionFlexible())
        tipo_eval = "FLEXIBLE"

    print(f"\n{'='*60}")
    print(f"            EVALUACIÓN {tipo_eval}")
    print(f"{'='*60}\n")

    for emp in lista_empleados:
        resultado = sistema.evaluar_empleado(emp)
        print(f"👤 {emp.nombre}")
        print(f"   Cargo: {emp.obtener_cargo()}")
        print(f"   Salario: ${emp.calcular_salario()}")
        print(f"   Desempeño: {emp.desempeno}/10")
        print(f"   {resultado}")
        print()

def menu():
    while True:
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
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            crear_empleado()
        elif opcion == "2":
            ver_empleados()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            editar_empleado()
        elif opcion == "5":
            aplicar_bono()
        elif opcion == "6":
            aplicar_descuento()
        elif opcion == "7":
            calificar_desempeno()
        elif opcion == "8":
            ver_estadisticas()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

menu()
