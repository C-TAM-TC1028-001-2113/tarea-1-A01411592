def main():
    # escribe tu código abajo de esta línea
    pass
    costo2 = float(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = float(input("Dame el número de minutos: "))
    
    costo = (costo2 + megas + minutos) * 0.80
    
    print("El costo mensual es:",costo)

if __name__ == '__main__':
    main()
