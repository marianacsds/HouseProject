import requests
import pandas as pd
from datetime import datetime, timedelta

# São Paulo coordenadas
LAT, LON = -23.55, -46.63
TZ = "America/Sao_Paulo"

# Datas
end_date = datetime.today().date()
start_date = end_date - timedelta(days=7)

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": LAT,
    "longitude": LON,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": TZ
}

print(f"Buscando dados de {start_date} até {end_date}...")
r = requests.get(url, params=params)
data = r.json()

df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temp_max": data["daily"]["temperature_2m_max"],
    "temp_min": data["daily"]["temperature_2m_min"]
})

df.to_csv("clima_ultima_semana.csv", index=False)
print("Arquivo salvo: clima_ultima_semana.csv")
