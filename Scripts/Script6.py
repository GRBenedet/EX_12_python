#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


words = ('casa' , 'filosofia' , 'atraso' , 'fracaço' , 'atalho')

for c in range(0, len(words)):
    print(f'\n{c + 1}. Em {words[c].upper()} temos: ' , end=' ')
    for i in words[c]:
        if i in 'aeiou':
            print(i , end=' ')
        