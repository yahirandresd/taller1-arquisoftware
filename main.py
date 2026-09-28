import sqlite3
from infraestructura.fecha.fecha_sistema import FechaSistema
from infraestructura.sqlite.sqlite_estudiantes import SQLiteEstudiantes
from infraestructura.memoria.memoria_prestamo import MemoriaPrestamo
from aplicacion.casos_uso.registrar_prestamo import RegistrarPrestamo
from dominio.estudiantes import Estudiantes


def ejecutar_conexion_real():
    # 1, creamos la base de datos real en la memoria del pc
    conexion_db = sqlite3.connect(":memory:")
    cursor = conexion_db.cursor()
    cursor.execute('''
        CREATE TABLE estudiantes (
            id TEXT PRIMARY KEY,
            nombres TEXT,
            apellidos TEXT,
            correo TEXT,
            telefono TEXT,
            prest_activos INTEGER,
            multa_pend INTEGER
        )
    ''')
    #2, instanciamos el adaptador real
    # aunque la variable se llame repo_estudiante, en realidad lleva el codigo de SQLiteEstudiantes
    repositorio_estudiante = SQLiteEstudiantes(conexion_db)

    #3 proba,os la conexion
    print("---probando conexion real del repositorio ---")

    #creamos un estudiante de prueba usando la clase de dominio Estudiantes
    alumno_ejemplo = Estudiantes("777", "Carlos", "Soto", "carlos.soto@univ.edu", "1234567890", 0, False)

    #guardamos 
    repositorio_estudiante.guardarEstudiante(alumno_ejemplo)
    print("Estudiante guardado correctamente en la base de datos.")

    #buscamos el estudiante por su ID
    alumno_recuperado = repositorio_estudiante.buscarEstudianteporId("777")
    if alumno_recuperado:
        print(f"Estudiante recuperado: {alumno_recuperado.nombres} {alumno_recuperado.apellidos}, Correo: {alumno_recuperado.correo}")

    conexion_db.close()



if __name__ == "__main__":
    ejecutar_conexion_real()