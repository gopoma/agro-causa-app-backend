from fastapi import FastAPI
from pydantic import BaseModel
import h5py
import numpy as np

app = FastAPI()

# Modelo de datos de entrada (latitud y longitud)
class Coordenadas(BaseModel):
    latitud: float
    longitud: float

def encontrar_indices_cercanos_fila_columna(cell_lat, cell_lon, latitud_dada, longitud_dada):
    # Extraer la columna 0 de la matriz cell_lat
    columna_lat = cell_lat[:, 0]    
    diferencias_lat = np.abs(columna_lat - latitud_dada)
    indices_filas_cercanas = np.argsort(diferencias_lat)[:1]  # Ordenar y tomar los dos primeros
    

    # Extraer la fila 0 de la matriz cell_lon
    fila_lon = cell_lon[0, :]
    diferencias_lon = np.abs(fila_lon - longitud_dada)
    indices_columnas_cercanas = np.argsort(diferencias_lon)[:1]  # Tomar los dos primeros

    productos_cruzados = np.array(np.meshgrid(indices_filas_cercanas, indices_columnas_cercanas)).T.reshape(-1, 2)

    return productos_cruzados

ruta = "./SMAP_L4_SM_aup_20240926T030000_Vv7031_001.h5"

# Endpoint que recibe latitud y longitud y retorna el valor de la humedad
@app.post("/obtener-humedad/")
async def obtener_humedad(coordenadas: Coordenadas):
    lat = coordenadas.latitud
    long = coordenadas.longitud
    print("PASANDO ASIGNACION ")

    with h5py.File(ruta, 'r') as archivo:
        cell_lat = archivo["//cell_lat"][:] # filas
        cell_lon = archivo["//cell_lon"][:] # columnas

        pares = encontrar_indices_cercanos_fila_columna(cell_lat, cell_lon, lat, long)
        
        rootzone_analysis = archivo["//Analysis_Data/sm_rootzone_analysis"][:]
        hum1 = rootzone_analysis[pares[0][0]][pares[0][1]]

        temp_surface = archivo["//Analysis_Data/surface_temp_analysis"][:]
        tempSuperficial = temp_surface[pares[0][0]][pares[0][1]]

        if tempSuperficial != -9999.0:
            tempSuperficial = tempSuperficial - 273.15

        surface_analysis = archivo["//Analysis_Data/sm_surface_analysis"][:]
        humSuperficial = surface_analysis[pares[0][0]][pares[0][1]]

        print(pares)
        print("Humedad: ", hum1)
        print("Temperatura superficial: ", tempSuperficial)

    return {
        "humedad": float(hum1),
        "temperatura_superficie":float(tempSuperficial),
        "humedad_superficie": float(humSuperficial)
        }