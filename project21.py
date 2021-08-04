from random import shuffle
from time import sleep


def checkFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


ouros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
espadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
copas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
paus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]  # Cartas em listas.
deck = [ouros, espadas, copas, paus]  # Juntando as listas em uma coleção de listas
print('BlackJackPy')
print('*=-=' * 6 + '*')
while True:
    print('Opções'.center(25, '-'))  # Menu
    print("1 - Para jogar\n2 - Para um breve tutorial")
    start = str(input("Opção = "))
    if start.isnumeric():
        start = int(start)
        if start == 1:
            break
        elif start == 2:
            print('*=-=' * 21 + '*')
            print("No inicio, indique o valor a depositar em fichas e o quanto quer apostar em seguida.\n"
                  "O objetivo do jogo é ficar mais próximo que a Mesa(CPU) do número 21 sem estourar esse limite.\n"
                  "No início de cada turno, a cpu compra duas cartas e revela seus valores.\nEm seguida, o jogador "
                  "recebe duas cartas e decide se vai continuar comprando ou não.\nCaso perca, o jogador perde o valor "
                  "apostado.\nCaso vença, seu dinheiro apostado dobra e retorna para sua carteira.\nÉ permitido parar "
                  "de jogar apenas ao final de cada rodada.\nTodo dinheiro usado nesse programa é fictício. 👀\n Tenha "
                  "um bom jogo")
            print('*=-=' * 21 + '*')
        else:
            print(f"{start} Não é numero válido de opção.")
    else:
        print(f"{start} Não é numero válido de opção.")  # Fim do menu
while True:
    carteira = str(input('Quanto em dinheiro quer de fichas? -> R$').replace(',', '.'))  # Definição da carteira
    if checkFloat(carteira):
        carteira = float(carteira)
        break
    else:
        print("ERROR! Digite um valor válido.")
print(f'Sua carteira possui R${carteira:.2f}')
while carteira > 0:
    print('*=-=' * 12 + '*')
    while True:
        aposta = str(input('Vai apostar quanto? R$').replace(',', '.'))  # Valor de aposta
        if checkFloat(aposta):
            aposta = float(aposta)
            if 0 < aposta <= carteira:  # Impedir que apostas sejam maiores do que a carteira e maiores que zero.
                break
            else:
                print(f'Insira um valor dentro do teu montante de R${carteira:.2f}')
        else:
            print("Digite um numero válido. (Exemplo: 10.40")
    print('Embaralhando...')
    baralho = []  # Iniciando lista do baralho para se embaralhado.
    for c in range(0, 4):  # Centralizando as cartas em uma única lista.
        for v in range(0, 14):  # Não usei lista única no inicio do programa para praticar e dar um "ar" de realismo.
            baralho.append(deck[c][v])
    sleep(1)
    print('Mesa comprando...')
    derrota = False
    shuffle(baralho)  # Momento de embaralhar o deck.
    mesa = baralho[0] + baralho[1]  # Primeira compra da mesa.
    jogador = baralho[2] + baralho[3]  # Primeira compra do Jogador.
    extra = 0  # Contador para adicionar +1 em futuras compras.
    sleep(1)
    print(f'A mesa comprou: {baralho[0]} e {baralho[1]} = {mesa}')
    while True:
        if mesa > 21:
            sleep(1)
            print('CPU perdeu!')
            break
        resposta = str(input(f'Suas cartas somam -> {jogador} e a Mesa -> {mesa}\nDeseja comprar? [S/N]').capitalize())
        if resposta != '':
            if resposta[0] in 'S':
                print('Comprando...', end=' ')
                sleep(1)
                jogador += baralho[4 + extra]
                print(f'+{baralho[4 + extra]}')
                sleep(1)
                extra += 1
                if jogador >= 21:
                    break
            elif resposta[0] in 'N':
                break
    if jogador < 22:
        while 21 > mesa < jogador:
            mesa += baralho[4 + extra]
            extra += 1
            print('O computador está comprando...')
            sleep(1)
            print(f'O computador comprou + {baralho[4 + extra]} = {mesa}')
    if 21 >= mesa > jogador:
        derrota = True
    if jogador > 21:
        derrota = True
    if derrota:
        print(f'Você comprou {jogador}\nO computador comprou {mesa}')
        sleep(1)
        print(f'Você perdeu!! -R${aposta:.2f}')
        carteira -= aposta
    elif jogador == mesa:
        print('Empate!')
    elif not derrota:
        print(f'O computador comprou {mesa} e você comprou {jogador}')
        sleep(1)
        print(f'Parabéns, você venceu. +R${aposta:.2f}')
        carteira += aposta
    print(f'Você possui R${carteira:.2f}')
    if carteira == 0:
        print('Quebrou a banca.')
        break
    while True:
        continuar = str(input('Deseja continuar? [S/N]').strip().capitalize())
        if continuar != '':
            if continuar[0] in 'NS':
                break
        else:
            print('S para continuar / N para parar')
    if continuar[0] == 'N':
        break
if carteira > 0:
    print(f'Você parou de jogar com R${carteira:.2f}')
