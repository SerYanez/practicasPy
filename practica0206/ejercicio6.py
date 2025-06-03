# Solicitar al usuario que ingrese su dirección email y verificar si la dirección es válida o no.
# En caso afirmativo, mostrar un mensaje que indique que la dirección es válida, en caso contrario
# advertirlo mediante un mensaje. Las direcciones de email que se consideran válidas son aquellas que
# contienen al menos un carácter y el símbolo "@".

def mail_valido(mail):
    if len(mail) > 1 and "@" in mail:
        print("Email válido")
    else:
        print("Mail inválido")


mail = input("Ingrese su dirección de e-mail: ")
mail_valido(mail)

