import sys as system
from time import ctime

def get_int_input(prompt):
    value = None
    while type(value) != int:
        try:
            value = int(input(prompt))
            return value
        except KeyboardInterrupt as e:
            exit()
        except:
            print('check that your input is correct!')
            print(ctime(), e, file = ERROR_FILE)
            pass

def main ():
    while True:
        clientName = input('Enter client name: ')
        if not clientName:
            break

        while True:
            productName = input('What product was purchased?: ')
            if not productName:
                break

            producQty = get_int_input(f'how many {productName}: ')
            price = get_int_input(f'how much is the cost of {producQty} {productName}?: ')


if __name__ ==  '__main__':
    ERROR_FILE = open('lo.txt', 'a')
    main()
    ERROR_FILE.close()
