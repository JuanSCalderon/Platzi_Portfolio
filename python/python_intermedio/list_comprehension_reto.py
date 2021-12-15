def main():
    
    LIMITE = 99999
    multiple = [i for i in range(LIMITE + 1) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 and i != 0] 
    print(multiple)


if __name__ == '__main__':
    main()