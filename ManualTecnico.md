# Manual Técnico - Implementación de Cifrado Asimétrico RSA 🛠️

**Universidad Mariano Gálvez de Guatemala**  
**Facultad de Ingeniería en Sistemas de Información**  
**Cátedra:** Análisis de Sistemas  
**Desarrolladores:** Ruben Garcia, Willi Hernandez  

---

## 1. Especificaciones de Ingeniería
El sistema emplea una arquitectura robusta basada en el framework **FastAPI** y el ORM **SQLAlchemy**. Se ha priorizado la integridad de los datos mediante el uso de UUIDs y el algoritmo **RSA de 2048 bits**.

## 2. Diccionario de Datos Detallado

| Tabla | Campo | Tipo | Restricción | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| **usuarios** | `id_usuario` | Integer | PK, Auto | Identificador del autor del mensaje. |
| **registro_mensajes** | `texto_cifrado` | Text | NOT NULL | Criptograma almacenado en formato Hexadecimal. |
| **registro_mensajes** | `estado` | Varchar | Default 'ACTIVO' | Control para el borrado lógico. |
| **tokens** | `token_string` | Varchar(8) | Unique, Index | Código alfanumérico de acceso para el usuario. |
| **tokens** | `usado` | Boolean | Default False | Flag de seguridad para un solo uso. |
| **auditoria** | `resultado` | Varchar | NOT NULL | Estado final del intento (EXITOSO/FALLIDO). |

## 3. Lógica de Negocio y Flujo de Control

### 3.1 Proceso de Cifrado (Escritura)
1. El sistema recibe el texto plano y la etiqueta.
2. El `MotorCriptografico` genera un par de llaves RSA.
3. Se cifra el contenido con la `public_key` y se guarda en `registro_mensajes`.
4. Se genera un `Token` asociado con una validez de 7 días.

### 3.2 Proceso de Descifrado (Lectura)
1. El usuario ingresa el `token_string`.
2. **Validación:** El sistema comprueba en una sola transacción que el token exista, no haya sido usado y no haya expirado.
3. **Ejecución:** Si es válido, el motor usa la `private_key` para descifrar.
4. **Finalización:** Se ejecuta el método `marcarComoUsado()` y se genera un log en la tabla de `Auditoria`.

## 4. Requerimientos de Seguridad
* **Protección de Llaves:** La llave privada reside únicamente en la instancia del motor durante la sesión.
* **Borrado Lógico:** No se eliminan registros físicos para mantener la trazabilidad de la auditoría exigida en el análisis de sistemas.

---
*Facultad de Ingeniería en Sistemas, Ciclo 2026.*
