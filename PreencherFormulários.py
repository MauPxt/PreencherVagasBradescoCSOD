import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

warnings.filterwarnings("ignore")

login_email = input('Login e-mail: ')
senha_email = input('Senha e-mail: ')
cpf = input('CPF: *somente numeros')
rg = input('RG: *somente numeros')
nascimento = input('Data de nascimento: *formato dd/mm/aaaa')
idade = input('Idade: ')
nome_do_curso = input('Nome do curso: *ex: economia')
ano_conclusao = input('Ano de conclusão do curso: ')
nome_mae = input('Nome da mãe: ')
nascimento_mae = input('Data de nascimento da mãe: *formato dd/mm/aaaa')
profissao_mae = input('Profissão da mãe: ')
nome_pai = input('Nome do pai: ')
nascimento_pai = input('Data de nascimento do pai: *formato dd/mm/aaaa')
profissao_pai = input('Profissão do pai')


def enviarcurriculo():
    # Configurações do selenium
    options = Options()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('log-level=3')
    navegador = webdriver.Chrome(options=options)

    # -----------------------# Parte 1 - Efetuar login
    print('Entrando no site...')
    # ENTRAR NO SITE DO BRADESCO CSOD
    navegador.get(
        "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco&lang=pt-BR")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'c-btn')))

    # BOTAO DE COOKIE
    try:
        navegador.find_element(By.CLASS_NAME, 'c-btn').click()
        time.sleep(0.5)
    except Exception:
        pass

    print('Iniciando processo de login...')
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cs-root"]/div/div[1]/div[1]/span/div/\
            div/div/div/div/div/div/div[2]/a')))
    # BOTAO ENTRAR
    navegador.find_element(By.XPATH, '//*[@id="cs-root"]/div/div[1]/div[1]/span/div/\
            div/div/div/div/div/div/div[2]/a').click()
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_siteContent_txtEmail"]')))
    # E-MAIL LOGIN
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_txtEmail"]').send_keys(login_email)

    # SENHA
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_txtPassword"]').send_keys(senha_email)

    # BOTAO LOGIN
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_btnSignIn"]').send_keys(Keys.ENTER)

    print('Login concluído com sucesso!')

    # Lendo o arquivo excel que contém os links
    print('Verificando existência de vagas...')
    data = pd.read_excel('VagasBradesco.xlsx')

    # Iniciando a rotina
    for i, url in enumerate(data['URL']):
        tipo_de_vaga = data.loc[i, "Título"]
        navegador.get(url)
        WebDriverWait(navegador, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[type="button"][data-tag="applyNowButton"]')))
        print(
            f'Vaga {i} encontrada!\n Iniciando processo de preenchimento da vaga...')

        # Página cadastro
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="applyNowButton"]').click()
        WebDriverWait(navegador, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[type="button"][data-tag="btnNext"]')))

        # ----------------------- #
        # --- PRIMEIRA PÁGINA --- #
        # ----------------------- #

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()
        WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                           '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                                                           '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input')))

        # ----------------------- #
        # --- SEGUNDA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        # CPF
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            cpf)

        # RG
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            rg)

        # BOTÃO ESTADO
        botao_estado = navegador.find_element(By.XPATH,
                                              '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                              '2]/div/div/div/div/div[ '
                                              '2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[5]/span')
        navegador.execute_script("arguments[0].click();", botao_estado)

        # DATA DE NASCIMENTO
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/input').send_keys(
            nascimento)

        # IDADE
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            idade)

        # FAIXA ETÁRIA
        botao_faixa_etaria = navegador.find_element(By.XPATH,
                                                    '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                    '2]/div/div/div/div/div[ '
                                                    '2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/label['
                                                    '3]/span')
        navegador.execute_script("arguments[0].click();", botao_faixa_etaria)

        # DEFICIENCIA
        botao_deficiencia = navegador.find_element(By.XPATH,
                                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                   '2]/div/div/div/div/div[ '
                                                   '2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[2]/span')
        navegador.execute_script("arguments[0].click();", botao_deficiencia)

        if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            # Possui outra fonte de renda que não seja trabalho assalariado (CLT) atualmente? #ESTÁGIO
            botao_assalariado = navegador.find_element(By.XPATH,
                                                       '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                       '1]/div/div/div[2]/div/div/div/div/div['
                                                       '2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label['
                                                       '2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_assalariado)

            # Possui participação societária em alguma empresa? #ESTÁGIO
            botao_societaria = navegador.find_element(By.XPATH,
                                                      '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[9]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_societaria)

        if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            # Como você se auto identifica?
            botao_auto_declaracao = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[10]/div/div/div/div/div[3]/div/label[5]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_auto_declaracao)

            # Confirme o seu nível de escolaridade atual
            botao_escolaridade_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[11]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_escolaridade_escriturario)

            # Situação do Ensino Superior
            botao_situação_ensino_superior_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[12]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino_superior_escriturario)

            # Qual das opções abaixo melhor descreve o seu curso superior?
            botao_area_curso_superior = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[13]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_area_curso_superior)

            # Estudou na Fundação Bradesco?
            botao_estudou_fundacao_bradesco_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[14]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estudou_fundacao_bradesco_escriturario)

            # Possui alguma das certificações abaixo?
            botoa_certificacao_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[15]/div/div/div/div/fieldset/div[3]/div/div/div/label/div')
            navegador.execute_script(
                "arguments[0].click();", botoa_certificacao_escriturario)

            # Possui experiència anterior no setor financeiro?
            botao_experiencia_setor_financeiro = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[16]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_experiencia_setor_financeiro)

            # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
            botao_atuou_estagiario_fundacao_bradesco_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[17]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_atuou_estagiario_fundacao_bradesco_escriturario)

            # Qual a distância aproximada da sua residência até o local da vaga?
            botao_distancia = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[18]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script("arguments[0].click();", botao_distancia)

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()

        # ----------------------- #
        # --- TERCEIRA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        if tipo_de_vaga.__contains__('APRENDIZ'):
            WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                               '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')))
            # Confirme o seu nível de escolaridade atual
            botao_escolaridade = navegador.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_escolaridade)

            # Estuda ou concluiu o ensino médio em Instituição de Ensino:
            botao_situação_ensino = navegador.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[2]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino)

            # ESTUDOU NA FUNDAÇÃO BRADESCO?
            botao_fundacao_bradesco = navegador.find_element(By.XPATH,
                                                             '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_fundacao_bradesco)

            # Já trabalhou como Aprendiz?
            botao_aprendiz = navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[4]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_aprendiz)

        if tipo_de_vaga.__contains__('ESTÁGIO'):
            WebDriverWait(navegador, 20).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')))
            # Confirme o seu nível de escolaridade atual
            botao_nivel_escolaridade = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_nivel_escolaridade)

            # Informe o nome do curso
            navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(nome_do_curso)

            # Situação do Ensino Superior
            botao_situação_ensino_superior = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino_superior)

            # Ano de término
            navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(ano_conclusao)

            # Estudou na Fundação Bradesco?
            botao_estudou_fundacao_bradesco = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[5]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estudou_fundacao_bradesco)

            # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
            botao_atuou_estagiario_fundacao_bradesco = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_atuou_estagiario_fundacao_bradesco)

        if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                               '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input')))
            # NOME COMPLETO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_mae)

            # DATA DE NASCIMENTO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_mae)

            # PROFISSAO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_mae)

            # NOME COMPLETO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_pai)

            # DATA DE NASCIMENTO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_pai)

            # PROFISSAO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_pai)

            # ESTADO CIVIL
            botao_estado_civil = navegador.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estado_civil)

            # Algum parente ou conhecido que trabalha na Organização Bradesco te indicou para trabalhar conosco?
            botao_parente_bradesco_escriturario = navegador.find_element(By.XPATH,
                                                                         '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_parente_bradesco_escriturario)

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()

        # ----------------------- #
        # --- QUARTA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__('APRENDIZ'):
            WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                               '/ html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                                               '2]/div/div/div/div/div[ '
                                                                               '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input')))
            # NOME COMPLETO MAE
            navegador.find_element(By.XPATH,
                                   '/ html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                   '2]/div/div/div/div/div[ '
                                   '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_mae)

            # DATA DE NASCIMENTO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_mae)

            # PROFISSAO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_mae)

            # NOME COMPLETO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_pai)

            # DATA DE NASCIMENTO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_pai)

            # PROFISSAO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_pai)

            # ESTADO CIVIL
            botao_estado_civil = navegador.find_element(By.XPATH,
                                                        '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                        '2]/div/div/div/div/div[ '
                                                        '2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label['
                                                        '1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estado_civil)

            # DISPENSA MILITAR
            botao_dispensa_militar = navegador.find_element(By.XPATH,
                                                            '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                            '1]/div/div/div[2]/div/div/div/div/div[ '
                                                            '2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label['
                                                            '2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_dispensa_militar)

            # PARENTE BRADESCO #Estágio
            if tipo_de_vaga.__contains__('ESTÁGIO'):
                botao_parente_bradesco_estagio = navegador.find_element(By.XPATH,
                                                                        '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label[2]/span')
                navegador.execute_script(
                    "arguments[0].click();", botao_parente_bradesco_estagio)

            # PARENTE BRADESCO #Aprendiz
            if tipo_de_vaga.__contains__('APRENDIZ'):
                botao_parente_bradesco_aprendiz = navegador.find_element(By.XPATH,
                                                                         '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[9]/div/div/div/div/div[3]/div/label[2]/span')
                navegador.execute_script(
                    "arguments[0].click();", botao_parente_bradesco_aprendiz)

            print('Passando para a proxima página...')
            # PRÓXIMA PÁGINA
            navegador.find_element(By.CSS_SELECTOR,
                                   'button[type="button"][data-tag="btnNext"]').click()
            WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                               '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                                               '1]/div/div/div[2]/div/div/div/div/div[ '
                                                                               '2]/div/div/div/div/span[1]/div/div/div/div/div['
                                                                               '3]/div/label[1]/span')))

        # ----------------------- #
        # --- QUINTA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                           '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                                           '1]/div/div/div[2]/div/div/div/div/div[ '
                                                                           '2]/div/div/div/div/span[1]/div/div/div/div/div['
                                                                           '3]/div/label[1]/span')))
        # Está participando de algum outro Processo Seletivo na Organização Bradesco?
        botao_processo_seletivo = navegador.find_element(By.XPATH,
                                                         '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                         '1]/div/div/div[2]/div/div/div/div/div[ '
                                                         '2]/div/div/div/div/span[1]/div/div/div/div/div['
                                                         '3]/div/label[1]/span')
        navegador.execute_script(
            "arguments[0].click();", botao_processo_seletivo)

        # Como soube das oportunidades de construir sua carreira na Organização Bradesco?
        botao_soube_carreira = navegador.find_element(By.XPATH,
                                                      '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                      '1]/div/div/div[2]/div/div/div/div/div[ '
                                                      '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/label['
                                                      '1]/span')
        navegador.execute_script("arguments[0].click();", botao_soube_carreira)

        # Como foi a sua experiência ao utilizar o site e realizar o processo de candidatura?
        botao_feedback = navegador.find_element(By.XPATH,
                                                '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                '2]/div/div/div/div/div[ '
                                                '4]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[5]/span')
        navegador.execute_script("arguments[0].click();", botao_feedback)

        # BOTÃO ENVIAR!
        # navegador.find_element(By.CSS_SELECTOR, 'button[type="button"][data-tag="btnSubmit"]').click()
        # time.sleep(5)

        print(f'O preenchimento da vaga {i+1} foi concluído com sucesso!')

    print('Processo de preenchimento de formulários, foi conluído com sucesso!')


if __name__ == '__main__':
    enviarcurriculo()
