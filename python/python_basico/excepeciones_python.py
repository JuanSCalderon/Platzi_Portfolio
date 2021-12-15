def busca_pais(paises, pais):
    """
    Paises es un diccionario. País es la llave.
    Código con el principio EAFP.
    """
    try:
        return paises[pais]
    except KeyError:
        return None

def run():
    paises = {
        'Mexico':1,
        'Argentina':2, 
        'Colombia':3,
    }

    pais = input('Ingrese su pais: ')
    pais = pais.capitalize()

    print(busca_pais(paises, pais))


if __name__ == '__main__':
    run()