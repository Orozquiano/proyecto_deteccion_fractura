"""
Interfaz principal del frontend.
"""

import sys
from pathlib import Path

# agregar la raíz del proyecto al path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


import streamlit as st

from frontend.styles.theme import apply_theme
from frontend.components.header import render_header
from frontend.components.uploader import render_uploader


def main():
    """
    Construye la interfaz principal.
    """

    st.set_page_config(
        page_title="Detector de Fracturas",
        page_icon="🦴",
        layout="wide"
    )

    apply_theme()

    render_header()

    render_uploader()


if __name__ == "__main__":
    main()