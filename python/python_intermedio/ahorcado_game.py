from math import isnan
import re
import random
import os


def read():

    words = []
    with open('./archivos/data.txt', 'r', encoding= 'utf-8') as f:
        for line in f:
            words.append(line.strip('\n'))
    return words
            
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
    print('''\n BIENVENIDO AL JUEGO DEL AHORCADO \n
    \033[92m
    +---+
    |   |
        |
        |
        |
        |
    ========= 
    \033[0m \n''')
    print( '''¡ Adivina la palabra ! \n''')
    chosen_word = read() #Crea la lista completa de palabras de data.txt
    chosen_word = random.choice(chosen_word) # Hace una escogencia aletoria de una de las palabras de la lista
    list_chosen_word = list(enumerate(chosen_word)) #Crea una lista numerada de cada una de las letras
    print(list_chosen_word)
    word = [] # Palabra que va armando el usuario
    print(chosen_word)
    print(len(chosen_word))
    for i in chosen_word:
        print('_', end= ' ')
    attempts = 0
    list_letter = []
    while attempts < 6:
        # while word != chosen_word:
        letter = input('\n \nIngresa una letra: ').lower()    
        letter = normalize(letter)
        list_letter += [letter]
        print(list_letter)

        if letter.isalpha() == True and len(letter) == 1:
            print(f'\n {letter.upper()}')
            
            for i2 in range(len(chosen_word)):
                chosen_letters = chosen_word[i2]
                print(chosen_letters)
                validador = 0
                if re.search(letter, chosen_word[:]):
                    validador = 1
                else:
                    validador == 0
                    
                if letter == chosen_letters:
                    word += chosen_letters
                    # word += word.insert(enumerate(chosen_letters),chosen_word[i2])
                    print(word)
                    print(f"Wow Vas súper, si está la letra: {letter}")

                if letter != chosen_word[:]:
                    print(f" La letra: {letter} no está" ) 

            if validador == 1:
                attempts += 0
            elif validador == 0:
                attempts += 1
                
        elif letter.isalpha() == True and len(letter) != 1:
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