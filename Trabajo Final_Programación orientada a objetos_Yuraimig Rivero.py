class Tarea:
    """Clase que representa una tarea individual."""
    
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaTareas:
    """Clase que gestiona una lista de tareas pendientes."""
    
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada correctamente.")

    def marcar_tarea_completada(self, indice):
        """Marca una tarea como completada según su índice."""
        try:
            self.tareas[indice].marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("Error: Índice de tarea no válido.")

    def mostrar_tareas(self):
        """Muestra todas las tareas con su estado."""
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista según su índice."""
        try:
            del self.tareas[indice]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("Error: Índice de tarea no válido.")


def main():
    """Función principal que maneja la interacción con el usuario."""
    lista_tareas = ListaTareas()
    
    while True:
        print("\nGestión de Tareas Pendientes")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Opción no válida. Por favor, ingrese un número.")
            continue

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            try:
                indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
                lista_tareas.marcar_tarea_completada(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 3:
            lista_tareas.mostrar_tareas()
        elif opcion == 4:
            try:
                indice = int(input("Ingrese el índice de la tarea a eliminar: "))
                lista_tareas.eliminar_tarea(indice)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
 