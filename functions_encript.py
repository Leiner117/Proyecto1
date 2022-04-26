from cryptography.fernet import Fernet
password_students = {}
password_admins = {}
def cifrar(name,password,rank):
    key = Fernet.generate_key()
    objeto_cifrado = Fernet(key)
    texto_encriptado = objeto_cifrado.encrypt(str.encode(password))
    if rank == "Administrativo":
        password_admins[name] = objeto_cifrado
    elif rank == "Estudiante":
         password_students[name] = objeto_cifrado
    print(password_students)
    print(password_admins)
    print(texto_encriptado)
    return texto_encriptado
def desencriptado(name,password,rank):
    if rank == "Administrativo":
        objeto_cifrado = password_admins[name]
    elif rank == "Estudiante":
        objeto_cifrado = password_students[name]
    texto_desencriptado_bytes = objeto_cifrado.decrypt(password)
    texto_desencriptado = texto_desencriptado_bytes.decode()
    print(texto_desencriptado)
    return texto_desencriptado
cifrar("leiner","12345","Administrativo")
desencriptado("leiner","12345","Administrativo")