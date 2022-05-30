if __name__ == '__main__':
    lista = []
    npar = []
    nimpar = []
    primo = []

    x = input('Insira um numero ')
    lista.append(x)
    par = int(x) % 2
    if par == 0:
        print(f'{x} é par')
        npar.append(lista[0])
    if par != 0:
        print(f'{lista[0]} é impar')
        nimpar.append(x)


    if x == max(lista):
        print(f'{x} é o maior')
    if x == min (lista):
        print(f'{x} é o menor')
    if x != min(lista) and x != max(lista):
        print(f'x é um numero normal')



    y = input(" repetir? ")


    while y == 'yes':
        outro = input('Insira outro numero ')
        par = int(outro) % 2

        if par == 0:
            print(f'{outro} é par')
            npar.append(outro)
            y = input(" repetir? ")
        if par != 0:
            print(f'{outro} é impar')
            nimpar.append(outro)
            y = input(" repetir? ")
    if y == 'no':
            print(lista)
            print(f'Numeros Pares {npar}')
            print(f'Numeros Impares {nimpar}')
            print(f'Numeros Primos {primo}')
