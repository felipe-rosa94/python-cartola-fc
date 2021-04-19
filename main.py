import inputs
import functions as f


def main():
    print(' ----------- Cartola ----------- ')
    sair = 'n'

    while sair != 's':
        print('1) Listar todos os clubes')
        print('2) Serie A')
        print('3) Outros clubes')
        print('4) Classificação brasileirão')
        print('5) Próximas partidas')
        print('6) Esquemas tácitos')

        opc = inputs.opcoes(['1', '2', '3', '4', '5', '6'], 'Digite a opção desejada: ')

        if opc == '1':
            f.listarClubes()
        elif opc == '2':
            f.serieA()
        elif opc == '3':
            f.serieB()
        elif opc == '4':
            f.classificacao()
        elif opc == '5':
            f.partidas()
        elif opc == '6':
            f.esquemas()


if __name__ == '__main__':
    main()
