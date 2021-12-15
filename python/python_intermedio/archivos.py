def read():
   
    numbers = [] 
    with open("./archivos/numbers.txt", 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
        
def write():

    # With 'w' Write:

    names = ["Alejandra", "Juan", "Nalgurri", "Chestarina" "Tatiana", "Sandra"]
    with open("./archivos/names.txt", 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

    #With 'a' Append:

    # names = ["Gloria","Rúben", "Nico"]
    # with open("./archivos/names.txt", 'a', encoding='utf-8') as f:
    #     for name in names:
    #         f.write(name)
    #         f.write('\n')
    
def main():
    # read()
    write() 




if __name__ == '__main__':
    main()