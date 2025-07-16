import subprocess
import yaml
import os

# Cargar configuración desde el archivo YAML
def cargar_configuracion():
    with open('conexion.yml', 'r') as archivo_yaml:
        config = yaml.safe_load(archivo_yaml)
    return config

# Restaurar el respaldo desde un archivo .sql
def restaurar_respaldo(config, archivo_sql):
    # Obtener configuración de la base de datos
    usuario = config['user']
    contrasena = config['pass']
    base_de_datos = config['database']
    host = config['host']
    puerto = config['port']

    # Ruta completa al ejecutable mysql
    mysql_path = r'C:\Program Files\MariaDB 11.8\bin\mysql.exe'

    # Comando para ejecutar mysql y restaurar
    comando = [
        mysql_path,
        f"--user={usuario}",
        f"--password={contrasena}",
        f"--host={host}",
        f"--port={puerto}",
        base_de_datos
    ]

    # Verifica que el archivo existe
    if not os.path.exists(archivo_sql):
        print(f"El archivo '{archivo_sql}' no existe.")
        return

    # Ejecutar el comando y alimentar la entrada con el contenido del archivo .sql
    with open(archivo_sql, 'r', encoding='utf-8') as archivo_entrada:
        subprocess.run(comando, stdin=archivo_entrada, shell=False)

    print(f"Restauración completada desde: {archivo_sql}")

if __name__ == "__main__":
    config = cargar_configuracion()
    
    # Cambia aquí por la ruta real al archivo SQL que quieras restaurar
    ruta_respaldo = r'C:\ruta\a\tu\respaldo.sql'
    restaurar_respaldo(config, ruta_respaldo)
