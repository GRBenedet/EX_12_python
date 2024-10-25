#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

nums = ('um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'dose' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte')

op = 0

op = int(input('digite um numero de 1 a 20: ')) - 1

while 20 <= op >= 0:
    op = int(input(' tente de novo, digite um numero de 1 a 20: ')) - 1

print(f'voce escolheu escreveu {nums[op]}')