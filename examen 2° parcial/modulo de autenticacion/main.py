from validador import verificar_acceso


def main():
    try:
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")

        if verificar_acceso(usuario, clave):
            print("Acceso concedido")
        else:
            print("Credenciales incorrectas")
    except Exception:
        print("Ocurrió un error al validar el acceso.")


if __name__ == "__main__":
        main()