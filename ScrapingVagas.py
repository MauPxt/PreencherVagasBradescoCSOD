import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

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

# Obtendo e manipulando o código fonte da página
pagina_inicial = navegador.page_source

# Para obter o ultimo botão:
pagina_gambiarra = BeautifulSoup(pagina_inicial, 'html.parser')
ultima_pagina = pagina_gambiarra.find(
    'ol', attrs={'class': 'page-number-list'})
ultimo_botao = ultima_pagina.findAll('button')[-1]
ultimo_botao = ultimo_botao.text
ultimo_botao = int(ultimo_botao)

# Passando as páginas
print('Obtendo conteúdo da página...')
time.sleep(0.5)
navegador.find_element_by_class_name('c-btn').click()
# Variável criada para servir de parametro pra passar a página
numero_pagina = 0

# GAMBIARRA! ---- INICIO
paginas = []

while numero_pagina != ultimo_botao:
    print('Passando para a proxima página...')
    navegador.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/\
            div/div/div[2]/div[2]/div/div/div[2]/div/\
                span/div/div/nav/button[2]').click()
    time.sleep(5)
    pagina_atual = navegador.page_source
    paginas.append([pagina_atual])
    numero_pagina = numero_pagina + 1

print('A ultima página configurada é a 3. \
    A última página atual é a: ', ultimo_botao)
site1 = pagina_gambiarra
site2 = BeautifulSoup(str(paginas[0]), 'html.parser')
site3 = BeautifulSoup(str(paginas[1]), 'html.parser')

# Lista para encaixar as vagas
dados_vagas = []

# Fazendo uma busca no código fonte para procurar o label das vagas
print('Buscando as vagas...')
time.sleep(0.5)
vagas1 = site1.find('div', attrs={'class': 'p-view-jobsearchresults'})
vagas2 = site2.find('div', attrs={'class': 'p-view-jobsearchresults'})
vagas3 = site3.find('div', attrs={'class': 'p-view-jobsearchresults'})

# Coletar as vagas uma por uma
for vaga in vagas1:

    vaga_info = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_url = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_local = vaga.find('p', attrs={'data-tag': 'displayJobLocation'})

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

for vaga in vagas2:

    vaga_info = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_url = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_local = vaga.find('p', attrs={'data-tag': 'displayJobLocation'})

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

for vaga in vagas3:

    vaga_info = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_url = vaga.find('a', attrs={'data-tag': 'displayJobTitle'})

    vaga_local = vaga.find('p', attrs={'data-tag': 'displayJobLocation'})

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

# GAMBIARRA! ---- FIM

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
