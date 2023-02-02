from pandas_datareader import data as pdr
from Functions.logs import print_log
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import configparser

yf.pdr_override()
plt.ioff()
config = configparser.ConfigParser()
config.read('Config\Config\config.conf')
path_save_grafic = config['PATHS']['ruta_guardar_grafico_imagen']

def get_data(tickers,fecha_inicio,fecha_fin):
    print_log('INFO','Inicio función: get_data')
    print_log('INFO','Pasa a iterar la lista de Acciones para obtener los datos')
    for accion in tickers:
        print_log('INFO',f'Itera la acción {accion} y pasa a obtener la tabla con la información')
        data = pdr.get_data_yahoo(accion, fecha_inicio, fecha_fin)
        print_log('INFO',f'Pasa a tomar unicamente la columna "Adj Close"')
        data = get_columns_dataframe(data)
        print_log('INFO','Pasa a obtener la media movil de 10 dias')
        data = get_media_movil(data,'10')
        print_log('INFO','Pasa a obtener la media movil de 20 dias')
        data = get_media_movil(data,'20')
        print_log('INFO','Pasa a generar y guardar el gráfico.')
        print_log('INFO',f'Tomó la información correctamente: {data}')
        generate_and_save_grafic(data, accion)
        print_log('INFO','Fin función: get_data')
    return data

def get_columns_dataframe(dataframe):
    print_log('INFO','Inicio función: get_columns_dataframe')
    dataframe = dataframe[['Adj Close']]
    print_log('INFO','Fin función: get_columns_dataframe')
    return dataframe

def get_media_movil(data,cant_dias):
    print_log('INFO','Inicio función: get_media_movil')
    print_log('INFO',f'Pasa a obtener la media movil de {cant_dias} días del precio de cierre.')
    int_day = int(cant_dias)
    data[f'M{cant_dias}'] = data['Adj Close'].rolling(int_day, min_periods=1).mean()
    print_log('INFO','Fin función: get_media_movil')
    return data

def generate_and_save_grafic(data,accion):
    print_log('INFO','Inicio función: generate_and_save_grafic')
    #Generar grafico
    print_log('INFO','Genera el gráfico')
    data.plot()
    #Guardar grafico
    print_log('INFO','Guarda el gráfico')
    print(f'{path_save_grafic}{accion}.png')
    plt.savefig(f'{path_save_grafic}{accion}.png')
    print_log('INFO','Fins función: generate_and_save_grafic')