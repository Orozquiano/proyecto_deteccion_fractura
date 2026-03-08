"""
Estilos personalizados de la interfaz.
"""

import streamlit as st


def apply_theme():
    """
    Aplica estilos personalizados.
    """

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #0f172a;
            color: white;
        }

        h1 {
            color: #38bdf8;
        }

        </style>
        """,
        unsafe_allow_html=True
    )