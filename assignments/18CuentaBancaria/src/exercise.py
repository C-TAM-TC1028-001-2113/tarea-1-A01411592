def main():
    # escribe tu código abajo de esta línea
    pass
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingreso = float(input("Dame los ingresos: "))
    egreso = float(input("Dame los egresos: "))
    cheques = float(input("Dame el número de cheques: "))
    pagar = saldo + ingreso - egreso - (cheques * 13)
    interes = (pagar * 7.5) / 100
    si = pagar - interes 

    print("El saldo final de la cuenta es:",si)


if __name__ == '__main__':
    main()
