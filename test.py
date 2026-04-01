from crypto_utils import MotorCriptografico

# Probamos con 1024 bits como pidió el profesor
motor = MotorCriptografico(bits=1024)

mensaje = "Este es un secreto universitario"
print(f"Original: {mensaje}")

# Ciframos
secreto = motor.cifrar(mensaje)
print(f"Cifrado (lo que se guarda en DB): {secreto.hex()[:50]}...")

# Desciframos
recuperado = motor.descifrar(secreto)
print(f"Descifrado: {recuperado}")