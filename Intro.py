import streamlit as st
from PIL import Image

st.set_page_config(page_title="Suite de Interfaces Multimodales", page_icon="🎛️", layout="wide")

st.title("🎛️ Suite de Interfaces Multimodales")
st.caption("Catálogo de tus apps, ordenadas tal como las fuimos personalizando.")

with st.sidebar:
    st.subheader("Acerca del catálogo")
    st.write(
        "Explora interfaces de voz, visión, análisis de texto, RAG, tableros y más. "
        "Haz clic en cualquier tarjeta para abrir la aplicación correspondiente."
    )

# ---- Definición del catálogo (orden exacto) ----
APPS = [
    # 1 → 14
    {"title": "Intro", "emoji": "🎉", "url": "https://introjuanda.streamlit.app", "img": None,
     "blurb": "Bienvenida y presentación general."},

    {"title": "Interfaz Voz → Texto", "emoji": "🎙️➡️📝", "url": "https://interfazvoztextojuanda.streamlit.app", "img": "traductor.jpg",
     "blurb": "Dicta y convierte tu voz en texto."},

    {"title": "Interfaz Texto → Voz", "emoji": "📝➡️🔊", "url": "https://interfaztextovozjuanda.streamlit.app", "img": "luciernaga.jpg",
     "blurb": "Escribe y escucha el audio generado en varios idiomas."},

    {"title": "Imagen → Texto (OCR)", "emoji": "🖼️➡️📝", "url": "https://imagentextoocrjuanda.streamlit.app", "img": "lupa.jpg",
     "blurb": "Extrae texto desde una fotografía con OCR."},

    {"title": "Imagen → Texto + Audio", "emoji": "🖼️➡️📝🔊", "url": "https://imagentextoaudiojuanda.streamlit.app", "img": "inspector.jpg",
     "blurb": "Convierte lo detectado en la imagen a voz."},

    {"title": "TF-IDF en Inglés", "emoji": "🔎🇬🇧", "url": "https://textoinglesjuanda.streamlit.app", "img": "lectora.jpg",
     "blurb": "Encuentra el documento más relevante a tu pregunta (inglés)."},

    {"title": "TF-IDF en Español", "emoji": "🔎🇪🇸", "url": "https://textoespanoljuanda.streamlit.app", "img": "lectora.jpg",
     "blurb": "Análisis de similitud entre textos en español."},

    {"title": "Reconocimiento de Gestos", "emoji": "✋🤖", "url": "https://reconocimientodegestosjuanda.streamlit.app", "img": "gestos.jpg",
     "blurb": "Clasifica gestos con un modelo de Teachable Machine."},

    {"title": "Objetos en Imágenes (YOLOv5)", "emoji": "🧭🖼️", "url": "https://reconocimientodeobjetosenimagenesjuanda.streamlit.app", "img": "deteccion.jpg",
     "blurb": "Detecta objetos en una foto y resume resultados."},

    {"title": "Interpretación de Imágenes (GPT-4o)", "emoji": "🧠🖼️", "url": "https://interpretaciondeimagenesjuanda.streamlit.app", "img": "images.jpeg",
     "blurb": "Describe y analiza imágenes con IA multimodal."},

    {"title": "Chat PDF (RAG)", "emoji": "💬📄", "url": "https://chatpdfjuanda.streamlit.app", "img": None,
     "blurb": "Haz preguntas a tus PDFs con recuperación semántica."},

    {"title": "Tablero Personalizado", "emoji": "🎨", "url": "https://tableropersonalizadojuanda.streamlit.app", "img": None,
     "blurb": "Dibuja, usa cuadrícula y exporta PNG/JSON."},

    {"title": "Control por Voz (MQTT)", "emoji": "🎛️🎙️", "url": "https://controlporvozjuanda.streamlit.app", "img": "traductor.jpg",
     "blurb": "Publica comandos por voz a un broker MQTT."},

    {"title": "AppsJuanda (Meta-app)", "emoji": "🗂️", "url": "https://appsjuanda.streamlit.app", "img": None,
     "blurb": "Contenedor con enlaces a la colección completa."},
]

# ---- Helper para tarjeta tipo catálogo ----
def card(title, emoji, blurb, url, img_path=None):
    with st.container():
        st.markdown(
            f"""
            <div style="border:1px solid rgba(255,255,255,0.1); border-radius:16px; padding:14px; margin-bottom:16px;">
              <div style="display:flex; gap:14px; align-items:center;">
                <div style="width:120px; min-width:120px;">
            """,
            unsafe_allow_html=True,
        )
        # Miniatura (si existe)
        if img_path:
            try:
                st.image(Image.open(img_path), use_container_width=True)
            except Exception:
                st.image(Image.new("RGB", (640, 400), color=(20, 20, 20)), caption="(imagen no encontrada)", use_container_width=True)
        else:
            st.image(Image.new("RGB", (640, 400), color=(20, 20, 20)), caption="(sin miniatura)", use_container_width=True)

        st.markdown(
            f"""
                </div>
                <div style="flex:1;">
                  <h4 style="margin:0;">{emoji} {title}</h4>
                  <p style="margin-top:6px; opacity:0.9;">{blurb}</p>
            """,
            unsafe_allow_html=True,
        )
        # Botón/link
        try:
            st.link_button("Abrir aplicación", url)
        except Exception:
            st.write(f"[Abrir aplicación]({url})")

        st.markdown(
            """
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---- Render en 2 columnas (catálogo) ----
left, right = st.columns(2)
for i, app in enumerate(APPS):
    (left if i % 2 == 0 else right).write(card(app["title"], app["emoji"], app["blurb"], app["url"], app["img"]))
