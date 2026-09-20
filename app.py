import streamlit as st
import joblib


# Nombres de los ODS
ODS_NOMBRES = {
    1: "Fin de la pobreza",
    2: "Hambre cero",
    3: "Salud y bienestar",
    4: "Educación de calidad",
    5: "Igualdad de género",
    6: "Agua limpia y saneamiento",
    7: "Energía asequible y no contaminante",
    8: "Trabajo decente y crecimiento económico",
    9: "Industria, innovación e infraestructura",
    10: "Reducción de las desigualdades",
    11: "Ciudades y comunidades sostenibles",
    12: "Producción y consumo responsables",
    13: "Acción por el clima",
    14: "Vida submarina",
    15: "Vida de ecosistemas terrestres",
    16: "Paz, justicia e instituciones sólidas"
}


# Cargar modelo
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_ods.joblib")


modelo = cargar_modelo()


# Configuración de la página
st.set_page_config(
    page_title="Clasificador de ODS",
    page_icon="🌎",
    layout="centered"
)


# Título
st.title("🌎 Clasificador de Objetivos de Desarrollo Sostenible")

st.write(
    """
    Esta aplicación utiliza un modelo de Machine Learning
    para clasificar un texto según el Objetivo de Desarrollo
    Sostenible (ODS) con el que presenta mayor relación.
    """
)

st.divider()


# Entrada del usuario
texto = st.text_area(
    "Ingrese el texto que desea clasificar:",
    height=200,
    placeholder="Escriba aquí el texto..."
)


# Botón
if st.button("🔍 Clasificar texto"):

    if not texto.strip():

        st.warning("Por favor, ingrese un texto.")

    else:

        # Realizar predicción
        prediccion = modelo.predict([texto])

        ods = int(prediccion[0])

        nombre_ods = ODS_NOMBRES.get(
            ods,
            "ODS no disponible"
        )

        # Mostrar resultado
        st.success(f"Predicción: ODS {ods}")

        st.subheader(nombre_ods)