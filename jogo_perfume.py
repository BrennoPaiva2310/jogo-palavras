secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Acabaram Sua chances')
        break


    letra = input('Digite uma letra: ')
    print(' ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra :) ')
        continue

    digitadas.append(letra.lower())

    if letra.lower() in secreto:
        print(f'A sua letra existe na palavra')
        print(' ')

    else:
        print(f'A {letra} não existe na palavra')
        digitadas.pop()
        chances-=1
        print(f'Você ainda tem {chances} chances')

    secreto_temporario =''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Parabens!!!!')
        break
    else:
        print(f'A palavra está assim {secreto_temporario}')
        print(' ')

