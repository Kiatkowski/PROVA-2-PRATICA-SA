import requests
import os
import json


url = "https://api.open-meteo.com/v1/forecast"

parametros = {
	"latitude": -26.4861,
	"longitude": -49.0667,
	"hourly": ["temperature_2m","umidade_relativa_2m","apparent_temperature","precipitation","wind_speed_10m","time"]
}

resposta = requests.get(
    url,
    params=parametros,
    timeout=15
)

if resposta.status_code == 200:
    dados = resposta.json()
    dados_horarios = dados["hourly"]
    temp_ar = [dados_horarios]["temperatura_2m"],
    umidade = [dados_horarios]["umidade_relativa_2m"],
    sensacao = [dados_horarios]["apparent_temperature"],
    precipitacao = [dados_horarios]["precipitation"],
    vel_vento = [dados_horarios]["wind_speed_10m"],
    horario = [dados_horarios]["time"]

print("A temperatura do ar é de:",temp_ar)
print("A umidade é de:",umidade)
print("A sensação é de:",sensacao)
print("A precipitação é de:",precipitacao)
print("A velocidade do vento é de:",vel_vento)
print("Horário da medição:",horario)