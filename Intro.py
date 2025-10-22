import streamlit as st
from PIL import Image

st.set_page_config(page_title="Suite de Interfaces Multimodales", page_icon="🎛️", layout="wide")

st.title("🎛️ Suite de Interfaces Multimodales")
st.caption("Explora aplicaciones interactivas: voz, texto, visión, TF-IDF, RAG y más.")

with st.sidebar:
    st.subheader("💡 Sobre esta suite")
    st.write(
        "Colección de apps multimodales (voz, texto, visión y datos). "
        "Cada tarjeta incluye una breve descripción y un enlace directo."
    )

st.markdown("---")

# (título, imagen, descripción, enlace) — ORDEN IZQ→DER, 3 por fila
APPS = [
    ("🧠 Introducción General", "travis.jpeg",
     "Presentación e introducción al entorno de aplicaciones.",
     "https://introjuanda.streamlit.app"),

    ("🎙️ Interfaz Voz → Texto", "traductor.jpg",
     "Convierte tu voz en texto con reconocimiento automático de habla.",
     "https://interfazvoztextojuanda.streamlit.app"),

    ("🔊 Interfaz Texto → Voz", "luciernaga.jpg",
     "Transforma texto en audio natural en diferentes idiomas.",
     "https://interfaztextovozjuanda.streamlit.app"),

    ("🖼️ Imagen → Texto (OCR)", "lupa.jpg",
     "Extrae texto desde fotografías o imágenes escaneadas.",
     "https://imagentextoocrjuanda.streamlit.app"),

    ("🖼️→📝🔊 Imagen → Texto + Audio", "inspector.jpg",
     "Lee una imagen, interpreta su contenido y lo convierte en audio.",
     "https://imagentextoaudiojuanda.streamlit.app"),

    ("🔎 TF-IDF (Inglés)", "lectora.jpg",
     "Calcula similitud entre textos en inglés usando TF-IDF.",
     "https://textoinglesjuanda.streamlit.app"),

    ("🔎 TF-IDF (Español)", "lectora.jpg",
     "Encuentra el documento más relevante a partir de tu pregunta en español.",
     "https://textoespanoljuanda.streamlit.app"),

    ("🖐️ Reconocimiento de Gestos", "gestos.jpg",
     "Clasifica movimientos de mano en tiempo real con un modelo entrenado.",
     "https://reconocimientodegestosjuanda.streamlit.app"),

    ("🧭 Detección de Objetos (YOLOv5)", "deteccion.jpg",
     "Detecta y clasifica objetos dentro de una imagen.",
     "https://reconocimientodeobjetosenimagenesjuanda.streamlit.app"),

    ("🧠 Interpretación de Imágenes (GPT-4o)", "images.jpeg",
     "Analiza y describe imágenes con IA multimodal.",
     "https://interpretaciondeimagenesjuanda.streamlit.app"),

    ("💬 Chat PDF (RAG)", "chatpdf.jpg",
     "Haz preguntas a un PDF y recibe respuestas contextualizadas.",
     "https://chatpdfjuanda.streamlit.app"),

    ("🎨 Tablero Personalizado", "tablero.jpg",
     "Dibuja, usa cuadrículas y exporta tus creaciones.",
     "https://tableropersonalizadojuanda.streamlit.app"),

    ("🎛️ Control por Voz (MQTT)", "controlporvoz.jpg",
     "Publica comandos por voz hacia un broker MQTT.",
     "https://controlporvozjuanda.streamlit.app"),

    ("🗂️ AppsJuanda (meta-app)", None,
     "Contenedor general con enlaces a la colección completa.",
     "https://appsjuanda.streamlit.app"),
]

# Tarjeta simple
def render_card(title, img_name, desc, url):
    st.markdown(f"### {title}")
    if img_name:
        try:
            st.image(Image.open(img_name), use_column_width=True)
        except Exception:
            st.warning(f"No se pudo cargar la imagen: {img_name}")
    st.write(desc)
    st.markdown(f"[Abrir]({url})")

# Mostrar en filas de 3 (izq→der)
for i in range(0, len(APPS), 3):
    cols = st.columns(3)
    for col, app in zip(cols, APPS[i:i+3]):
        with col:
            render_card(*app)

st.markdown("---")
st.caption("Desarrollado por Juanda · Suite educativa de interfaces multimodales · 2025")
