import requests
import pandas as pd
from datetime import datetime, timedelta

# Datas
end_date = datetime.today().date()
start_date = end_date - timedelta(days=7)

print(f"Buscando cotação USD/BRL de {start_date} até {end_date}...")

# AwesomeAPI devolve os últimos 7 registros em ordem decrescente
url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/7"

r = requests.get(url)
data = r.json()

# Processar para DataFrame
rows = []
for item in data:
    rows.append({
        "date": datetime.fromtimestamp(int(item["timestamp"])).date(),
        "bid": float(item["bid"]),   # valor de compra
        "ask": float(item["ask"]),   # valor de venda
        "high": float(item["high"]), # máxima do dia
        "low": float(item["low"])    # mínima do dia
    })

df = pd.DataFrame(rows)

# A API devolve em ordem decrescente, vamos ordenar por data
df = df.sort_values("date").reset_index(drop=True)

df.to_csv("usd_brl_ultima_semana.csv", index=False)
print("Arquivo salvo: usd_brl_ultima_semana.csv")
