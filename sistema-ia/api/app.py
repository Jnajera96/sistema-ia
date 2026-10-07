from src.inferencia import predecir


def iniciar():
    datos = [1, 2, 3]
    resultado = predecir(datos)
    return resultado


if __name__ == "__main__":
    print(iniciar())
