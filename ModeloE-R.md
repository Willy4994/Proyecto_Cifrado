# Modelo Entidad-Relación (E-R) 📊

**Proyecto:** Gestor de Mensajería Criptográfica RSA  
**Curso:** Análisis de Sistemas - UMG  
**Desarrolladores:** Ruben Garcia, Willi Hernandez  

---

## 1. Diagrama Lógico
El sistema sigue una estructura relacional diseñada para garantizar la integridad referencial y la trazabilidad de los mensajes cifrados.



## 2. Descripción de Entidades

### Entidad: Usuarios
*   **id_usuario (PK):** Identificador único del sistema.
*   **nombre_usuario:** Nombre de cuenta único.
*   **password_hash:** Almacenamiento seguro de credenciales.

### Entidad: RegistroMensajes
*   **id_registro (PK):** UUID para identificar el mensaje cifrado.
*   **id_usuario (FK):** Relación con el autor del mensaje.
*   **texto_cifrado:** Contenido protegido en formato Hexadecimal.
*   **estado:** Flag para borrado lógico (ACTIVO/USADO).

### Entidad: Tokens
*   **id_token (PK):** Identificador único del token.
*   **id_registro (FK):** Relación directa con el mensaje a descifrar.
*   **token_string:** Código de 8 caracteres (Único).
*   **usado:** Booleano de control de acceso único.

### Entidad: Auditoria
*   **id_log (PK):** Autoincremental.
*   **id_registro (FK):** Relación con el mensaje intentado.
*   **resultado:** Registro de éxito o fallo.
*   **ip_visitante:** Dirección IP para control de seguridad.

## 3. Relaciones y Cardinalidad
1.  **Usuarios → RegistroMensajes (1:N):** Un usuario puede poseer múltiples registros.
2.  **RegistroMensajes → Tokens (1:1):** Un registro genera exactamente un token de recuperación.
3.  **RegistroMensajes → Auditoria (1:N):** Un registro puede generar múltiples entradas de auditoría por intentos de acceso.

---
*Documento generado para fines académicos - Facultad de Ingeniería UMG 2026.*
