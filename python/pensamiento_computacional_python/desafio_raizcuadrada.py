import math


def epsilon(pass)

    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        # print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')


def busqueda_binaria(pass)
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
    pass 



if __name__ == '__main__':
    run()