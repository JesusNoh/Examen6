class Alumno:
    def __init__(self, nombre, matricula, materias_aprobadas, promedio):
        self.nombre = nombre
        self.matricula = matricula
        self.materias_aprobadas = materias_aprobadas
        self.promedio = promedio

    def __repr__(self):
        return f"{self.nombre} (Matrícula: {self.matricula}, Materias Aprobadas: {self.materias_aprobadas}, Promedio: {self.promedio})"

def seleccion_directa(alumnos):
    n = len(alumnos)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if alumnos[j].nombre < alumnos[indice_minimo].nombre:
                indice_minimo = j
        alumnos[i], alumnos[indice_minimo] = alumnos[indice_minimo], alumnos[i]

def quicksort(alumnos):
    if len(alumnos) <= 1:
        return alumnos
    else:
        pivote = alumnos[len(alumnos) // 2].materias_aprobadas
        izquierda = [alumno for alumno in alumnos if alumno.materias_aprobadas < pivote]
        medio = [alumno for alumno in alumnos if alumno.materias_aprobadas == pivote]
        derecha = [alumno for alumno in alumnos if alumno.materias_aprobadas > pivote]
        return quicksort(izquierda) + medio + quicksort(derecha)

def mostrar_alumnos(alumnos):
    print(f"{'Nombre':<20} {'Matrícula':<15} {'Materias Aprobadas':<20} {'Promedio':<10}")
    print("-" * 75)

    for alumno in alumnos:
        print(f"{alumno.nombre:<20} {alumno.matricula:<15} {alumno.materias_aprobadas:<20} {alumno.promedio:<10}")

def ingresar_alumnos(cantidad):
    lista_alumnos = []
    for _ in range(cantidad):
        nombre = input("Ingrese el nombre del alumno: ")
        matricula = input("Ingrese la matrícula del alumno: ")
        
        while True:
            try:
                materias_aprobadas = int(input("Ingrese el número de materias aprobadas: "))
                if materias_aprobadas < 0:
                    raise ValueError("El número de materias aprobadas no puede ser negativo.")
                break
            except ValueError as e:
                print(e)
        
        while True:
            try:
                promedio = float(input("Ingrese el promedio del alumno: "))
                if not (0 <= promedio <= 10):
                    raise ValueError("El promedio debe estar entre 0 y 10.")
                break
            except ValueError as e:
                print(e)
        
        nuevo_alumno = Alumno(nombre, matricula, materias_aprobadas, promedio)
        lista_alumnos.append(nuevo_alumno)
    return lista_alumnos

def main():
    alumnos = []

    while True:
        print("\nMenú de Opciones:")
        print("1. Ingresar cantidad de alumnos")
        print("2. Usar alumnos existentes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            cantidad = int(input("¿Cuántos alumnos desea ingresar? "))
            alumnos = ingresar_alumnos(cantidad)

            while True:
                print("\nMenú de Ordenamiento:")
                print("1. Ordenar por nombre (Selección Directa)")
                print("2. Ordenar por número de materias aprobadas (Quicksort)")
                print("3. Volver al menú principal")
                
                opcion_ordenamiento = input("Seleccione una opción (1-3): ")

                if opcion_ordenamiento == '1':
                    seleccion_directa(alumnos)
                    print("\nAlumnos ordenados por nombre:")
                    mostrar_alumnos(alumnos)
                
                elif opcion_ordenamiento == '2':
                    alumnos_ordenados = quicksort(alumnos)
                    print("\nAlumnos ordenados por número de materias aprobadas:")
                    mostrar_alumnos(alumnos_ordenados)
                
                elif opcion_ordenamiento == '3':
                    break
                
                else:
                    print("Opción no válida. Por favor intente de nuevo.")

        elif opcion == '2':
            if not alumnos:
                print("No hay alumnos ingresados. Por favor ingrese primero algunos alumnos.")
                continue
            
            while True:
                print("\nMenú de Ordenamiento con Alumnos Existentes:")
                print("1. Ordenar por nombre (Selección Directa)")
                print("2. Ordenar por número de materias aprobadas (Quicksort)")
                print("3. Volver al menú principal")
                
                opcion_ordenamiento = input("Seleccione una opción (1-3): ")

                if opcion_ordenamiento == '1':
                    seleccion_directa(alumnos)
                    print("\nAlumnos ordenados por nombre:")
                    mostrar_alumnos(alumnos)
                
                elif opcion_ordenamiento == '2':
                    alumnos_ordenados = quicksort(alumnos)
                    print("\nAlumnos ordenados por número de materias aprobadas:")
                    mostrar_alumnos(alumnos_ordenados)
                
                elif opcion_ordenamiento == '3':
                    break
                
                else:
                    print("Opción no válida. Por favor intente de nuevo.")

        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()
