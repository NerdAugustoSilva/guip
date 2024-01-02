#Bibliotecas
import requests, os
from urllib.request import urlopen
from time import sleep

#Limpando o terminal
os.system('clear')

# Lê o conteúdo do arquivo
with open("conf/cor.txt", "r") as arquivo:
    conteudo = arquivo.read()

if "vermelho" in conteudo:
    v = '\033[31m'
    b = '\033[39m'

if "verdeClaro" in conteudo:
    v = '\033[32m'
    b = '\033[39m'

if "amarelo" in conteudo:
    v = '\033[33m'
    b = '\033[39m'

if "azulClaro" in conteudo:
    v = '\033[34m'
    b = '\033[39m'

if "roxo" in conteudo:
    v = '\033[35m'
    b = '\033[39m'

if "ciano" in conteudo:
    v = '\033[36m'
    b = '\033[39m'

#Logo
#https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=blaip
print(f"""{v}

       Por NerdAugustoSilva

    ▄████  █    ██  ██▓ ██▓███
   ██▒ ▀█▒ ██  ▓██▒▓██▒▓██░  ██▒
  ▒██░▄▄▄░▓██  ▒██░▒██▒▓██░ ██▓▒
  ░▓█  ██▓▓▓█  ░██░░██░▒██▄█▓▒ ▒
  ░▒▓███▀▒▒▒█████▓ ░██░▒██▒ ░  ░
   ░▒   ▒ ░▒▓▒ ▒ ▒ ░▓  ▒▓▒░ ░  ░
    ░   ░ ░░▒░ ░ ░  ▒ ░░▒ ░
  ░ ░   ░  ░░░ ░ ░  ▒ ░░░
        ░    ░      ░""")

while True:
    with open("conf/cor.txt", "r") as arquivo:
        conteudo = arquivo.read()

    if "vermelho" in conteudo:
        v = '\033[31m'
        b = '\033[39m'

    if "verdeClaro" in conteudo:
        v = '\033[32m'
        b = '\033[39m'

    if "amarelo" in conteudo:
        v = '\033[33m'
        b = '\033[39m'

    if "azulClaro" in conteudo:
        v = '\033[34m'
        b = '\033[39m'

    if "roxo" in conteudo:
        v = '\033[35m'
        b = '\033[39m'

    if "ciano" in conteudo:
        v = '\033[36m'
        b = '\033[39m'

    #Menu
    print('')
    print(f'  {v}a) {b}Meu IP')
    print(f'  {v}b) {b}Rastrear IP')
    print(f'  {v}c) {b}Personalizar')
    print(f'  {v}d) {b}Limpar tela')
    print(f'  {v}e) {b}Sair')
    print('')
    l = input(f'{v}Opção: {b}')

    letras_predefinidas = {'a', 'b', 'c', 'd', 'e'}

    if any(letra in l for letra in letras_predefinidas):
                #Opção a)
        if l == 'a':
            print('')
            try:
                ip = requests.get('https://api.ipify.org').text
                if ip:
                    url = f'http://ip-api.com/json/{ip}'
                    request = urlopen(url)
                    data = request.read().decode()
                    data = eval(data)
                    print(f'  {v}============== Meu IP ==============')
                    print('')
                    print(f'  IP               =  {b}{ip}')
                    print(f'  {v}País             = {b}', data['country'])
                    print(f'  {v}Sigla do País    = {b}', data['countryCode'])
                    print(f'  {v}Estado           = {b}', data['regionName'])
                    print(f'  {v}Sigla do Estado  = {b}', data['region'])
                    print(f'  {v}Cidade           = {b}', data['city'])
                    print(f'  {v}Latitude         = {b}', data['lat'])
                    print(f'  {v}Longitude        = {b}', data['lon'])
                    print(f'  {v}Provedor         = {b}', data['isp'])
                    print('')
                    print(f'  {v}========== Resetando Menu ==========')
            except:
                print(f'{v}Sem conexão!')

        #Opção b)
        if l == 'b':
            print('')
            ip = input(f'{v}Digite o IP: {b}')
            print('')
            if ip:
                try:
                    url = f'http://ip-api.com/json/{ip}'
                    request = urlopen(url)
                    data = request.read().decode()
                    data = eval(data)
                    print(f'  {v}============ Rastrear IP ===========')
                    print('')
                    try:
                        print(f'  {v}País             = {b}', data['country'])
                        print(f'  {v}Sigla do País    = {b}', data['countryCode'])
                        print(f'  {v}Estado           = {b}', data['regionName'])
                        print(f'  {v}Sigla do Estado  = {b}', data['region'])
                        print(f'  {v}Cidade           = {b}', data['city'])
                        print(f'  {v}Latitude         = {b}', data['lat'])
                        print(f'  {v}Longitude        = {b}', data['lon'])
                        print(f'  {v}Provedor         = {b}', data['isp'])
                    except:
                        print(f'  {v}Endereço inválido!')
                    print('')
                    print(f'  {v}========== Resetando Menu ==========')
                except:
                    print(f'{v}Sem conexão!')

        #Opção c)
        if l == 'c':
            print('')
            print(f'  {v}=========== personalizar ===========')
            print('')
            print(f'  {v}a) {b}Vermelho')
            print(f'  {v}b) {b}Verde Claro')
            print(f'  {v}c) {b}Amarelo')
            print(f'  {v}d) {b}Azul Claro')
            print(f'  {v}e) {b}Roxo')
            print(f'  {v}f) {b}Ciano')
            print('')
            cor = input(f'  {v}Opção: {b}')
            print('')

            letras_predefinidas = {'a', 'b', 'c', 'd', 'e', 'f'}

            if any(letra in cor for letra in letras_predefinidas):
                    if cor == 'a':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('vermelho')
                            print(f'  {v}Cor Alterada com sucesso!')

                    if cor == 'b':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('verdeClaro')
                            print(f'  {v}Cor Alterada com sucesso!')

                    if cor == 'c':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('amarelo')
                            print(f'  {v}Cor Alterada com sucesso!')

                    if cor == 'd':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('azulClaro')
                            print(f'  {v}Cor Alterada com sucesso!')

                    if cor == 'e':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('roxo')
                            print(f'  {v}Cor Alterada com sucesso!')

                    if cor == 'f':
                        with open("conf/cor.txt", "w") as arquivo:
                            arquivo.write('ciano')
                            print(f'  {v}Cor Alterada com sucesso!')

                    print('')
                    sleep(1.5)
                    os.system('clear')
                    if cor == 'a':
                        v = '\033[31m'
                        b = '\033[39m'

                    if cor == 'b':
                        v = '\033[32m'
                        b = '\033[39m'

                    if cor == 'c':
                        v = '\033[33m'
                        b = '\033[39m'

                    if cor == 'd':
                        v = '\033[34m'
                        b = '\033[39m'

                    if cor == 'e':
                        v = '\033[35m'
                        b = '\033[39m'

                    if cor == 'f':
                        v = '\033[36m'
                        b = '\033[39m'
                    print(f"""{v}

       Por NerdAugustoSilva

    ▄████  █    ██  ██▓ ██▓███
   ██▒ ▀█▒ ██  ▓██▒▓██▒▓██░  ██▒
  ▒██░▄▄▄░▓██  ▒██░▒██▒▓██░ ██▓▒
  ░▓█  ██▓▓▓█  ░██░░██░▒██▄█▓▒ ▒
  ░▒▓███▀▒▒▒█████▓ ░██░▒██▒ ░  ░
   ░▒   ▒ ░▒▓▒ ▒ ▒ ░▓  ▒▓▒░ ░  ░
    ░   ░ ░░▒░ ░ ░  ▒ ░░▒ ░
  ░ ░   ░  ░░░ ░ ░  ▒ ░░░
        ░    ░      ░""")
            else:
                print(f"  {v}Opção inexistente!")
                print('')
                print(f'  {v}========== Resetando Menu ==========')

        #Opção d)
        if l == 'd':
            os.system('clear')
            print(f"""{v}

       Por NerdAugustoSilva

    ▄████  █    ██  ██▓ ██▓███
   ██▒ ▀█▒ ██  ▓██▒▓██▒▓██░  ██▒
  ▒██░▄▄▄░▓██  ▒██░▒██▒▓██░ ██▓▒
  ░▓█  ██▓▓▓█  ░██░░██░▒██▄█▓▒ ▒
  ░▒▓███▀▒▒▒█████▓ ░██░▒██▒ ░  ░
   ░▒   ▒ ░▒▓▒ ▒ ▒ ░▓  ▒▓▒░ ░  ░
    ░   ░ ░░▒░ ░ ░  ▒ ░░▒ ░
  ░ ░   ░  ░░░ ░ ░  ▒ ░░░
        ░    ░      ░""")
            

        #Opção e)
        if l == 'e':
            print('')
            exit()

    else:
        print('')
        print(f"{v}Opção inexistente!")
        