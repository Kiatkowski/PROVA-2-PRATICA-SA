import streamlit as st
import consumidor_api

st.set_page_config(page_title="Estação Meteorológica", page_icon="🌡️")

st.title("Estação Meteorológica")
st.write("Monitoramento de condições ambientais")

try:
    dados = consumidor_api()

    st.subheader("Temperatura")
    st.metric("Temperatura do ar", f"{dados['temperatura']:.1f} °C")
    st.metric("Sensação térmica", f"{dados['sensacao_termica']:.1f} °C")

    st.divider()

    st.subheader("Umidade e precipitação")
    st.metric("Umidade relativa", f"{dados['umidade_relativa']:.0f} %")
    st.metric("Precipitação", f"{dados['precipitacao']:.1f} mm")

    st.divider()

    st.subheader("Vento")
    st.metric("Velocidade", f"{dados['velocidade_vento']:.1f} km/h")

    st.caption(f"Horário da consulta: {dados['horario']}")

except Exception as erro:
    st.error(f"Falha na consulta meteorológica: {erro}")