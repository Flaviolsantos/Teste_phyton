def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)

def ler(ficheiro):
    with open(ficheiro) as file:
        for num, line in enumerate(file, 1):
            print(line.rstrip().split(','))
            if num == 1:
                titulos = (line.rstrip().split(','))

            else:
                dados = (line.rstrip().split(','))


    x = 1
    while x < len(dados[1]):
        totalsata = dados[1][x] + dados[1][x + 1]
        print(f'total sata = {totalsata}')
        x += 1
    while x < len(dados[2]):
        totaltap = dados[2][x] + dados[2][x + 1]
        print(f'total tap = {totaltap}')
        x += 1
    while x < len(dados[3]):
        totalryanair = dados[3][x] + dados[3][x + 1]
        print(f'total ryanair = {totalryanair}')
        x += 1

if __name__ =='__main__':
    ler("passageiros.csv")
