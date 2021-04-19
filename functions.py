import rest_http as http


def listarClubes():
    data = dict(http.get('clubes'))
    print('---------- Clubes ----------')
    for i in data:
        print(data[i]['nome'])

    print('-------------------------------------------')


def serieA():
    data = dict(http.get('clubes'))
    print('---------- Serie A ----------')

    for i in data:
        if data[i].get('posicao', '') == '':
            continue
        else:
            print(data[i]['nome'])

    print('-------------------------------------------')


def serieB():
    data = dict(http.get('clubes'))
    print('---------- Serie B ----------')
    for i in data:
        if data[i].get('posicao', '') != '':
            continue
        else:
            print(data[i]['nome'])

    print('-------------------------------------------')


def classificacao():
    data = dict(http.get('clubes'))
    print('---------- Classificação Serie A ----------')

    clubes = []

    for i in data:
        if data[i].get('posicao', '') == '':
            continue
        else:
            clubes.append(data[i])

    clubes = sorted(clubes, key=lambda k: k['posicao'])

    for i in clubes:
        print(str(i['posicao']) + 'º - ' + i['nome'])

    print('-------------------------------------------')


def partidas():
    data = dict(http.get('partidas'))

    clubes = []
    times = data['clubes']

    for i in times:
        time = {}

        time['nome'] = times[i]['nome']
        time['id'] = times[i]['id']
        clubes.append(time)

    partidas = data['partidas']

    print('---------- Partidas ----------')

    for i in partidas:
        mandante = equipe(clubes, i['clube_casa_id'])
        pos_mandante = i['clube_casa_posicao']

        visitante = equipe(clubes, i['clube_visitante_id'])
        pos_visitante = i['clube_visitante_posicao']

        local = i['local']

        print(str(pos_mandante) + 'º ' + mandante + ' x ' + str(pos_visitante) + 'º ' + visitante)

        data_partida = i['partida_data'][:-3]

        dataHora = data_partida.split(' ')
        num_datas = dataHora[0].split('-')

        data_partida = '(' + num_datas[2] + '/' + num_datas[1] + '/' + num_datas[0] + ' ' + dataHora[1] + ')'

        print('local:', local, data_partida)
        print('-  -  -  -  -  -   -  -  -  -  -  -  - ')

    print('------------------------------------------')


def equipe(clubes, id):
    for i in clubes:
        if id == i['id']:
            return i['nome']


def esquemas():
    data = http.get('esquemas')

    print('---------- Esquemas ----------')

    for i in data:
        print('Esquema:', i['nome'])
        taticas(i['nome'])

    print('-------------------------------------------')


def taticas(tatica):
    if tatica == '3-4-3':
        print('ATA    ATA    ATA')
        print('')
        print('MEI           MEI')
        print('')
        print('    MEI  MEI')
        print('')
        print('  ZAG  ZAG  ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '3-5-2':
        print('    ATA   ATA')
        print('')
        print('MEI           MEI')
        print('')
        print('    MEI  MEI')
        print('')
        print('       MEI')
        print('')
        print('  ZAG  ZAG  ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '4-3-3':
        print('ATA    ATA    ATA')
        print('')
        print('MEI    MEI     MEI')
        print('')
        print('ZAG  ZAG ZAG  ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '4-4-2':
        print('    ATA   ATA')
        print('')
        print('MEI MEI MEI MEI')
        print('')
        print('ZAG ZAG ZAG ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '4-5-1':
        print('       ATA')
        print('')
        print('MEI  MEI MEI  MEI')
        print('')
        print('       MEI')
        print('')
        print('ZAG  ZAG ZAG  ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '5-3-2':
        print('    ATA     ATA')
        print('')
        print('    MEI MEI MEI')
        print('')
        print('ZAG ZAG ZAG ZAG ZAG')
        print('')
        print('       GOL')
        print('---------------')
    elif tatica == '5-4-1':
        print('       ATA')
        print('')
        print('  MEI MEI MEI MEI')
        print('')
        print('ZAG ZAG ZAG ZAG ZAG')
        print('')
        print('       GOL')
        print('---------------')