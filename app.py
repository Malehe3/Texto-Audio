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

# Recetas predefinidas
recetas = {
    "Tacos de Pollo Mexicano": {
        "Descripción": "Deliciosos tacos de pollo con un toque mexicano.",
        "Ingredientes": "- Pollo desmenuzado\n- Tortillas de maíz\n- Cebolla\n- Tomate\n- Aguacate\n- Cilantro\n- Limón\n- Salsa de tomate\n- Especias mexicanas",
        "Instrucciones": "1. Saltear el pollo con las especias.\n2. Calentar las tortillas.\n3. Servir con los ingredientes frescos y salsa."
    },
    "Espaguetis a la Boloñesa": {
        "Descripción": "Clásicos espaguetis con una deliciosa salsa de carne italiana.",
        "Ingredientes": "- Espaguetis\n- Carne molida\n- Cebolla\n- Ajo\n- Zanahoria\n- Salsa de tomate\n- Vino tinto\n- Aceite de oliva\n- Especias italianas",
        "Instrucciones": "1. Cocinar la carne con las verduras.\n2. Agregar la salsa de tomate y el vino.\n3. Cocinar a fuego lento.\n4. Servir sobre los espaguetis."
    },
    "Salmón al Horno con Verduras": {
        "Descripción": "Salmón fresco horneado con una variedad de verduras sazonadas.",
        "Ingredientes": "- Filetes de salmón\n- Brócoli\n- Zanahorias\n- Calabacín\n- Limón\n- Aceite de oliva\n- Sal\n- Pimienta\n- Hierbas aromáticas",
        "Instrucciones": "1. Colocar el salmón y las verduras en una bandeja.\n2. Rociar con aceite de oliva y especias.\n3. Hornear hasta que estén dorados y tiernos."
    }
}

# Opción para seleccionar una receta predefinida
selected_recipe = st.selectbox("Selecciona una receta predefinida", list(recetas.keys()))

# Mostrar la receta completa una vez seleccionada
if st.button("Ver Receta"):
    st.subheader(selected_recipe)
    st.write(f"**Descripción:** {recetas[selected_recipe]['Descripción']}")
    st.write(f"**Ingredientes:** {recetas[selected_recipe]['Ingredientes']}")
    st.write(f"**Instrucciones:** {recetas[selected_recipe]['Instrucciones']}")

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
