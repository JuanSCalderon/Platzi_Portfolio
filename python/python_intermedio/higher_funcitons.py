from functools import reduce

def main():
    #Funciones anónimas: # identificador = argumento: expresión
    # lambda argumentos: expresión
    # ejemplo:
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))

    ###
    # Higher Functions: filter, map y reduce
    # funciones que reciben otras funciones como parámetro otra función

    # filter:
    my_list = [1,2,3,4,5,7,9,10,11,12,13,14,15]
    odd = list(filter(lambda i: i%2 != 0, my_list))
    print(odd)

    # map:
    nums = [i2*1 for i2 in range(1,6)]
    squares = list(map(lambda i3: i3**2,nums))
    print(squares)

    # reduce: IMPORTANTE (Importar 'reduce' desde 'functools')
    # Para esta higher function se ingresan 2 parámetros (a,b), 'a' sería el primer parámetro
    # y 'b' el segundo de la lista, los cuáles una vez hagan la operación de la expresión serán
    # reemplazados; 'a' se convertirá en el resultado de la expresión anterior y 'b' será el siguiente valor de
    # la lista.

    my_list2 = [2,2,2,2,2]
    all_multiply = reduce(lambda a,b: a*b, my_list2)
    print(all_multiply)


if __name__ == '__main__':
    main()