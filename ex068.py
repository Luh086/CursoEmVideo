from random import randint

print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*30)
cont = 0

while True:
    n = s = int(input('Digite um número entre 1 e 10: '))
    op = str(input('Qual você escolhe [P/I]: ')).upper().strip()
    npc = randint(1, 10)
    s += n + npc

    if s % 2 == 0 and op == 'P':
        cont =+ 1
        print(f'Você venceu !!! O computador escolheu {npc} e a soma deu {s}')
        print('Vamos jogar novamente.')
    else:
        print('-GAME OVER-')
        print(f'Você perdeu o computador escolheu {npc} e a soma total foi {s} ')
        break

if cont == 1:
    print(f'Você venceu apenas {cont} vez.')
elif cont == 0:
    print('Você não conseguiu vencer nenhuma vez.')
else:
    print(f'Você conseguiu vencer {cont} vezes')
print('FIM')
