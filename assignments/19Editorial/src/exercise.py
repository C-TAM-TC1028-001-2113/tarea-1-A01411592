def main():
    # escribe tu código abajo de esta línea
    pass
    Npalabras = float(input("Dame el número de palabras: "))
    if Npalabras <= 475:
        costo = 60
        descuento = costo * 0.10
        total = costo - descuento 
        print("El costo de la publicación es: ",total)
    if Npalabras >= 475 and Npalabras <= 950:
        costo =  2 * 60 
        descuento = costo * 0.10
        total = costo - descuento 
        print("El costo de la publicación es: ",total)
    else:
        print("El costo de la publicacion es mayor a 108 peos")
    
    
if __name__ == '__main__':
    main()
