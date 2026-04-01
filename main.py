import uuid
from datetime import datetime
from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn

import models
from database import engine, get_db
from crypto_utils import MotorCriptografico 

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
gestor = MotorCriptografico(bits=2048)

@app.get("/")
def inicio(request: Request):
    # Formato actualizado para evitar TypeError
    return templates.TemplateResponse(request, "index.html")

@app.post("/cifrar")
async def cifrar(request: Request, texto: str = Form(...), etiqueta: str = Form(...), db: Session = Depends(get_db)):
    cifrado_bytes = gestor.cifrar(texto) 
    nuevo_msg = models.RegistroMensaje(
        id_usuario=1, etiqueta=etiqueta, 
        texto_cifrado=cifrado_bytes.hex(), longitud_bits=2048
    )
    db.add(nuevo_msg)
    db.flush()

    t_val = str(uuid.uuid4())[:8].upper()
    nuevo_token = models.Token(id_registro=nuevo_msg.id_registro, token_string=t_val)
    db.add(nuevo_token)
    db.commit()

    return templates.TemplateResponse(request, "index.html", {"token": t_val})

@app.post("/descifrar")
async def descifrar(request: Request, token_input: str = Form(...), db: Session = Depends(get_db)):
    tk = db.query(models.Token).filter(models.Token.token_string == token_input).first()
    
    if not tk or tk.usado:
        log = models.Auditoria(resultado="FALLIDO", ip_visitante=request.client.host)
        db.add(log)
        db.commit()
        return templates.TemplateResponse(request, "index.html", {"error": "Token inválido o usado"})

    msg = db.query(models.RegistroMensaje).filter(models.RegistroMensaje.id_registro == tk.id_registro).first()
    
    try:
        original = gestor.descifrar(bytes.fromhex(msg.texto_cifrado))
        tk.usado = True 
        msg.estado = "USADO"
        
        log = models.Auditoria(id_registro=msg.id_registro, resultado="EXITOSO", ip_visitante=request.client.host)
        db.add(log)
        db.commit()

        return templates.TemplateResponse(request, "index.html", {"revelado": original, "etiqueta": msg.etiqueta})
    except:
        return templates.TemplateResponse(request, "index.html", {"error": "Error de descifrado"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)