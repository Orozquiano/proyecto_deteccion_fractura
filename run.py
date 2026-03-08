"""
Script de arranque del sistema.

Inicia simultáneamente el backend (FastAPI)
y el frontend (Streamlit).
"""

import subprocess


def main():

    print("Iniciando backend...")

    subprocess.Popen(
        ["uv", "run", "uvicorn", "app.main:app", "--reload"]
    )

    print("Iniciando frontend...")

    subprocess.Popen(
        ["uv", "run", "streamlit", "run", "frontend/app.py"]
    )


if __name__ == "__main__":
    main()