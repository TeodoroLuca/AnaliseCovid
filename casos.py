from colorama import Fore
import os

with open("/home/theodoro/Desktop/analise/casos.csv", 'r', encoding='iso8859-1') as casos: # Abrindo o arquivo CSV com encoding iso8859-1: alfabeto latino
    numero_casos_confirmados = []
    total_confirmados = 0
    
    for linha in casos:
        caso = linha.strip().split(';')  # Remove espaços em branco e dividir por ';'
        if "CONFIRMADO" in caso[1] and caso[4].strip() == "XAXIM":  # Verificar se é confirmado e se o bairro é o pedido
            print(Fore.WHITE,"DATA DE ATENDIMENTO:", caso[0],Fore.GREEN, "COVID:", caso[1],Fore.RED, "BAIRRO:", caso[4]) # imprimi cada coluna solicitada
            total_confirmados += 1 # faz o incremento de casos e retorna o total
    os.system('clear')
    print(Fore.BLUE,f"\nTOTAL DE CASOS CONFIRMADOS NO BAIRRO CIDADE INDUSTRIAL DE CURITIBA: {total_confirmados}\n") # printa o total de casos de um bairro especifico
