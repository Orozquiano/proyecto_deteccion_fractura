"""
Componente visual del resultado del modelo.
"""

import streamlit as st


def render_result(resultado):
    """
    Muestra el resultado del análisis.
    """

    prediccion = resultado["resultado"]
    confianza = resultado["confianza"]

    if "fractura" in prediccion:

        st.error("⚠ Posible fractura detectada")

    else:

        st.success("✅ No se detectó fractura")

    st.progress(confianza)

    st.metric(
        "Confianza del modelo",
        f"{confianza*100:.2f}%"
    )