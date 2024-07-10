
estudiante = []
def datosAlumno(coleccion): #En parametro colocamos estudiante ya que ahi se almacenará los datos de cada estudiante.
    try: 
        nombre = input("Ingrese el nómbre del estudiante.-->")
        apellido = input("Ingrese el apellido del estudiante.-->")
        rut = input("Ingrese el rut del estudiante.(ej: 1234567-8)-->")
        curso = input("Ingrese el curso del estudiante.-->")
        promedio = input("Ingrese el promedio del estudiante.-->")
        
    except:
        print("ERR0r404#####.... Vuelva a intentar.")

    coleccion.append([nombre, apellido, rut, curso, promedio]) #Aquí se agregan todos los datos del estudiante con un .append a la lista estudiante
    
    print("Se ha guardado correctamente.")

    for estudiante in coleccion:
        print(estudiante) #un for que permita ver el estudiante ingresado


def mostrarAlumnos(estudiante): #En parametros colocamos a estudiante ya que ahí están los datos de los alumnos, para que se pueda mostrar
    contador = 1 
    if not estudiante:
        print("No hay alumnos ingresados")
    else:
        print("\tNOMBRE  |  APELLIDO  |  RUT  |  CURSO  |  PROMEDIO \n")
        for estudiante in estudiante: #Utulizamos este for para imprimir los 5 datos ingresados del estudiante
            print(f"  {contador}.-{estudiante[0]:<5} | {estudiante[1]:<6} | {estudiante[2]:<5} | {estudiante[3]:<5} | {estudiante[4]:<5}") 
            contador = contador + 1 #colocamos contador +1 ya que irá sumando 1 cada vez que se ingresa un alumno

def eliminarAlumno(coleccion):
        try:
            rutEliminar = input("Ingrese el rut del alumno que quiere eliminar.(ej:1234567-8)-->")

            for estudiante in coleccion[:]:
                if estudiante[2] == rutEliminar:
                    coleccion.remove(estudiante)
                    print(f"Estudiante con rut {rutEliminar} eliminado correctamente.")
                    return
        except ValueError:
            print("ERR0r, el rut ingresado no existe.")


def modEstudiante(coleccion):
    mostrarAlumnos(coleccion)
    try:
        rutMod = input("Ingresa el rut del estudiante que quieres modificar.(ej:1234567-8)-->")
    except:
        print("El rut ingresado no existe")

    for estudiante in coleccion:
        if estudiante[2] == rutMod: 
            print(f"El alumno con rut {rutMod} será modificado a continuación.")
        
            nomNuevo = input("Ingresa el nuevo nómbre del estudiante--->")
            apeNuevo = input("Ingresa el nuevo apellido del estudiante--->")
            rutNuevo = input("Ingresa el nuevo rut del estudiante--->")
            cursoNuevo = input("Ingresa el nuevo curso del estudiante--->")
            promNuevo = input("Ingresa el nuevo promedio del estudiante--->")

            estudiante[0] = nomNuevo
            estudiante[1] = apeNuevo
            estudiante[2] = rutNuevo
            estudiante[3] = cursoNuevo
            estudiante[4] = promNuevo

            print("Se ha modificado correctamente el alumno")
            print(estudiante)
            break

def guardarAlumno(alumnos):
    with open('Alumnos2024.txt', 'w', encoding='utf-8', newline='') as archivo:
        archivo.write(f"{'| NOMBRE |': <20}{'| APELLIDO |':<20}{'| RUT |': <20}{'| CURSO |': <20}{'| PROMEDIO |':<20}\n")  # Agregamos \n al final
        archivo.write("_" * 100 + "\n")  # Línea de separación 
        for alumnos in alumnos:
            archivo.write(f"{alumnos[0]:<20}{alumnos[1]:<20}{alumnos[2]:<20}{alumnos[3]:<20}{alumnos[4]:<20}\n")
            archivo.write("_"* 100 + "\n")
            print("Se ha guardado correctamente el estudiante.")




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
        datosAlumno(estudiante)
    elif (opc == 2):
        mostrarAlumnos(estudiante)
    elif (opc == 3):
        eliminarAlumno(estudiante)
    elif (opc == 4): 
        modEstudiante(estudiante)
    elif (opc == 5):
        guardarAlumno(estudiante)
    elif (opc == 6):
        print("Cerrando sesión....")
        break
    else:
        print("A ocurrido un error, Vuelva a intentarlo...")