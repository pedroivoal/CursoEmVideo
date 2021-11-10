#
#
#
def jogada_PC():

    from random import randint
    n = randint(1,3)

    return n

#
#
#
def jokenpo(num):

    if num == 1:
        jogada = 'pedra'
    elif num == 2:
        jogada = 'papel'
    else:
        jogada = 'tesoura'

    return jogada

#
#
#
def acha_ganhador(play_PC, play_person):

    if play_PC == 'pedra' and play_person == 'pedra':
        return 'Empate'
    elif play_PC == 'pedra' and play_person == 'papel':
        return 'Você'
    elif play_PC == 'pedra' and play_person == 'tesoura':
        return 'Computador'

    elif play_PC == 'papel' and play_person == 'pedra':
        return 'Computador'
    elif play_PC == 'papel' and play_person == 'papel':
        return 'Empate'
    elif play_PC == 'papel' and play_person == 'tesoura':
        return 'Você'
    
    elif play_PC == 'tesoura' and play_person == 'pedra':
        return 'Você'
    elif play_PC == 'tesoura' and play_person == 'papel':
        return 'Computador'
    elif play_PC == 'tesoura' and play_person == 'tesoura':
        return 'Empate'


    
jogada_player = input('\nPedra, papel ou tesoura? ')
jogadaPC = jokenpo(jogada_PC())

print('\nVocê: {}'.format(jogada_player))
print('Computador: {}'.format(jogadaPC))

resutado = acha_ganhador(jogadaPC, jogada_player)

if resutado == 'Empate':
    print(resutado)
else:
    print('{} ganhou \n'.format(resutado))

