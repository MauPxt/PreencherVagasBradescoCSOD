import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd


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


def coletareentrarnosites():
    # Configurações iniciais.
    options = Options()
    # options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    navegador = webdriver.Chrome(options=options)

    # -----------------------# Parte 1 - Efetuar login
    print('Entrando no site...')
    # ENTRAR NO SITE DO BRADESCO CSOD
    navegador.get(
        "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco&lang=pt-BR")
    time.sleep(5)

    # BOTAO DE COOKIE
    try:
        navegador.find_element(By.CLASS_NAME, 'c-btn').click()
        time.sleep(0.5)
    except Exception:
        pass

    print('Iniciando processo de login...')

    # BOTAO ENTRAR
    navegador.find_element(By.XPATH, '//*[@id="cs-root"]/div/div[1]/div[1]/span/div/\
            div/div/div/div/div/div/div[2]/a').click()

    # E-MAIL LOGIN
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_txtEmail"]').send_keys(login_email)
    time.sleep(0.5)

    # SENHA
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_txtPassword"]').send_keys(senha_email)
    time.sleep(0.5)

    # BOTAO LOGIN
    navegador.find_element(
        By.XPATH, '//*[@id="ctl00_siteContent_btnSignIn"]').send_keys(Keys.ENTER)
    time.sleep(5)

    print('Login concluído com sucesso!')

    # Lendo o arquivo excel que contém os links
    print('Verificando existência de vagas...')
    data = pd.read_excel('VagasBradesco.xlsx')

    # Iniciando a rotina
    for i, url in enumerate(data['URL']):
        tipo_de_vaga = data.loc[i, "Título"]
        navegador.get(url)
        time.sleep(5)
        print('Vaga encontrada!\n Iniciando processo de preenchimento da vaga...')

        # Página cadastro
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="applyNowButton"]').click()
        time.sleep(5)

        # ----------------------- #
        # --- PRIMEIRA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')
        # BOTAO DE COOKIE
        try:
            navegador.find_element(By.CLASS_NAME, 'c-btn').click()
            time.sleep(0.5)
        except Exception:
            pass

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()
        time.sleep(5)

        # ----------------------- #
        # --- SEGUNDA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        # CPF
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            cpf)
        time.sleep(0.5)

        # RG
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            rg)
        time.sleep(0.5)

        # BOTÃO ESTADO
        botao_estado = navegador.find_element(By.XPATH,
                                              '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                              '2]/div/div/div/div/div[ '
                                              '2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[5]/span')
        navegador.execute_script("arguments[0].click();", botao_estado)
        time.sleep(0.5)

        # DATA DE NASCIMENTO
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/input').send_keys(
            nascimento)
        time.sleep(0.5)

        # IDADE
        navegador.find_element(By.XPATH,
                               '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                               '2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
            idade)
        time.sleep(0.5)

        # FAIXA ETÁRIA
        botao_faixa_etaria = navegador.find_element(By.XPATH,
                                                    '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                    '2]/div/div/div/div/div[ '
                                                    '2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/label['
                                                    '3]/span')
        navegador.execute_script("arguments[0].click();", botao_faixa_etaria)
        time.sleep(0.5)

        # DEFICIENCIA
        botao_deficiencia = navegador.find_element(By.XPATH,
                                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                   '2]/div/div/div/div/div[ '
                                                   '2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[2]/span')
        navegador.execute_script("arguments[0].click();", botao_deficiencia)
        time.sleep(0.5)

        if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            # Possui outra fonte de renda que não seja trabalho assalariado (CLT) atualmente? #ESTÁGIO
            botao_assalariado = navegador.find_element(By.XPATH,
                                                       '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                       '1]/div/div/div[2]/div/div/div/div/div['
                                                       '2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label['
                                                       '2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_assalariado)
            time.sleep(0.5)

            # Possui participação societária em alguma empresa? #ESTÁGIO
            botao_societaria = navegador.find_element(By.XPATH,
                                                      '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[9]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_societaria)
            time.sleep(0.5)

        if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            # Como você se auto identifica?
            botao_auto_declaracao = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[10]/div/div/div/div/div[3]/div/label[5]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_auto_declaracao)
            time.sleep(0.5)

            # Confirme o seu nível de escolaridade atual
            botao_escolaridade_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[11]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_escolaridade_escriturario)
            time.sleep(0.5)

            # Situação do Ensino Superior
            botao_situação_ensino_superior_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[12]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino_superior_escriturario)
            time.sleep(0.5)

            # Qual das opções abaixo melhor descreve o seu curso superior?
            botao_area_curso_superior = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[13]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_area_curso_superior)
            time.sleep(0.5)

            # Estudou na Fundação Bradesco?
            botao_estudou_fundacao_bradesco_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[14]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estudou_fundacao_bradesco_escriturario)
            time.sleep(0.5)

            # Possui alguma das certificações abaixo?
            botoa_certificacao_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[15]/div/div/div/div/fieldset/div[3]/div/div/div/label/div')
            navegador.execute_script(
                "arguments[0].click();", botoa_certificacao_escriturario)
            time.sleep(0.5)

            # Possui experiència anterior no setor financeiro?
            botao_experiencia_setor_financeiro = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[16]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_experiencia_setor_financeiro)
            time.sleep(0.5)

            # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
            botao_atuou_estagiario_fundacao_bradesco_escriturario = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[17]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_atuou_estagiario_fundacao_bradesco_escriturario)
            time.sleep(0.5)

            # Qual a distância aproximada da sua residência até o local da vaga?
            botao_distancia = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[18]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script("arguments[0].click();", botao_distancia)
            time.sleep(0.5)

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()
        time.sleep(5)

        # ----------------------- #
        # --- TERCEIRA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        if tipo_de_vaga.__contains__('APRENDIZ'):
            # Confirme o seu nível de escolaridade atual
            botao_escolaridade = navegador.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_escolaridade)
            time.sleep(0.5)

            # Estuda ou concluiu o ensino médio em Instituição de Ensino:
            botao_situação_ensino = navegador.find_element(By.XPATH,
                                                           '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[2]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino)
            time.sleep(0.5)

            # ESTUDOU NA FUNDAÇÃO BRADESCO?
            botao_fundacao_bradesco = navegador.find_element(By.XPATH,
                                                             '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_fundacao_bradesco)
            time.sleep(0.5)

            # Já trabalhou como Aprendiz?
            botao_aprendiz = navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[4]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_aprendiz)
            time.sleep(0.5)

        if tipo_de_vaga.__contains__('ESTÁGIO'):
            # Confirme o seu nível de escolaridade atual
            botao_nivel_escolaridade = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[3]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_nivel_escolaridade)
            time.sleep(0.5)

            # Informe o nome do curso
            navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(nome_do_curso)
            time.sleep(0.5)

            # Situação do Ensino Superior
            botao_situação_ensino_superior = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[3]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_situação_ensino_superior)
            time.sleep(0.5)

            # Ano de término
            navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(ano_conclusao)
            time.sleep(0.5)

            # Estudou na Fundação Bradesco?
            botao_estudou_fundacao_bradesco = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[5]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estudou_fundacao_bradesco)
            time.sleep(0.5)

            # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
            botao_atuou_estagiario_fundacao_bradesco = navegador.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_atuou_estagiario_fundacao_bradesco)
            time.sleep(0.5)

        if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
            # NOME COMPLETO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_mae)
            time.sleep(0.5)

            # DATA DE NASCIMENTO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_mae)
            time.sleep(0.5)

            # PROFISSAO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_mae)
            time.sleep(0.5)

            # NOME COMPLETO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_pai)
            time.sleep(0.5)

            # DATA DE NASCIMENTO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_pai)
            time.sleep(0.5)

            # PROFISSAO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_pai)
            time.sleep(0.5)

            # ESTADO CIVIL
            botao_estado_civil = navegador.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label[1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estado_civil)
            time.sleep(0.5)

            # Algum parente ou conhecido que trabalha na Organização Bradesco te indicou para trabalhar conosco?
            botao_parente_bradesco_escriturario = navegador.find_element(By.XPATH,
                                                                         '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label[2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_parente_bradesco_escriturario)
            time.sleep(0.5)

        print('Passando para a proxima página...')
        # PRÓXIMA PÁGINA
        navegador.find_element(By.CSS_SELECTOR,
                               'button[type="button"][data-tag="btnNext"]').click()
        time.sleep(5)

        # ----------------------- #
        # --- QUARTA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__('APRENDIZ'):
            # NOME COMPLETO MAE
            navegador.find_element(By.XPATH,
                                   '/ html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                   '2]/div/div/div/div/div[ '
                                   '2]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_mae)
            time.sleep(0.5)

            # DATA DE NASCIMENTO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_mae)
            time.sleep(0.5)

            # PROFISSAO MAE
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[3]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_mae)
            time.sleep(0.5)

            # NOME COMPLETO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[4]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                nome_pai)
            time.sleep(0.5)

            # DATA DE NASCIMENTO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[5]/div/div/div/div/div[3]/div/div/div/input').send_keys(
                nascimento_pai)
            time.sleep(0.5)

            # PROFISSAO PAI
            navegador.find_element(By.XPATH,
                                   '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div['
                                   '2]/div/div/div/div/span[6]/div/div/div/div/div[3]/div/div/div/div/div/div/input').send_keys(
                profissao_pai)
            time.sleep(0.5)

            # ESTADO CIVIL
            botao_estado_civil = navegador.find_element(By.XPATH,
                                                        '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                        '2]/div/div/div/div/div[ '
                                                        '2]/div/div/div/div/span[7]/div/div/div/div/div[3]/div/label['
                                                        '1]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_estado_civil)
            time.sleep(0.5)

            # DISPENSA MILITAR
            botao_dispensa_militar = navegador.find_element(By.XPATH,
                                                            '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                            '1]/div/div/div[2]/div/div/div/div/div[ '
                                                            '2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label['
                                                            '2]/span')
            navegador.execute_script(
                "arguments[0].click();", botao_dispensa_militar)
            time.sleep(0.5)

            # PARENTE BRADESCO #Estágio
            if tipo_de_vaga.__contains__('ESTÁGIO'):
                botao_parente_bradesco_estagio = navegador.find_element(By.XPATH,
                                                                        '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[8]/div/div/div/div/div[3]/div/label[2]/span')
                navegador.execute_script(
                    "arguments[0].click();", botao_parente_bradesco_estagio)
                time.sleep(0.5)

            # PARENTE BRADESCO #Aprendiz
            if tipo_de_vaga.__contains__('APRENDIZ'):
                botao_parente_bradesco_aprendiz = navegador.find_element(By.XPATH,
                                                                         '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[9]/div/div/div/div/div[3]/div/label[2]/span')
                navegador.execute_script(
                    "arguments[0].click();", botao_parente_bradesco_aprendiz)
                time.sleep(0.5)

            print('Passando para a proxima página...')
            # PRÓXIMA PÁGINA
            navegador.find_element(By.CSS_SELECTOR,
                                   'button[type="button"][data-tag="btnNext"]').click()
            time.sleep(5)

        # ----------------------- #
        # --- QUINTA PÁGINA --- #
        # ----------------------- #
        print('Preenchendo campos da página atual...')

        # Está participando de algum outro Processo Seletivo na Organização Bradesco?
        botao_processo_seletivo = navegador.find_element(By.XPATH,
                                                         '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                         '1]/div/div/div[2]/div/div/div/div/div[ '
                                                         '2]/div/div/div/div/span[1]/div/div/div/div/div['
                                                         '3]/div/label[1]/span')
        navegador.execute_script(
            "arguments[0].click();", botao_processo_seletivo)
        time.sleep(0.5)

        # Como soube das oportunidades de construir sua carreira na Organização Bradesco?
        botao_soube_carreira = navegador.find_element(By.XPATH,
                                                      '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                                                      '1]/div/div/div[2]/div/div/div/div/div[ '
                                                      '2]/div/div/div/div/span[2]/div/div/div/div/div[3]/div/label['
                                                      '1]/span')
        navegador.execute_script("arguments[0].click();", botao_soube_carreira)
        time.sleep(0.5)

        # Como foi a sua experiência ao utilizar o site e realizar o processo de candidatura?
        botao_feedback = navegador.find_element(By.XPATH,
                                                '/html/body/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div['
                                                '2]/div/div/div/div/div[ '
                                                '4]/div/div/div/div/span[1]/div/div/div/div/div[3]/div/label[5]/span')
        navegador.execute_script("arguments[0].click();", botao_feedback)
        time.sleep(0.5)

        # BOTÃO ENVIAR!
        # navegador.find_element(By.CSS_SELECTOR, 'button[type="button"][data-tag="btnSubmit"]').click()
        # time.sleep(5)

        print(f'O preenchimento da vaga {i+1} foi concluído com sucesso!')

    print('Processo de preenchimento de formulários, foi conluído com sucesso!')


if __name__ == '__main__':
    coletareentrarnosites()
