"""
Módulo principal del backend.

Este archivo inicia la API encargada de procesar radiografías
y ejecutar el modelo de inteligencia artificial para detectar fracturas.
"""

from fastapi import FastAPI
from app.api.routes import router

def crear_aplicacion() -> FastAPI:
    """
    Crea y configura la aplicación FastAPI.
    """

    app = FastAPI(
        title="API de Detección de Fracturas Óseas",
        description="Servicio de inteligencia artificial para analizar radiografías.",
        version="1.0.0"
    )

    # Registrar rutas
    app.include_router(router)

    return app


# instancia de la aplicación
app = crear_aplicacion()