import time
import os
while True:
    try:
        numeroElementos = int(input("Introduzca el nÃºmero de elementos: "))
        listaElementos = [None] * numeroElementos
        break
    except:
        print('Solo introduzca nÃºmeros.')
        print('IntÃ©ntelo nuevamente.')
        time.sleep(1)
        os.system('cls')
while True:
    try:
        for i in range(0, numeroElementos):
            elementos = int(input('Elemento {}: '.format(i+1)))
            listaElementos[i] = elementos
        numeros = 0
        total = 0
        for i in range(len(listaElementos)):
            numeros = listaElementos[i]
            total += numeros

        print('Promedio: ', total/numeroElementos)
        break
    except:
        print('Solo introduzca nÃºmeros.')
        print('IntÃ©ntelo nuevamente.')
        time.sleep(1)
        os.system('cls')
        

    
