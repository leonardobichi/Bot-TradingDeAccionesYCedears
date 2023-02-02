from openpyxl import load_workbook
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('Config\Config\config.conf')
current_date = datetime.now()
path_logs = config['PATHS']['ruta_logs']

def print_log(tipo,info):
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    #Abrir archivo xlsx
    wb = load_workbook(path_logs)
    # Seleccionar la hoja activa
    ws = wb.active
    # Agregar una nueva fila con los datos del log
    ws.append([current_date, tipo, info])
    # Guardar el libro de trabajo
    wb.save(path_logs)
    print(info)