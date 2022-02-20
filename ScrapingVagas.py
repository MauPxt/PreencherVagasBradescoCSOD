import time
import warnings
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore")


def obtervagas():
    ##########################################################################
    # Configurações do selenium
    options = Options()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('log-level=3')
    navegador = webdriver.Chrome(options=options)

    # Entrando no site e esperando 5 segundos
    print('Entrando no site...')
    navegador.get(
        "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco&lang"
        "=pt-BR")
    WebDriverWait(navegador, 20).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[1]/div['
                   '2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[ '
                   '2]/div/span/div/div/nav/button[2]')))

    # Botão cookie
    try:
        navegador.find_element(By.CLASS_NAME, 'c-btn').click()
        time.sleep(0.5)
    except Exception:
        pass
    ##########################################################################
    # Obtendo o último botão de passar a página
    pagina_inicial = navegador.page_source
    pagina_inicial = BeautifulSoup(pagina_inicial, 'html.parser')
    ultima_pagina = pagina_inicial.find(
        'ol', attrs={'class': 'page-number-list'})
    ultimo_botao = ultima_pagina.findAll('button')[-1]
    ultimo_botao = ultimo_botao.text
    ultimo_botao = int(ultimo_botao)
    ##########################################################################
    # Variável criada para servir de parâmetro para passar a página
    numero_pagina = 1

    # Lista para encaixar as vagas
    dados_vagas = []

    while numero_pagina < ultimo_botao + 1:
        pagina_atual = navegador.page_source
        site_geral = BeautifulSoup(pagina_atual, 'html.parser')
        vagas_geral = site_geral.find(
            'div', attrs={'class': 'p-view-jobsearchresults'})
        print(
            f'Coletando e armazenando as vagas da página {numero_pagina}...')
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
        navegador.find_element(By.XPATH,
                               '/html/body/div[1]/div/div[1]/div['
                               '2]/div/div/div/div/div/div/div[2]/div[ '
                               '2]/div/div/div['
                               '2]/div/span/div/div/nav/button[2]').click()
        numero_pagina = numero_pagina + 1
        if numero_pagina == ultimo_botao + 1:
            print('Encontrada a última página!')
        time.sleep(3)
    ##########################################################################
    # Transformando os dados da lista em um dataframe e filtrando o local
    df = pd.DataFrame(dados_vagas, columns=['Título', 'Local', 'URL'])
    dados = df[df['Local'].str.contains('BRASIL', case=False)]
    dados = dados[df['Título'].str.contains('APRENDIZ|ESTAGIÁRIO|ESCRITURÁRIO',
                                            case=False)]
    dados = dados[~df['Título'].str.contains('PCD', case=False)]

    print('Criando arquivo excel...')
    # Convertendo para um arquivo excel
    dados.to_excel('VagasBradesco.xlsx', index=False)
    print('Concluído!')
    ##########################################################################


if __name__ == '__main__':
    obtervagas()
