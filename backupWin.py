import subprocess
import yaml
import os
from datetime import datetime

# Cargar configuración desde el archivo YAML
def cargar_configuracion():
    with open('conexion.yml', 'r') as archivo_yaml:
        config = yaml.safe_load(archivo_yaml)
    return config

# Realizar el respaldo incremental
def realizar_respaldo(config):
    # Obtener configuración de la base de datos
    usuario = config['user']
    contrasena = config['pass']
    base_de_datos = config['database']
    host = config['host']
    puerto = config['port']
    carpeta_respaldo = config['backup_dir']

    # Ruta completa al ejecutable mysqldump
    mysqldump_path = r'C:\Program Files\MariaDB 11.8\bin\mysqldump.exe'

    # Crear nombre de archivo con fecha
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{base_de_datos}_{fecha_actual}.sql"
    ruta_completa = os.path.join(carpeta_respaldo, nombre_archivo)

    # Comando para ejecutar mysqldump
    comando = [
        mysqldump_path,
        f"--user={usuario}",
        f"--password={contrasena}",
        f"--host={host}",
        f"--port={puerto}",
        "--routines",  # incluye procedimientos almacenados
        base_de_datos
    ]

    # Ejecutar el comando y guardar salida
    with open(ruta_completa, 'w', encoding='utf-8') as archivo_salida:
        subprocess.run(comando, stdout=archivo_salida, shell=False)

    print(f"Respaldo completado: {ruta_completa}")

if __name__ == "__main__":
    config = cargar_configuracion()
    realizar_respaldo(config)
