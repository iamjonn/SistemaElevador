import os

print('Sou processo principal (pai). Meu PID é:', os.getpid())

escolha = input('\nDigite 1 para criar um novo processo, ou qualquer outra tecla para sair: ')

if escolha == '1':
    pid = os.fork()
    if pid == 0:
        print('\nSou filho. Meu PID é:', os.getpid())
    elif pid > 0:
        print('Sou pai. Meu PID:', os.getpid(), 'Meu filho é:', pid)
else:
    exit()
