import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image

st.title("CocinaFacil - Tu Asistente de Cocina Personalizado")

image = Image.open('Gatitochef2.jpg')
st.image(image, width=200, caption='Ya no serás este:')

try:
    os.mkdir("temp")
except:
    pass


# Mensaje de bienvenida
st.write("¡Bienvenido a CocinaFacil con ChefIA, tu asistente de cocina personal! Quien te narrará las recetas para que puedas concentrarte en cocinar sin preocupaciones de posibles accidentes y disfrutar al máximo de tus creaciones culinarias.")

# Función para convertir texto a audio
def text_to_speech(text, tld):
    tts = gTTS(text, "es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text

# Opción para ingresar texto o seleccionar una receta predefinida
option = st.radio("¿Cómo prefieres obtener la receta?", ("Escribir la receta", "Seleccionar receta predefinida"))

# Si elige escribir la receta
if option == "Escribir la receta":
    text = st.text_area("Escribe la receta aquí")
else:
    # Lista de recetas predefinidas
    recetas_predefinidas = ["Receta 1", "Receta 2", "Receta 3"]
    selected_recipe = st.selectbox("Selecciona una receta predefinida", recetas_predefinidas)
    text = selected_recipe

# Botón para convertir texto a audio
if st.button("Convertir texto a audio"):
    result, output_text = text_to_speech(text, "es")
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)

remove_files(7)

