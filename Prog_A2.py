if __name__ == '__main__':

    x = float(input('Altura em metros? '))
    print(f'{x * 100} cm')
    y = input(" repetir? ")

    while y == 'y':
        x = float(input('Altura em metros? '))
        print(f'{x * 100} cm')
        if y == 'n':
            print()


