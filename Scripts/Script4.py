#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.


nums = (int(input('digite o primeiro numero: ')) , int(input('digite o segundo numero: ')) , int(input('digite o terceiro numero: ')) , int(input('digite o quarto numero: ')))

 

print(f'o valor 9 aparece {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O numero 3 está na posição {nums.index(3) + 1}')
else:
    print('o numero 3 não foi digitado.')

print('os numeros pares são: ' , end='')
for c in nums:
    if c % 2 == 0:
        print(c, end=' ')