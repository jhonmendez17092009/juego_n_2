# importamos la libreria random

import random

usuario = int(input("digite un numero del 1 al 100: "))
i = 1

if usuario < 1 or usuario > 100:
    print("Valor No Valido.")
else :
    maq = random.randint(1,100)

    while maq != usuario:
        i = i +1
        if usuario > maq :
            print("intentalo de nuevo el numero es muy alto")
        else:
            print("intentalo de nuevo el numero es muy bajo")
        usuario = int(input("vuelve a intentarlo de nuevo: "))
        if maq == usuario:
            print("GANESTE")
            print("el valor de la maq era : "  + str(maq))
            print("el numero de intentos es: " + str(i))