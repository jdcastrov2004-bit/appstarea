import streamlit as st
from PIL import Image

st.set_page_config(page_title="Suite de Interfaces Multimodales", page_icon="🎛️", layout="wide")

st.title("🎛️ Suite de Interfaces Multimodales")
st.caption("Explora aplicaciones interactivas desarrolladas con inteligencia artificial multimodal: voz, texto, visión y datos.")

with st.sidebar:
    st.subheader("💡 Sobre esta suite")
    st.write(
        "Esta colección reúne diferentes aplicaciones diseñadas para experimentar con IA multimodal: "
        "reconocimiento de voz, texto, imágenes, análisis de datos y más. "
        "Cada módulo ilustra una capacidad distinta de la inteligencia artificial aplicada."
    )

st.markdown("---")

# --- Columnas principales ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧠 Introducción General")
    st.image(Image.open("luciernaga.jpg"), width=250)
    st.write("Presentación e introducción al entorno de aplicaciones.")
    st.write("[Abrir](https://introjuanda.streamlit.app)")

    st.subheader("🎙️ Interfaz Voz → Texto")
    st.image(Image.open("traductor.jpg"), width=250)
    st.write("Convierte tu voz en texto con reconocimiento automático de habla.")
    st.write("[Abrir](https://interfazvoztextojuanda.streamlit.app)")

    st.subheader("🔊 Interfaz Texto → Voz")
    st.image(Image.open("luciernaga.jpg"), width=250)
    st.write("Transforma texto en audio natural en diferentes idiomas.")
    st.write("[Abrir](https://interfaztextovozjuanda.streamlit.app)")

    st.subheader("🧭 Detección de Objetos")
    st.image(Image.open("deteccion.jpg"), width=250)
    st.write("Detecta y clasifica objetos dentro de una imagen usando YOLOv5.")
    st.write("[Abrir](https://reconocimientodeobjetosenimagenesjuanda.streamlit.app)")

with col2:
    st.subheader("🖼️ Imagen → Texto (OCR)")
    st.image(Image.open("lupa.jpg"), width=250)
    st.write("Extrae texto desde fotografías o imágenes escaneadas.")
    st.write("[Abrir](https://imagentextoocrjuanda.streamlit.app)")

    st.subheader("🔊 Imagen → Texto + Audio")
    st.image(Image.open("inspector.jpg"), width=250)
    st.write("Lee una imagen, interpreta su contenido y lo convierte en audio.")
    st.write("[Abrir](https://imagentextoaudiojuanda.streamlit.app)")

    st.subheader("🔎 Análisis TF-IDF (Inglés)")
    st.image(Image.open("lectora.jpg"), width=250)
    st.write("Calcula similitud entre textos en inglés usando TF-IDF.")
    st.write("[Abrir](https://textoinglesjuanda.streamlit.app)")

    st.subheader("🔎 Análisis TF-IDF (Español)")
    st.image(Image.open("lectora.jpg"), width=250)
    st.write("Encuentra el documento más relevante a partir de tu pregunta en español.")
    st.write("[Abrir](https://textoespanoljuanda.streamlit.app)")

with col3:
    st.subheader("🖐️ Reconocimiento de Gestos")
    st.image(Image.open("gestos.jpg"), width=250)
    st.write("Clasifica movimientos de mano en tiempo real con un modelo entrenado.")
    st.write("[Abrir](https://reconocimientodegestosjuanda.streamlit.app)")

    st.subheader("🧠 Interpretación de Imágenes (GPT-4o)")
    st.image(Image.open("images.jpeg"), width=250)
    st.write("Analiza y describe imágenes con inteligencia visual avanzada.")
    st.write("[Abrir](https://interpretaciondeimagenesjuanda.streamlit.app)")

    st.subheader("💬 Chat PDF (RAG)")
    st.image(Image.open("inspector.jpg"), width=250)
    st.write("Haz preguntas a un PDF y recibe respuestas contextualizadas.")
    st.write("[Abrir](https://chatpdfjuanda.streamlit.app)")

    st.subheader("🎨 Tablero Personalizado")
    st.image(Image.open("lectora.jpg"), width=250)
    st.write("Dibuja, usa cuadrículas y exporta tus creaciones.")
    st.write("[Abrir](https://tableropersonalizadojuanda.streamlit.app)")

st.markdown("---")

st.subheader("🎛️ Control por Voz (MQTT)")
st.image(Image.open("traductor.jpg"), width=300)
st.write("Controla sistemas físicos o virtuales por medio de comandos de voz.")
st.write("[Abrir aplicación](https://controlporvozjuanda.streamlit.app)")

st.markdown("---")
st.caption("Desarrollado por Juanda · Suite educativa de interfaces multimodales · 2025")
