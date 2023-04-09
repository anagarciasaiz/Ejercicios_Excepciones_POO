import re

class Usuario:
    def __init__(self, correo, contrasena):
        self.correo = correo
        self.contrasena = contrasena

    def logIn(self):
        email = input("Introduzca su dirección de correo: ")
        while True:
            try:
                if email == "":
                    raise Exception("'' es una entrada incorrecta. Introduzca una dirección de correo electrónico")
                elif re.search(".+@.+\..+", email) is None:
                    raise Exception("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
                else:
                    if email == self.correo:
                        print(f"¡Bienvenido {self.correo}!")
                        break
                    else:
                        raise Exception("Cuenta bloqueada a causa de un ataque")
            except Exception as e:
                print(e)
                if str(e) == "Cuenta bloqueada a causa de un ataque":
                    break
            email = input("Introduzca su dirección de correo: ")

user = Usuario("ana@gmail.com", "ana")
user.logIn()
