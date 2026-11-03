import requests
import os
import json

parametros = {
	"latitude": -26.4861,
	"longitude": -49.0667,
	"hourly": "temperature_2m",
    "hourly": "umidade_relativa_2m",
    "hourly": "apparent_temperature",
    "hourly": "precipitation",
    "hourly": "wind_speed_10m",
    "hourly": "time"
}
url = "https://api.open-meteo.com/v1/forecast"

resposta = requests.get(
    url,
    params=parametros,
    timeout=15
)

if resposta.status_code(200):
    dados = resposta.json()
    temp_ar = ["current"]["temperatura_2m"],
    umidade = ["Umidade Relativa"]["umidade_relativa_2m"],
    sensacao = ["Sensação Térmica"]["apparent_temperature"],
    precipitacao = ["Precipitação"]["precipitation"],
    vel_vento = ["Velocidade do Vento"]["wind_speed_10m"],
    horario = ["Horário da Medição"]["time"]

print("A temperatura do ar é de:",temp_ar)
print("A umidade é de:",umidade)
print("A sensação é de:",sensacao)
print("A precipitação é de:",precipitacao)
print("A velocidade do vento é de:",vel_vento)
print("Horário da medição:",horario)