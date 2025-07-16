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

    # Crear nombre de archivo con fecha
    fecha_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    archivo_respaldo = os.path.join(carpeta_respaldo, f'backup_incremental_{fecha_actual}.sql')

    # Comando mysqldump para el respaldo incremental
    comando = [
        'mysqldump',
        f'--user={usuario}',
        f'--password={contrasena}',
        f'--host={host}',
        f'--port={puerto}',
        '--single-transaction',
        '--flush-logs',  # Para hacer respaldo incremental
        '--master-data=2',  # Incluye información de binlog (es necesario para la replicación)
        base_de_datos
    ]

    # Ejecutar el comando mysqldump
    with open(archivo_respaldo, 'w') as archivo:
        resultado = subprocess.run(comando, stdout=archivo, stderr=subprocess.PIPE)

    if resultado.returncode != 0:
        print("Error al realizar el respaldo:", resultado.stderr.decode())
    else:
        print(f"Respaldo exitoso guardado en: {archivo_respaldo}")

# Ejecutar el respaldo
def ejecutar_respaldo():
    config = cargar_configuracion()
    realizar_respaldo(config)

if __name__ == '__main__':
    ejecutar_respaldo()
