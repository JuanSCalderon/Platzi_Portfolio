menu = """
Bienvenido al conversor de monedas 💰  

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Eligue una de las opciones: """
opcion = input(menu)
if opcion == "1":
    pesos = float(input('¿Cuántos pesos colombianos tienes?: '))
    valor_dolar = 3444
    valor_dolar = int(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print('Tienes $ ' + dolares + ' dólares') 
elif opcion == "2":
    pesos = float(input('¿Cuántos pesos argentinos tienes?: '))
    valor_dolar = 85.74
    valor_dolar = float(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print('Tienes $ ' + dolares + ' dólares') 
elif opcion == "3":
    pesos = float(input('¿Cuántos pesos mexicanos tienes?: '))
    valor_dolar = 19.8
    valor_dolar = float(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print('Tienes $ ' + dolares + ' dólares') 
else:
    print("Escoge una opción de las 3")
 




# pesos = input('¿Cuantos pesos colombianos tienes?:')
# pesos =int(pesos)
# valor_dolar = 3444
# valor_dolar = int(valor_dolar)
# dolares = pesos / valor_dolar
# dolares = round (dolares,2)
# dolares = str (dolares)
# print('Tienes $ ' + dolares + ' dólares') 