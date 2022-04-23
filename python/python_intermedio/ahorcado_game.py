from dataclasses import replace
from math import isnan
import re
import random
import os
import unicodedata


def read():

    words = []
    with open('/Users/juancalderon/Desktop/code/platzi/python/python_intermedio/archivos/data.txt', 'r', encoding= 'utf-8') as f:
        for line in f:
            words.append(line.strip('\n'))
    print(words)
    return words
    
# def compare_caseless(s1, s2):
# def NFD(letra):
#     return unicodedata.normalize( 'NFD', letra)
#     return NFD(NFD(s1). casefold()) == NFD (NFD(s2).casefold())
            
def normalize(string): #Devuelve strings sin acentos 
    
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        string = string.replace(a, b).replace(a.lower(), b.lower())
    return string 
    
    # HANGMAN = ['''
    # +---+
    # |   |
    #     |
    #     |
    #     |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    #     |
    #     |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    # |   |
    #     |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    # /|   |
    #     |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    # /|\  |
    #     |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    # /|\  |
    # /    |
    #     |
    # =========''', '''
    # +---+
    # |   |
    # O   |
    # /|\  |
    # / \  |
    #     |
    # =========''']
    
def main():
    
    os.system('clear') 
    print('''\n \033[92m
.______    __   _______ .__   __. ____    ____  _______ .__   __.  __   _______   ______                     
|   _  \  |  | |   ____||  \ |  | \   \  /   / |   ____||  \ |  | |  | |       \ /  __  \                    
|  |_)  | |  | |  |__   |   \|  |  \   \/   /  |  |__   |   \|  | |  | |  .--.  |  |  |  |                   
|   _  <  |  | |   __|  |  . `  |   \      /   |   __|  |  . `  | |  | |  |  |  |  |  |  |                   
|  |_)  | |  | |  |____ |  |\   |    \    /    |  |____ |  |\   | |  | |  '--'  |  `--'  |                   
|______/  |__| |_______||__| \__|     \__/     |_______||__| \__| |__| |_______/ \______/                    
                                                                                                             
     ___       __                __   __    __   _______   _______   ______       _______   _______  __      
    /   \     |  |              |  | |  |  |  | |   ____| /  _____| /  __  \     |       \ |   ____||  |     
   /  ^  \    |  |              |  | |  |  |  | |  |__   |  |  __  |  |  |  |    |  .--.  ||  |__   |  |     
  /  /_\  \   |  |        .--.  |  | |  |  |  | |   __|  |  | |_ | |  |  |  |    |  |  |  ||   __|  |  |     
 /  _____  \  |  `----.   |  `--'  | |  `--'  | |  |____ |  |__| | |  `--'  |    |  '--'  ||  |____ |  `----.
/__/     \__\ |_______|    \______/   \______/  |_______| \______|  \______/     |_______/ |_______||_______|
                                                                                                             
     ___       __    __    ______   .______          ___       ______     ___       _______   ______         
    /   \     |  |  |  |  /  __  \  |   _  \        /   \     /      |   /   \     |       \ /  __  \        
   /  ^  \    |  |__|  | |  |  |  | |  |_)  |      /  ^  \   |  ,----'  /  ^  \    |  .--.  |  |  |  |       
  /  /_\  \   |   __   | |  |  |  | |      /      /  /_\  \  |  |      /  /_\  \   |  |  |  |  |  |  |       
 /  _____  \  |  |  |  | |  `--'  | |  |\  \----./  _____  \ |  `----./  _____  \  |  '--'  |  `--'  |       
/__/     \__\ |__|  |__|  \______/  | _| `._____/__/     \__\ \______/__/     \__\ |_______/ \______/        
                                                                                                            \033[0m\n ''')
    print( ''' 
    _                 _  _         _                  _                        _         _                   _ 
   (_)     /\        | |(_)       (_)                | |                      | |       | |                 | |
   | |    /  \     __| | _ __   __ _  _ __    __ _   | |  __ _   _ __    __ _ | |  __ _ | |__   _ __  __ _  | |
   | |   / /\ \   / _` || |\ \ / /| || '_ \  / _` |  | | / _` | | '_ \  / _` || | / _` || '_ \ | '__|/ _` | | |
   | |  / ____ \ | (_| || | \ V / | || | | || (_| |  | || (_| | | |_) || (_| || || (_| || |_) || |  | (_| | |_|
   |_| /_/    \_\ \__,_||_|  \_/  |_||_| |_| \__,_|  |_| \__,_| | .__/  \__,_||_| \__,_||_.__/ |_|   \__,_| (_)
                                                                | |                                            
                                                                |_|                                            
\n ''')
    print(''' \033[92m
    +---+
    |   |
        |
        |
        |
        |
    ========= 
    \033[0m \n ''')
    chosen_word = read() #Crea la lista completa de palabras de data.txt
    chosen_word = random.choice(chosen_word) # Hace una escogencia aletoria de una de las palabras de la lista
    list_chosen_word = list(enumerate(chosen_word)) #Crea una lista numerada de cada una de las letras
    print(list_chosen_word)
    word = [] # Palabra que va armando el usuario
    print(chosen_word)
    for letter in chosen_word: #Crea un guión bajo por cada letra de la palabra
        letter += letter
        hiden_word=letter.replace(letter, '_')
        print(hiden_word, end=' ')
    print(f"\n{letter}")
    attempts = 0
    while word != chosen_word and attempts < 6:
        user_letter = input('\n \nIngresa una letra: ').lower()    
        user_letter = normalize(user_letter)
        if user_letter.isalpha() == True and len(user_letter) == 1:
            print(f'\n {user_letter.upper()}')
            
            for i2 in range(len(chosen_word)):
                chosen_letters = chosen_word[i2]
                print(chosen_letters)
                validador = 0
                if re.search(user_letter, chosen_word[:]):
                    validador = 1
                else:
                    validador == 0
                if user_letter == chosen_letters:
                        word += chosen_letters
            for i in range(len(word)):
                if user_letter == word[i]:
                    print(f"La letra {user_letter} ya la usaste")
                    continue
                # word += word.insert(enumerate(chosen_letters),chosen_word[i2])
                print(word)
                print(f"Wow vas súper, si está la letra: {user_letter}")

                if user_letter != chosen_word[:]:
                    print(f" La letra: {user_letter} no está" ) 

            if validador == 1:
                attempts += 0
            elif validador == 0:
                attempts += 1
                
        elif user_letter.isalpha() == True and len(user_letter) != 1:
            print('\n \033[1m\033[91m Ingresa sólo una letra \n\033[0m')
            continue
        else:
            print('\n \033[1m\033[91m Sólo puedes ingresa letras \n\033[0m')
            continue
        
        # Use insert.() to add to 'word' variable in an specific index
        # Utilizar f' print para ir imprimiendo las letras de 'word' y los '_' que se muestran al usuario

        if attempts == 1:
            print('''\033[93m
            +---+
            |   |
            O   |
                |
                |
                |
            =========\033[0m\n''')
            continue
        if attempts == 2:
            print('''\033[93m
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========\033[0m\n''')
            continue
        if attempts == 3:
            print('''\033[93m
            +---+
            |   |
            O   |
            /|  |
                |
                |
            =========\033[0m\n''')
            continue
        if attempts == 4:
            print('''\033[93m
            +---+
            |   |
            O   |
            /|\ |
                |
                |
            =========\033[0m\n''')
            continue
        if attempts == 5:
            print('''\033[93m
            +---+
            |   |
            O   |
            /|\ |
            /   |
                |
            =========\033[0m\n''')
            continue
    else:
        os.system('clear') 
        print('''\n \033[91mAHORCADO XD \n
        +---+
        |   |
        O   |
        /|\ |
        / \ |
            |
        =========\033[0m\n''')
        print('El juego acabó')
        
    
    
    
    
        # Intentar crear una lista con la cantidad de letras de 'chosenword' ✅
        # y hacer lo mismo que en reeplacements para cambiar letras por '_'




if __name__ == '__main__':
    main()



    # Crear clases para los dibjos de los cuerpos del ahorcado
    # Crear funciones para buscar la letra (usar un search) , para revisar si la letra ya fue escrita y para imprimir los '_'