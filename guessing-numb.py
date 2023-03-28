import random


limite_numb = input('digite um numero: ')

if limite_numb.isdigit():
        limite_numb = int(limite_numb)

        if limite_numb < 0:
            print('Digite um numero maior que zero da proxima vez')
            quit()

else:
    print('Digite um número da proxima vez')
    quit()


num_aleatorio = random.randint(0,limite_numb)
tentativas = 0

while True:
    tentativas += 1
    guess = input('Tentativa: ')

    if guess.isdigit():
        guess = int(guess)
        if guess > limite_numb:
            print('Tentativa maior que o limite')
            continue
        if guess < 0:
            print('Digite um número maior que zero')
            continue
    else:
        print('Digite um número da próxima vez')

    if guess == num_aleatorio:
        print('Acertou!')
        break
    elif guess > num_aleatorio:
        print('Você está acima do número')
    else:
        print('Você está abaixo do número')


print('Você acertou em',tentativas,'tentativas')