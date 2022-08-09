import json

import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao realizar a requisição em: {}".format(url))

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("Erro ao fazer parsing")

def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)

lista = []

def listar_nome_paises(lista_de_paises):
    for pais in lista_de_paises:
        lista.append(pais['name'])
    return lista

lista_pais = []
lista_populacao = []
def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}:{}".format(pais['name'], pais['population']))
                lista_pais.append(pais['name'])
                lista_populacao.append(pais['population'])
            return lista_pais, lista_populacao
        else:
            print("Pais não encontrado")

lista_moedas = []
lista_codes = []
def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} | {}".format(moeda['name'], moeda['code']))
                    lista_moedas.append(moeda['name'])
                    lista_codes.append(moeda['code'])
                return lista_moedas, lista_codes
        else:
            print("Moeda não encontrada")