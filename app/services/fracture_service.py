"""
Servicio encargado de ejecutar el modelo de detección de fracturas.
"""

import torch
from app.core.model_loader import model, processor


def analizar_radiografia(imagen):
    """
    Analiza una radiografía utilizando el modelo de inteligencia artificial.
    """

    inputs = processor(images=imagen, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=1)

    indice = torch.argmax(probs).item()

    etiqueta = model.config.id2label[indice]

    confianza = probs[0][indice].item()

    # Traducción de etiquetas
    if etiqueta.lower() == "fractured":
        etiqueta = "fractura detectada"
    else:
        etiqueta = "sin fractura"

    return {
        "resultado": etiqueta,
        "confianza": round(confianza, 3)
    }