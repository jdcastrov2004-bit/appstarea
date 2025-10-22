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

# --- Datos de las apps ---
apps = [
    ("🧠 Introducción General", "luciernaga.jpg", "Presentación e introducción al entorno de aplicaciones.", "https://introjuanda.streamlit.app"),
    ("🎙️ Interfaz Voz → Texto", "traductor.jpg", "Convierte tu voz en texto con reconocimiento automático de habla.", "https://interfazvoztextojuanda.streamlit.app"),
    ("🔊 Interfaz Texto → Voz", "luciernaga.jpg", "Transforma texto en audio natural en diferentes idiomas.", "https://interfaztextovozjuanda.streamlit.app"),
    ("🖼️ Imagen → Texto (OCR)", "lupa.jpg", "Extrae texto desde fotografías o imágenes escaneadas.", "https://imagentextoocrjuanda.streamlit.app"),
    ("🔊 Imagen → Texto + Audio", "inspector.jpg", "Lee una imagen, interpreta su contenido y lo convierte en audio.", "https://imagentextoaudiojuanda.streamlit.app"),
    ("🔎 Análisis TF-IDF (Inglés)", "lectora.jpg", "Calcula similitud entre textos en inglés usando TF-IDF.", "https://textoinglesjuanda.streamlit.app"),
    ("🔎 Análisis TF-IDF (Español)", "lectora.jpg", "Encuentra el documento más relevante a partir de tu pregunta en español.", "https://textoespanoljuanda.streamlit.app"),
    ("🖐️ Reconocimiento de Gestos", "gestos.jpg", "Clasifica movimientos de mano en tiempo real con un modelo entrenado.", "https://reconocimientodegestosjuanda.streamlit.app"),
    ("🧭 Detección de Objetos", "deteccion.jpg", "Detecta y clasifica objetos dentro de una imagen usando YOLOv5.", "https://reconocimientodeobjetosenimagenesjuanda.streamlit.app"),
    ("🧠 Interpretación de Imágenes (GPT-4o)", "images.jpeg", "Analiza y describe imágenes con inteligencia visual avanzada.", "https://interpretaciondeimagenesjuanda.streamlit.app"),
    ("💬 Chat PDF (RAG)", "inspector.jpg", "Haz preguntas a un PDF y recibe respuestas contextualizadas.", "https://chatpdfjuanda.streamlit.app"),
    ("🎨 Tablero Personalizado", "lectora.jpg", "Dibuja, usa cuadrículas y exporta tus creaciones.", "https://tableropersonalizadojuanda.streamlit.app"),
    ("🎛️ Control por Voz (MQTT)", "traductor.jpg", "Controla sistemas físicos o virtuales por medio de comandos de voz.", "https://controlporvozjuanda.streamlit.app"),
]

# --- Mostrar en filas de 3 ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for col, (titulo, imagen, descripcion, enlace) in zip(cols, apps[i:i+3]):
        with col:
            st.markdown(f"### {titulo}")
            try:
                img = Image.open(imagen)
                st.image(img, use_container_width=True)
            except Exception:
                st.warning(f"No se pudo cargar la imagen: {imagen}")
            st.write(descripcion)
            st.markdown(f"[Abrir]({enlace})")

st.markdown("---")
st.caption("Desarrollado por Juanda · Suite educativa de interfaces multimodales · 2025")
