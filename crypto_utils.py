from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

class MotorCriptografico:
    def __init__(self, bits=2048):
        # Generamos llaves depende los bits que elija el usuario
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=bits
        )
        self.public_key = self.private_key.public_key()

    def cifrar(self, texto: str) -> bytes:
        # Transformamos el texto en algo oculto o secreto
        return self.public_key.encrypt(
            texto.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def descifrar(self, datos_cifrados: bytes) -> str:
        # Usamos la llave privada para recuperar el texto original
        texto_claro = self.private_key.decrypt(
            datos_cifrados,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return texto_claro.decode()
