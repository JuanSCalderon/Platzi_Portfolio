def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_inv = palabra[::-1]
    if palabra == palabra_inv:
        return True
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()