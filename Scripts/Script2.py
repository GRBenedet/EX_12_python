#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Botafogo' , 'Palmeiras' , 'fortaleza' , 'flamengo' , 'são paulo' , 'internacional' , 'bahia' , 'cruzeiro', 'atletico-MG' , 'vasco da gama' , 'fluminense' , 'criciuma' , 'gremio' , 'Chapecoence' , 'juventude' , 'ec vitoria' , 'corinthians' , 'athletico-PR' , 'cuiaba' , 'atletico-GO')

op = 0

while True:
    print('='*8 , 'MENU' , '='*8)
    print('1. mostrar os 5 primeiros times da tabela.\n2. Os Últimos 4 colocados.\n3. Times em ordem alfabética. \n4. Em que posição está o time da Chapecoense\n5. finalizar programa.\n')
    op = int(input('qual opção deseja executar: '))

    match op:
        case 1:
            print(f'esses são os 5 primeiros times:\n{times[:5]}')
            break
        case 2:
            print(f'Os últimos 4 colocados são:\n{times[16:]}')
            break
        case 3:
            print(f'Agora os times estão em ordem alfabetica:\n{sorted(times)}')
            break
        case 4:
            print(f'a posição da Chapecoence é o {times.index('Chapecoence') + 1}ª time na tabela.')
            break
        case 5:
            print('Programa encerrado...')
            break