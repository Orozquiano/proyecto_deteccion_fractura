"""
Componente visual del encabezado.
"""

import streamlit as st


def render_header():
    """
    Muestra el encabezado principal.
    """

    st.title("🦴 Sistema Inteligente de Detección de Fracturas")

    st.markdown(
        """
        Analiza radiografías médicas usando **Inteligencia Artificial**
        para detectar posibles fracturas óseas.
        """
    )

    st.divider()