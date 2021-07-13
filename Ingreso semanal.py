from datetime import datetime
while True:
    n = int(input("TIEMPO TRANSCURRIDO \n"
                  "1. SEMANAL \n"
                  "2. SALIR \n"
                  "Elija una opcion: "))
    if n == 1:
        a = int(input("Ingreso del lunes: "))
        b = int(input("Ingreso del martes: "))
        c = int(input("Ingreso del miercoles: "))
        d = int(input("Ingreso del jueves: "))
        e = int(input("Ingreso del viernes: "))
        f = int(input("Ingreso del sabado: "))
        g = int(input("Ingreso del domingo: "))
        total = a + b + c + d + e + f + g
        print("El ingreso de la semana es: ", total)
        now = datetime.now()
        horas_actual = now.strftime("%H:%M:%S")
        print("GANANCIA SEMANAL:", a)
        print("HORA ACTUAL: ", horas_actual)
    else:
        break