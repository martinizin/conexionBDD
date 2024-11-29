import pyodbc
# Declarar variables de Conexión
name_server = 'PCMARTIN'+'\\'+'SQLEXPRESS'  # Nombre del servidor SQL
database = 'UDEMYTEST1'  # Nombre de la base de datos
username = 'pythonconect3'  # Usuario para la conexión
password = 'UDLA'  # Contraseña del usuario
controlador_odbc = 'ODBC Driver 17 for SQL Server'  # Controlador ODBC para SQL Server.

# Crear Cadena de Conexion
connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'

class BaseDatos:
    """
    Clase que encapsula la conexión y las operaciones con la base de datos.
    """
    def __init__(self, connection_string):
        try:
            self.conexion = pyodbc.connect(connection_string)
            print("Conexión exitosa a la base de datos.\n")
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)
            self.conexion = None

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.\n")

    def insertar_curso(self, curso):
        """
        Inserta un nuevo curso en la base de datos.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
            INSERT INTO cursos (IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso)
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (curso.IDCurso, curso.NombreCurso, curso.Descripcion, curso.PrecioxHora, curso.TipoCurso))
            self.conexion.commit()
            print("Curso insertado exitosamente.\n")
        except Exception as e:
            print("Error al insertar el curso: ", e)

    def consultar_cursos(self):
        """
        Consulta y muestra todos los cursos en la base de datos.
        """
        try:
            cursor = self.conexion.cursor()
            query = "SELECT IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso FROM cursos"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(f"ID: {row.IDCurso}, Nombre: {row.NombreCurso}, Descripción: {row.Descripcion}, "
                    f"Precio/Hora: {row.PrecioxHora}, Tipo: {row.TipoCurso}")
        except Exception as e:
            print("Error al consultar los cursos: ", e)

    def actualizar_curso(self, curso):
        """
        Actualiza un curso en la base de datos.
        """
        try:
            cursor = self.conexion.cursor()
            query = """
            UPDATE cursos
            SET NombreCurso = ?, Descripcion = ?, PrecioxHora = ?, TipoCurso = ?
            WHERE IDCurso = ?
            """
            cursor.execute(query, (curso.NombreCurso, curso.Descripcion, curso.PrecioxHora, curso.TipoCurso, curso.IDCurso))
            self.conexion.commit()
            print("Curso actualizado exitosamente.\n")
        except Exception as e:
            print("Error al actualizar el curso: ", e)

    def eliminar_curso(self, id_curso):
        """
        Elimina un curso de la base de datos por ID.
        """
        try:
            cursor = self.conexion.cursor()
            query = "DELETE FROM cursos WHERE IDCurso = ?"
            cursor.execute(query, (id_curso,))
            self.conexion.commit()
            if cursor.rowcount > 0:
                print("Curso eliminado exitosamente.\n")
            else:
                print("No se encontró un curso con ese ID.\n")
        except Exception as e:
            print("Error al eliminar el curso: ", e)


class Curso:
    """
    Clase que representa la tabla  curso.
    """
    def __init__(self, IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso):
        self.IDCurso = IDCurso
        self.NombreCurso = NombreCurso
        self.Descripcion = Descripcion
        self.PrecioxHora = PrecioxHora
        self.TipoCurso = TipoCurso


# Programa principal
def main():
    # Conexión a la base de datos
    connection_string = "tu_connection_string_aqui"
    db = BaseDatos(connection_string)

    while True:
        print("\n** MENÚ CRUD **")
        print("1. Insertar curso")
        print("2. Consultar cursos")
        print("3. Actualizar curso")
        print("4. Eliminar curso")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            IDCurso = input("Ingrese el ID del curso: ")
            NombreCurso = input("Ingrese el nombre del curso: ")
            Descripcion = input("Ingrese la descripción: ")
            PrecioxHora = float(input("Ingrese el precio por hora: "))
            TipoCurso = input("Ingrese el tipo de curso: ")
            curso = Curso(IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso)
            db.insertar_curso(curso)
        elif opcion == '2':
            db.consultar_cursos()
        elif opcion == '3':
            IDCurso = input("Ingrese el ID del curso a actualizar: ")
            NombreCurso = input("Ingrese el nuevo nombre del curso: ")
            Descripcion = input("Ingrese la nueva descripción: ")
            PrecioxHora = float(input("Ingrese el nuevo precio por hora: "))
            TipoCurso = input("Ingrese el nuevo tipo de curso: ")
            curso = Curso(IDCurso, NombreCurso, Descripcion, PrecioxHora, TipoCurso)
            db.actualizar_curso(curso)
        elif opcion == '4':
            IDCurso = input("Ingrese el ID del curso a eliminar: ")
            db.eliminar_curso(IDCurso)
        elif opcion == '5':
            db.cerrar_conexion()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
