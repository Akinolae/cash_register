import sys as system
def get_int_input(prompt):
    value = None
    while type(value) != int:
        try:
            value = int(input(prompt))
            return value
        except:
            print('check that your input is correct!')
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
    main()