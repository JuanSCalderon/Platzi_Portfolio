import random


def run():
    vidas = 3
    numero_ran = random.randint(1,100)
    numero_elegido = int(input('Adivina un número de 1 a 100 (Tienes 4 oportunidades): '))
    
    while numero_elegido != numero_ran:
        if numero_elegido < numero_ran:
            print('\n Nop...El número es mayor \n')
            
        else:
            print('\n Nop... El número es menor \n')
        vidas -= 1           
        numero_elegido = int(input('\n Todavía tienes chance, escoge un nuevo número: '))
        
        if vidas == 2:
            print('\n Te quedan dos oportunidades :O \n')
        if vidas == 1:
            print('\n Te queda una oportunidad :S \n')
        if vidas == 0 and numero_elegido != numero_ran:
            print(' \n Perdistes \n')
            print('\n \n El número era: ' + str(numero_ran))
            break
    if numero_elegido == numero_ran:
        print('\n \n ¡ Felicidades Ganaste !\n \n')
        




if __name__ == '__main__':
    run()   