"""
Componente encargado de subir radiografías.
"""

import streamlit as st
from PIL import Image
from frontend.services.api_client import analizar_imagen
from frontend.components.result_panel import render_result


def render_uploader():
    """
    Renderiza el cargador de radiografías.
    """

    archivo = st.file_uploader(
        "Sube una radiografía",
        type=["png", "jpg", "jpeg"]
    )

    if archivo:

        imagen = Image.open(archivo)

        col1, col2 = st.columns([2, 1])

        with col1:

            st.image(imagen, use_column_width=True)

        with col2:

            if st.button("Analizar radiografía"):

                resultado = analizar_imagen(
                    archivo.getvalue()
                )

                render_result(resultado)