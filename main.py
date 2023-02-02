from Functions.calcular_media_movil import *
from Functions.logs import print_log

acciones = ['META']
inicio = '2023-01-01'
fin = '2023-02-01'
tipo_log_exception= 'EXCEPTION'
tipo_log_info= 'INFO'

def main():
    try:
        print_log('INFO','Inicio función: main')
        get_data(acciones,inicio,fin)
        print_log('INFO','Fin función: main')
    except Exception as error:
        print_log(tipo_log_exception,f'No se pudo avanzar con el bot debido a la siguiente excepción: {error}')
main()

