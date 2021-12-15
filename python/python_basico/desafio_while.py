def run(): 

    LIMITE = 3
    contador = 0
    agenda = ''
    while contador <= LIMITE:
        nombre = input('Ingresa tu nombre: ')
        nombre_cap = nombre.capitalize()
        apellido = input('Ingresa tu apellido: ')
        apellido_cap = apellido.capitalize()
        contacto = nombre_cap + ' ' + apellido_cap
        print('Tu nombre y apellido son: ' + contacto)
        question = input('¿Quieres otro contacto? ')
        agenda = agenda + '\n' + contacto 
        print (agenda)
        contador += 1

        if question.lower() == 'si':
            continue
        else:
            print ('Ah bueno entonces vayates')
            break
        





if __name__ == '__main__':
    run()