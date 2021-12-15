def divisor(num):
    divisor = [i for i in range(1,num+1) if num % i == 0]
    return divisor
  
    # for i in range(1,num+1):
    #     if num % i == 0:
    #         divisor.append(i) 
    # return divisor

def main():
    try:
        num = int(input('Ingresa un número: ')) 
        try:
            if num < 0:
                raise ValueError('* Ingresa un valor positivo *')
            print(divisor(num))
        except ValueError as ve:
            print(ve)
            return False

    except ValueError:
        print('* Ingresa un valor numérico *')


if __name__ == '__main__':
    main()