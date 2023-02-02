from openpyxl import load_workbook
from datetime import datetime

current_date = datetime.now()

def print_log(tipo,info):
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    #Abrir archivo xlsx
    wb = load_workbook("C:\\Users\\PC\\Documents\\Desarrollos\\Python\\Bot - Trading de Acciones y Cedears\\logs.xlsx")
    # Seleccionar la hoja activa
    ws = wb.active
    # Agregar una nueva fila con los datos del log
    ws.append([current_date, tipo, info])
    # Guardar el libro de trabajo
    wb.save("C:\\Users\\PC\\Documents\\Desarrollos\\Python\\Bot - Trading de Acciones y Cedears\\logs.xlsx")
    print(info)