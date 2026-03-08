"""
Cliente para comunicación con la API.
"""

import requests

API_URL = "http://localhost:8000/predict"


def analizar_imagen(imagen_bytes):
    """
    Envía la radiografía al backend.
    """

    response = requests.post(
        API_URL,
        files={"file": imagen_bytes}
    )

    return response.json()