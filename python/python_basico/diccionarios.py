def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    poblacion = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    for pais in poblacion.keys():
        print(pais)
    for pais in poblacion.values():
        print(pais)
    for pais, pobl in poblacion.items():
        print(pais + ' tiene ' + str(pobl) + ' habitantes')



if __name__ == '__main__':
    run()   