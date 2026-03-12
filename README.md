# ⚙️ Requisitos

Antes de ejecutar el proyecto asegúrate de tener instalado:

-   Python **3.11 o superior**
-   Git
-   UV (gestor moderno de dependencias para Python)
-   Make (opcional, para ejecutar comandos simplificados)

Instalar **uv**:

``` bash
pip install uv
```

------------------------------------------------------------------------

# 🚀 Instalación del proyecto

Sigue los siguientes pasos para instalar y ejecutar el proyecto en tu
máquina local.

## 1️⃣ Clonar el repositorio

``` bash
git clone https://github.com/tu-usuario/xray-fracture-detector.git
```

Entrar al directorio del proyecto:

``` bash
cd xray-fracture-detector
```

------------------------------------------------------------------------

## 2️⃣ Crear el entorno virtual

Crear el entorno virtual utilizando **uv**:

``` bash
uv venv
```

------------------------------------------------------------------------

## 3️⃣ Activar el entorno virtual

### Windows

``` bash
.venv\Scripts\activate
```

o en **Git Bash**

``` bash
source .venv/Scripts/activate
```

### Linux / Mac

``` bash
source .venv/bin/activate
```

------------------------------------------------------------------------

## 4️⃣ Instalar dependencias

Instalar todas las dependencias del proyecto:

``` bash
uv sync
```

------------------------------------------------------------------------

# ▶ Ejecutar el sistema

El proyecto incluye un **Makefile** que permite iniciar el backend y el
frontend con un solo comando.

``` bash
make start
```

Esto iniciará automáticamente:

Backend → http://localhost:8000\
Frontend → http://localhost:8501

------------------------------------------------------------------------

# 🌐 Acceso a la aplicación

## Interfaz de usuario

Abrir en el navegador:

http://localhost:8501

Desde esta interfaz el usuario podrá:

-   Subir radiografías
-   Visualizar la imagen cargada
-   Analizar posibles fracturas con IA
-   Ver la probabilidad del diagnóstico

------------------------------------------------------------------------

## Documentación de la API

FastAPI genera documentación automática en:

http://localhost:8000/docs

Aquí se puede probar directamente el endpoint:

POST /predict

subiendo una radiografía desde el navegador.

------------------------------------------------------------------------

# 🧠 Funcionamiento del sistema

Flujo del sistema:

1.  El usuario carga una radiografía desde la interfaz.
2.  La imagen se envía al backend mediante la API.
3.  FastAPI recibe la imagen y la procesa.
4.  El modelo de inteligencia artificial analiza la radiografía.
5.  Se devuelve una predicción indicando si existe una posible fractura.

------------------------------------------------------------------------

# 📊 Ejemplo de respuesta del modelo

``` json
{
  "resultado": "fractura detectada",
  "confianza": 0.92
}
```

------------------------------------------------------------------------

# ⚠️ Nota importante

Este sistema tiene fines **académicos y de investigación**.

No debe utilizarse como herramienta de diagnóstico médico sin la
supervisión de profesionales de la salud.

------------------------------------------------------------------------

# 👨‍💻 Autor

**Juan Pablo Orozco**
**Luis David Hurtado**
**Manuel Castillo**
**Luisa Ospina**

Proyecto académico de Inteligencia Artificial para detección de
fracturas en radiografías.
