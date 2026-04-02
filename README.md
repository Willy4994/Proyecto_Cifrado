# Sistema de Gestión Criptográfica RSA 🔐

**Universidad Mariano Gálvez de Guatemala**  
**Facultad de Ingeniería en Sistemas de Información**  
**Curso:** Análisis de Sistemas  
**Desarrolladores:** Ruben Garcia, Willi Hernandez  

---

## Descripción del Proyecto
Aplicación web desarrollada con **FastAPI** que permite el cifrado de mensajes mediante el algoritmo **RSA de 2048 bits**. El sistema garantiza la confidencialidad mediante un esquema de tokens de un solo uso y auditoría de accesos.

## Guía de Usuario
1. **Cifrar:** Ingrese una etiqueta y el mensaje. El sistema le entregará un **Token** único.
2. **Descifrar:** Ingrese el Token de 8 caracteres. Si es válido y no ha expirado (7 días), el sistema revelará el mensaje.
3. **Seguridad:** Una vez consultado, el token se inhabilita permanentemente (Single-use policy).

## Instalación y Ejecución
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python main.py` o `uvicorn main:app --reload`

---
