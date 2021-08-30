def main():
    # escribe tu código abajo de esta línea
    pass
    nuevo = float(input("Dame la cantidad de juegos nuevos: "))
    usado = float(input("Dame la catidad de juegos usados: "))
    
    costo = (nuevo * 1000) + (usado * 350)
    
    print("El total de la compra es:",costo)


if __name__ == '__main__':
    main()
