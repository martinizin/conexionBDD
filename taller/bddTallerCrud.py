# Importar Biblioteca de conexión
import pyodbc

# Declarar variables de Conexión
name_server = 'PCMARTIN'+'\\'+'SQLEXPRESS'  # Nombre del servidor SQL
database = 'UDEMYTEST1'  # Nombre de la base de datos
username = 'pythonconect3'  # Usuario para la conexión
password = 'UDLA'  # Contraseña del usuario
controlador_odbc = 'ODBC Driver 17 for SQL Server'  # Controlador ODBC para SQL Server.

# Crear Cadena de Conexion
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

# Función insertar registros
def insertar_registro(conexion):
    """
    Funcion para insertar un nuevo registro en la tabla .
    """
    try:
        cursor = conexion.cursor()  # Crear un cursor para ejecutar la consulta
        print("\n\tInserción de un nuevo registro:")
        # Solicitar al usuario los datos del curso
        IDCurso = input("Ingrese el ID del curso: ")
        NombreCurso = input("Ingrese el nombre del curso: ")
        Descripcion = input("Ingrese la descripción: ")
        precio_por_hora = float(input("Ingrese el precio por hora: "))
        TipoCurso = input("Ingrese el tipo de curso: ")

        # Consulta SQL para insertar un registro
        query = """
        INSERT INTO cursos (IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (IDCurso, NombreCurso, Descripcion, precio_por_hora, TipoCurso))  # Ejecutar la consulta
        conexion.commit()  # Confirmar los cambios
        print("\nRegistro insertado exitosamente.")
    except Exception as e:
        print("\nOcurrió un error al insertar el registro: ", e)

# Función eliminar registros
def eliminar_registro(conexion):
    """
    En esta funcion eliminamos un registro existente en la tabla 'cursos'.
    """
    try:
        cursor = conexion.cursor()
        print("\n\tEliminación de un registro:")
        id_curso = int(input("Ingrese el ID del curso a eliminar: "))

        # Consulta SQL para eliminar un registro
        query = "DELETE FROM cursos WHERE IDCurso = ?"
        cursor.execute(query, (id_curso,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("\nRegistro eliminado exitosamente.")
        else:
            print("\nNo se encontró el registro con ese ID.")
    except Exception as e:
        print("\nOcurrió un error al eliminar el registro: ", e)

# Función actualizar registros
def actualizar_registro(conexion):
    """
    Esta funcion se encarga de permitirnos actualizar cada campo de la tabla'.
    """
    try:
        cursor = conexion.cursor()
        print("\n\tActualización de un registro:")
        # Solicitar al usuario los nuevos datos
        id_curso = int(input("Ingrese el ID del curso a actualizar: "))
        nuevo_curso = input("Ingrese el nuevo nombre del curso: ")
        nueva_descripcion = input("Ingrese la nueva descripción: ")
        nuevo_precio = float(input("Ingrese el nuevo precio por hora: "))
        nuevo_tipo_curso = input("Ingrese el nuevo tipo de curso: ")

        # Consulta SQL para actualizar un registro
        query = """
        UPDATE cursos
        SET NombreCurso = ?, Descripcion = ?, PrecioxHora = ?, TipoCurso = ?
        WHERE IDCurso = ?
        """
        cursor.execute(query, (nuevo_curso, nueva_descripcion, nuevo_precio, nuevo_tipo_curso, id_curso))
        conexion.commit()  # Confirmar los cambios

    except Exception as e:
        print("\nOcurrió un error al actualizar los registros: ", e)

# Función consultar registros
def consultar_registros(conexion):
    """
    Consulta y muestra todos los registros en la tabla 'cursos'.
    """
    try:
        cursor = conexion.cursor()
        print("\n\tConsulta de registros:\n")

        # Consulta SQL para seleccionar registros
        query = "SELECT IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso FROM cursos"
        cursor.execute(query)
        rows = cursor.fetchall()  # Obtener todos los registros

        # Imprimir los registros
        for row in rows:
            print(f"ID: {row.IDCurso}, Nombre: {row.NombreCurso}, "
                  f"Descripción: {row.Descripcion}, Precio/Hora: {row.PrecioxHora}, Tipo: {row.TipoCurso}")
    except Exception as e:
        print("\nOcurrió un error al consultar los registros: ", e)

# Función para mostrar opciones CRUD
def mostrar_opciones_crud():
    """
    Muestra el menú de opciones para realizar operaciones CRUD.
    """
    print("\t**")  
    print("\t** SISTEMA CRUD UDEMYTEST **")  
    print("\t**")  
    print("\tOpciones CRUD:\n")
    print("\t1. Crear registro")
    print("\t2. Consultar registros")
    print("\t3. Actualizar registro")
    print("\t4. Eliminar registro")
    print("\t5. Salir\n\n")

# Establecer la conexión
try:
    conexion = pyodbc.connect(connection_string)  # Conectar a la base de datos
    print("Conexión exitosa.\n")
except Exception as e:
    print("\nOcurrió un error al conectar a SQL Server: ", e)
else:
    # Ciclo para mostrar el menú y ejecutar operaciones
    while True:
        mostrar_opciones_crud()
        opcion = input("Seleccione una opción 1-5:\t")
        
        if opcion == '1':
            insertar_registro(conexion)
        elif opcion == '2':
            consultar_registros(conexion)
        elif opcion == '3':
            actualizar_registro(conexion)
        elif opcion == '4':
            eliminar_registro(conexion)
        elif opcion == '5':
            print("Saliendo del programa...\n")
            break
        else:
            print("Opción no válida.")
finally:
    # Cerrar la conexión si está activa
    if 'conexion' in locals() and conexion:
        conexion.close()
        print("Conexión cerrada.")