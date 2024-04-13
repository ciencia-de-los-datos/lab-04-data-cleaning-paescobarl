"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
from datetime import datetime

import re
import pandas as pd


def clean_data():

    resultado = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    resultado = resultado.copy()

    resultado.dropna(inplace=True) 

    resultado["sexo"] = resultado["sexo"].str.lower()

    resultado["tipo_de_emprendimiento"] = resultado["tipo_de_emprendimiento"].str.lower()

    resultado["idea_negocio"] = [
        str.lower(idea.replace("_", " ").replace("-", " "))
        for idea in resultado["idea_negocio"]
    ]

    resultado.barrio = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in resultado.barrio
    ]

    resultado["barrio"] = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in resultado["barrio"]
    ]


    resultado["comuna_ciudadano"] = resultado["comuna_ciudadano"].astype(int)

    resultado["estrato"] = resultado["estrato"].astype(int)

    resultado["línea_credito"] = [
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in resultado["línea_credito"]
    ]
    resultado["línea_credito"] = resultado["línea_credito"].str.lower().str.strip() 

    resultado["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in resultado["fecha_de_beneficio"]
    ]

    resultado["monto_del_credito"] = [
        int(monto.replace("$ ", "").replace(".00", "").replace(",", ""))
        for monto in resultado["monto_del_credito"]
    ]
    resultado["monto_del_credito"] = resultado["monto_del_credito"].astype(int)  ##
    resultado.drop_duplicates(inplace=True)

    return resultado

