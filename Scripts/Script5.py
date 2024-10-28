#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela_produtos = ('lapis' , 1.75 , 'borracha' , 2.00 , 'caderno' , 15.90 , 'estojo' , 25.00 , 'transferidor' , 4.20 , 'compasso' , 9.99 , 'mochila' , 120.32 , 'canetas' , 22.30 , 'livro' , 34.90)


print(f'{'-' * 50}\n{'LISTAGEM DE PRODUTOS'.center(50)}\n{'-' * 50}')

for c in range(0, len(tabela_produtos)):
    if c % 2 == 0:
        print(f'{tabela_produtos[c]:.<44}', end='')
    else:
        print(f'R$ {tabela_produtos[c]:.2f}')