import defi as fun
estudiante = []

while True:
    print("/" * 60)
    print("\t|BIENVENIDO AL INGRESO DE ESTUDIANTES |")
    print("\t|_____________________________________|")
    print("\t|                                     |")
    print("\t| 1.-Ingresar datos del alumno        |")
    print("\t| 2.-Mostrar alumnos                  |")
    print("\t| 3.-Eliminar alumno                  |")
    print("\t| 4.-Modificar alumno                 |")
    print("\t| 5.-Guardar alumno                   |")
    print("\t| 6.-Cerrar Sesión                    |")
    print("\t|_____________________________________|")
    print("\t|                                     |")
    opc = int(input("\t| ¿Que opción desea usar?-->"))
    if opc == 1:
        fun.datosAlumno(estudiante)
    elif (opc == 2):
        fun.mostrarAlumnos(estudiante)
    elif (opc == 3):
        fun.eliminarAlumno(estudiante)
    elif (opc == 4): 
        fun.modEstudiante(estudiante)
    elif (opc == 5):
        fun.guardarAlumno(estudiante)
    elif (opc == 6):
        print("Cerrando sesión....")
        print("...")
        break
    else:
        print("A ocurrido un error, Vuelva a intentarlo...")