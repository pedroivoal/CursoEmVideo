cores = {
    'limpa': '\033[1m',
    'preto e branco': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'ciano': '\033[1;36m',
}

n1 = int(input('\033[1;34mDigite o 1° número: \033[m'))
n2 = int(input('\033[1;34mDigite o 2° número: \033[m'))

print('\033[1;34mVocê digitou \033[1;32m{} \033[1;34me \033[1;32m{}\033[m'.format(n1, n2))