def divisor(num):
    divisor = [i for i in range(1,num+1) if num % i == 0]
    return divisor

def main():
    num = input('Ingresa un número: ')
    assert num.isnumeric() and int(num) > 0, '* Ingresa sólo números y que sean positivos *' 
    print(divisor(int(num)))



if __name__ == '__main__':
    main()