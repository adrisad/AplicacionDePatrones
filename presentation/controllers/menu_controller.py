# ========== CAPA DE PRESENTACIÓN: CONTROLADOR DE MENÚ ==========
# El controlador coordina entre las vistas y los servicios

from business.services.empleado_service import EmpleadoService
from business.services.evaluacion_service import EvaluacionService
from business.strategies.estrategia_evaluacion import EvaluacionEstricta, EvaluacionFlexible
from presentation.views.menu_view import MenuView
from presentation.views.empleado_view import EmpleadoView
from presentation.views.estadisticas_view import EstadisticasView


class MenuController:
    """Controlador principal del sistema"""

    def __init__(self, empleado_service: EmpleadoService):
        self.empleado_service = empleado_service
        self.menu_view = MenuView()
        self.empleado_view = EmpleadoView()
        self.estadisticas_view = EstadisticasView()

    def ejecutar(self):
        """Ejecuta el bucle principal del menú"""
        while True:
            self.menu_view.mostrar_menu()
            opcion = self.menu_view.solicitar_opcion()

            if opcion == "1":
                self.crear_empleado()
            elif opcion == "2":
                self.ver_empleados()
            elif opcion == "3":
                self.eliminar_empleado()
            elif opcion == "4":
                self.editar_empleado()
            elif opcion == "5":
                self.aplicar_bono()
            elif opcion == "6":
                self.aplicar_descuento()
            elif opcion == "7":
                self.calificar_desempeno()
            elif opcion == "8":
                self.ver_estadisticas()
            elif opcion == "9":
                self.menu_view.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.menu_view.mostrar_error("Opción inválida")

    def crear_empleado(self):
        """Crea un nuevo empleado"""
        try:
            nombre, tipo, salario = self.empleado_view.mostrar_formulario_creacion()
            empleado = self.empleado_service.crear_empleado(tipo, nombre, salario)
            self.empleado_view.mostrar_empleado_creado(empleado)
        except ValueError as e:
            self.menu_view.mostrar_error(str(e))
        except Exception as e:
            self.menu_view.mostrar_error(f"Error al crear empleado: {e}")

    def ver_empleados(self):
        """Muestra la lista de empleados"""
        empleados = self.empleado_service.obtener_todos_empleados()
        self.empleado_view.mostrar_lista_empleados(empleados)

    def eliminar_empleado(self):
        """Elimina un empleado"""
        self.ver_empleados()
        if not self.empleado_service.hay_empleados():
            return

        try:
            indice = self.empleado_view.solicitar_numero_empleado("Número de empleado a eliminar")
            empleado = self.empleado_service.eliminar_empleado(indice)
            if empleado:
                self.empleado_view.mostrar_empleado_eliminado(empleado)
            else:
                self.menu_view.mostrar_error("Índice inválido")
        except (ValueError, IndexError):
            self.menu_view.mostrar_error("Número inválido")

    def editar_empleado(self):
        """Edita un empleado"""
        self.ver_empleados()
        if not self.empleado_service.hay_empleados():
            return

        try:
            indice = self.empleado_view.solicitar_numero_empleado("Número de empleado a editar")
            opcion = self.empleado_view.mostrar_menu_edicion()

            if opcion == "1":
                nuevo_nombre = self.empleado_view.solicitar_nuevo_nombre()
                if self.empleado_service.actualizar_nombre_empleado(indice, nuevo_nombre):
                    self.empleado_view.mostrar_nombre_actualizado(nuevo_nombre)
                else:
                    self.menu_view.mostrar_error("Error al actualizar nombre")
            elif opcion == "2":
                nuevo_salario = self.empleado_view.solicitar_nuevo_salario()
                if self.empleado_service.actualizar_salario_empleado(indice, nuevo_salario):
                    self.empleado_view.mostrar_salario_actualizado(nuevo_salario)
                else:
                    self.menu_view.mostrar_error("Error al actualizar salario")
            else:
                self.menu_view.mostrar_error("Opción inválida")
        except (ValueError, IndexError):
            self.menu_view.mostrar_error("Número inválido")

    def aplicar_bono(self):
        """Aplica un bono a un empleado"""
        self.ver_empleados()
        if not self.empleado_service.hay_empleados():
            return

        try:
            indice = self.empleado_view.solicitar_numero_empleado("Número de empleado para aplicar bono")
            empleado = self.empleado_service.aplicar_bono_empleado(indice)
            if empleado:
                self.empleado_view.mostrar_bono_aplicado(empleado)
            else:
                self.menu_view.mostrar_error("Índice inválido")
        except (ValueError, IndexError):
            self.menu_view.mostrar_error("Número inválido")

    def aplicar_descuento(self):
        """Aplica un descuento a un empleado"""
        self.ver_empleados()
        if not self.empleado_service.hay_empleados():
            return

        try:
            indice = self.empleado_view.solicitar_numero_empleado("Número de empleado para aplicar descuento")
            empleado = self.empleado_service.aplicar_descuento_empleado(indice)
            if empleado:
                self.empleado_view.mostrar_descuento_aplicado(empleado)
            else:
                self.menu_view.mostrar_error("Índice inválido")
        except (ValueError, IndexError):
            self.menu_view.mostrar_error("Número inválido")

    def calificar_desempeno(self):
        """Califica el desempeño de un empleado"""
        self.ver_empleados()
        if not self.empleado_service.hay_empleados():
            return

        try:
            indice = self.empleado_view.solicitar_numero_empleado("Número de empleado a calificar")
            calificacion = self.empleado_view.solicitar_calificacion()

            empleados = self.empleado_service.obtener_todos_empleados()
            if self.empleado_service.calificar_desempeno_empleado(indice, calificacion):
                self.empleado_view.mostrar_calificacion_actualizada(empleados[indice], calificacion)
            else:
                self.empleado_view.mostrar_calificacion_invalida()
        except (ValueError, IndexError):
            self.menu_view.mostrar_error("Número inválido")

    def ver_estadisticas(self):
        """Muestra estadísticas y evaluaciones de empleados"""
        if not self.empleado_service.hay_empleados():
            self.estadisticas_view.mostrar_sin_empleados()
            return

        tipo = self.estadisticas_view.solicitar_tipo_evaluacion()

        if tipo == "1":
            evaluacion_service = EvaluacionService(EvaluacionEstricta())
            tipo_eval = "ESTRICTA"
        else:
            evaluacion_service = EvaluacionService(EvaluacionFlexible())
            tipo_eval = "FLEXIBLE"

        self.estadisticas_view.mostrar_encabezado_estadisticas(tipo_eval)

        empleados = self.empleado_service.obtener_todos_empleados()
        evaluaciones = evaluacion_service.evaluar_lista_empleados(empleados)

        for emp, resultado in evaluaciones:
            self.estadisticas_view.mostrar_evaluacion_empleado(emp, resultado)
