"""
Definición de los endpoints de la API.
"""

from fastapi import APIRouter, UploadFile, File
from app.services.fracture_service import analizar_radiografia
from app.utils.image_utils import cargar_imagen

router = APIRouter(
    prefix="",
    tags=["Análisis de Radiografías"]
)


@router.post(
    "/predict",
    summary="Analizar radiografía",
    description="Recibe una radiografía y determina si existe una fractura.",
    response_description="Resultado del análisis de la radiografía"
)
async def predecir(file: UploadFile = File(..., description="Archivo de la radiografía en formato PNG o JPG")):
    """
    Endpoint que permite subir una radiografía para su análisis.

    Parameters
    ----------
    file : UploadFile
        Imagen de la radiografía.

    Returns
    -------
    dict
        Resultado con la predicción del modelo.
    """

    contenido = await file.read()

    imagen = cargar_imagen(contenido)

    resultado = analizar_radiografia(imagen)

    return resultado