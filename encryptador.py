from cryptography.fernet import Fernet

# Texto a encriptar
text = "Hola Mundo"

# Genera una clave o llave en formato de secuencia de bytes:
key = Fernet.generate_key()
# Creamos un objeto cifrado
objeto_cifrado = Fernet(key)
# Creamos un texto encriptado que va ser igual a el objeto crifrado
texto_encriptado = objeto_cifrado.encrypt(str.encode(text)) # encode cifra el texto
print(texto_encriptado)

# Creamos esta variable para desencriptar el texto
texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado_bytes)

texto_desencriptado = texto_desencriptado_bytes.decode()
print(texto_desencriptado)