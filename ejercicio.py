# Creando una clase de Python con el método __init__:
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

# Creando un objeto de la clase Usuario:
usuario1 = Usuario("Favio", "mi_contrasena732012")

print(f"nombre_usuario: {usuario1.nombre_usuario}")
print(f"contrasena: {usuario1.contrasena}")
