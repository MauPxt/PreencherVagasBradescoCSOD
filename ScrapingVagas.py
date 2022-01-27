import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


def obtervagas():
    # Configurações do selenium
    options = Options()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    navegador = webdriver.Chrome(options=options)

    # Entrando no site e esperando 5 segundos
    print('Entrando no site...')
    navegador.get(
        "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco&lang=pt-BR")
    time.sleep(5)

    # Botão cookie
    try:
        navegador.find_element_by_class_name('c-btn').click()
        time.sleep(0.5)
    except Exception:
        pass

    # Obtendo o último botão de passar a página
    pagina_inicial = navegador.page_source
    pagina_inicial = BeautifulSoup(pagina_inicial, 'html.parser')
    ultima_pagina = pagina_inicial.find(
        'ol', attrs={'class': 'page-number-list'})
    ultimo_botao = ultima_pagina.findAll('button')[-1]
    ultimo_botao = ultimo_botao.text
    ultimo_botao = int(ultimo_botao)

    # Variável criada para servir de parâmetro para passar a página
    numero_pagina = 0

    # Lista para encaixar as vagas
    dados_vagas = []

    while numero_pagina != ultimo_botao:
        pagina_atual = navegador.page_source
        site_geral = BeautifulSoup(pagina_atual, 'html.parser')
        vagas_geral = site_geral.find(
            'div', attrs={'class': 'p-view-jobsearchresults'})
        print('Buscando as vagas...')
        time.sleep(0.5)
        for vaga in vagas_geral:
            vaga_info = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})
            vaga_url = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})
            vaga_local = vaga.find(
                'p', attrs={'data-tag': 'displayJobLocation'})
            if vaga_info:
                vaga_info = vaga_info.text
            else:
                vaga_info = 'vazio'

            if vaga_url:
                vaga_url = 'https://bradesco.csod.com' + vaga_url['href']
            else:
                vaga_url = 'vazio'

            if vaga_local:
                vaga_local = vaga_local.text
            else:
                vaga_local = 'vazio'

            dados_vagas.append([vaga_info, vaga_local, vaga_url])

        print('Passando para a proxima página...')
        navegador.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/\
                div/div/div[2]/div[2]/div/div/div[2]/div/\
                    span/div/div/nav/button[2]').click()
        numero_pagina = numero_pagina + 1
        time.sleep(3)

    # Transformando os dados da lista em um dataframe e filtrando o local
    df = pd.DataFrame(dados_vagas, columns=['Título', 'Local', 'URL'])
    dados = df[df['Local'].str.contains('Brasil')]
    dados = dados[df['Título'].str.contains('APRENDIZ|ESTÁGIO|ESCRITURÁRIO')]
    dados = dados[~df['Título'].str.contains('PCD')]

    print('Criando arquivo excel...')
    time.sleep(0.5)
    # Convertendo para um arquivo excel
    dados.to_excel('VagasBradesco.xlsx')
    print('Concluído!')


if __name__ == '__main__':
    obtervagas()
