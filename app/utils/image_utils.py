"""
Funciones utilitarias para manejo de imágenes médicas.
"""

from PIL import Image
import io


def cargar_imagen(bytes_imagen):
    """
    Convierte bytes recibidos en una imagen.

    Parameters
    ----------
    bytes_imagen : bytes
        Contenido binario de la imagen.

    Returns
    -------
    PIL.Image
        Imagen lista para ser procesada por el modelo.
    """

    imagen = Image.open(io.BytesIO(bytes_imagen))

    return imagen.convert("RGB")