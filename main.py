import time
import warnings
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import getpass

warnings.filterwarnings("ignore")


class VagasBradesco:
    def __init__(self):
        # Configurações do selenium
        options = Options()
        options.add_experimental_option("detach", True)
        # options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('log-level=3')
        self.navegador = webdriver.Chrome(options=options)

    def enviar_curriculo(self):

        login_email = input('Login e-mail: >>> ')
        senha_email = getpass.getpass(
            prompt='Senha e-mail: *Não é possível visualizar, mas a senha '
                   'está sendo escrita >>> ', stream=None)
        cpf = input('CPF: *somente numeros >>> ')
        rg = input('RG: *somente numeros >>> ')
        nascimento = input('Data de nascimento: *formato dd/mm/aaaa >>> ')
        idade = input('Idade: >>> ')
        nome_do_curso = input('Nome do curso: *ex: economia >>> ')
        ano_conclusao = input('Ano de conclusão do curso: >>> ')
        nome_mae = input('Nome da mãe: >>> ')
        nascimento_mae = input(
            'Data de nascimento da mãe: *formato dd/mm/aaaa >>> ')
        profissao_mae = input('Profissão da mãe: >>> ')
        nome_pai = input('Nome do pai: >>> ')
        nascimento_pai = input(
            'Data de nascimento do pai: *formato dd/mm/aaaa >>> ')
        profissao_pai = input('Profissão do pai: >>> ')

        # -----------------------# Parte 1 - Efetuar login
        print('Entrando no site...')
        # ENTRAR NO SITE DO BRADESCO CSOD
        self.navegador.get(
            "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco"
            "&lang "
            "=pt-BR")
        WebDriverWait(self.navegador, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'c-btn')))
        time.sleep(3)
        # BOTAO DE COOKIE
        try:
            self.navegador.find_element(By.CLASS_NAME, 'c-btn').click()
            time.sleep(0.5)
        except Exception:
            pass

        print('Iniciando processo de login...')
        WebDriverWait(self.navegador, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cs-root"]/div'
                                            '/div[1]/div[1]/spa'
                                            'n/div/'
                                            'div/div/div/div/div/div'
                                            '/div[2]/a')))
        # BOTAO ENTRAR
        self.navegador.find_element(By.XPATH, '//*[@id="cs-root"]/div/div['
                                              '1]/div[ '
                                    '1]/span/div/ '
                                    'div/div/div/div/div/div/div['
                                    '2]/a').click()
        WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="ctl00_siteContent_txtEmail"]')))
        # E-MAIL LOGIN
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="ctl00_site'
                                    'Content_txtEmail"]').send_keys(
            login_email)

        # SENHA
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="ctl00_site'
                                    'Content_txtPassword"]').send_keys(
            senha_email)

        # BOTAO LOGIN
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="ctl00_siteContent_btnSignIn"]').send_keys(
            Keys.ENTER)

        print('Login concluído com sucesso!')
        ##########################################################################
        # Lendo o arquivo excel que contém os links
        print('Verificando existência de vagas...')
        data = pd.read_excel('VagasBradesco.xlsx')
        time.sleep(1)
        ##########################################################################
        # Iniciando a rotina
        for i, url in enumerate(data['URL']):
            tipo_de_vaga = data.loc[i, "Título"]
            self.navegador.get(url)
            WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                'button[type="button"][data-tag="applyNowButton"]')))
            print(
                f'Vaga {i + 1} encontrada!\n Iniciando processo de preenchimento '
                f'da vaga...')

            # Página cadastro
            self.navegador.find_element(By.CSS_SELECTOR, 'button[type="button"]['
                                        'data-tag="apply'
                                        'NowButton"]').click()
            WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[type="button"][data-tag="btnNext"]')))

            # ----------------------- #
            # --- PRIMEIRA PÁGINA --- #
            # ----------------------- #
            # BOTAO DE COOKIE
            try:
                self.navegador.find_element(By.CLASS_NAME, 'c-btn').click()
                time.sleep(0.5)
            except Exception:
                pass

            # PRÓXIMA PÁGINA
            self.navegador.find_element(By.CSS_SELECTOR,
                                        'button[type="button"]'
                                        '[data-tag="btnNext"]').click()
            WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/div['
                 '2]/div/div/div/div['
                 '1]/div/div/div[ '
                 '2]/div/div/div/div/div[ '
                 '2]/div/div/div/div/span['
                 '1]/div/div/div/div/div['
                 '3]/div/div/div/div/div/div/input')))

            # ----------------------- #
            # --- SEGUNDA PÁGINA --- #
            # ----------------------- #

            # CPF
            self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                        '2]/div/div/div/div[1]/div/div/div['
                                        '2]/div/div/div/div/div[ '
                                        '2]/div/div/div/div/span['
                                        '1]/div/div/div/div/div['
                                        '3]/div/div/div/'
                                        'div/div/div/input').send_keys(
                cpf)

            # RG
            self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                        '2]/div/div/div/div[1]/div/div/div['
                                        '2]/div/div/div/div/div[ '
                                        '2]/div/div/div/div/span['
                                        '2]/div/div/div/div/div['
                                        '3]/div/div/div/'
                                        'div/div/div/input').send_keys(
                rg)

            # BOTÃO ESTADO
            botao_estado = self.navegador.find_element(By.XPATH,
                                                       '/html/body/div/div/div['
                                                       '2]/div[2]/div/div/div/div['
                                                       '1]/div/div/div[ '
                                                       '2]/div/div/div/div/div[ '
                                                       '2]/div/div/div/div/span['
                                                       '3]/div/div/div/div/div['
                                                       '3]/div/label[5]/span')
            self.navegador.execute_script(
                "arguments[0].click();", botao_estado)

            # DATA DE NASCIMENTO
            self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                        '2]/div/div/div/div[1]/div/div/div['
                                        '2]/div/div/div/div/div[ '
                                        '2]/div/div/div/div/span['
                                        '4]/div/div/div/div/div['
                                        '3]/div/div/div/input').send_keys(
                nascimento)

            # IDADE
            self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                        '2]/div/div/div/div[1]/div/div/div['
                                        '2]/div/div/div/div/div[ '
                                        '2]/div/div/div/div/span['
                                        '5]/div/div/div/div/div['
                                        '3]/div/div/div/d'
                                        'iv/div/div/input').send_keys(
                idade)

            # FAIXA ETÁRIA
            botao_faixa_etaria = self.navegador.find_element(By.XPATH,
                                                             '/html/body/div/div/div['
                                                             '2]/div['
                                                             '2]/div/div/div/div['
                                                             '1]/div/div/div[ '
                                                             '2]/div/div/div/div/div[ '
                                                             '2]/div/div/div/div'
                                                             '/span['
                                                             '6]/div/div/div/div/div['
                                                             '3]/div/label[ '
                                                             '3]/span')
            self.navegador.execute_script(
                "arguments[0].click();", botao_faixa_etaria)

            # DEFICIENCIA
            botao_deficiencia = self.navegador.find_element(By.XPATH,
                                                            '/html/body/div/div/div['
                                                            '2]/div['
                                                            '2]/div/div/div/div['
                                                            '1]/div/div/div[ '
                                                            '2]/div/div/div/div/div[ '
                                                            '2]/div/div/div/div/span['
                                                            '7]/div/div/div/div/div['
                                                            '3]/div/label[2]/span')
            self.navegador.execute_script(
                "arguments[0].click();", botao_deficiencia)

            if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__(
                    'ESCRITURÁRIO'):
                # Possui outra fonte de renda que não seja trabalho assalariado
                # (CLT) atualmente? #ESTÁGIO
                botao_assalariado = self.navegador.find_element(By.XPATH,
                                                                '/html/body/div/div'
                                                                '/div[2]/div['
                                                                '2]/div/div/div/div[ '
                                                                '1]/div/div/div['
                                                                '2]/div/di'
                                                                'v/div/div/div[ '
                                                                '2]/div/div/div/div'
                                                                '/span['
                                                                '8]/div/div/div/div'
                                                                '/div[3]/div/label[ '
                                                                '2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_assalariado)

                # Possui participação societária em alguma empresa? #ESTÁGIO
                botao_societaria = self.navegador.find_element(By.XPATH,
                                                               '/html/body/div/div'
                                                               '/div[2]/div['
                                                               '2]/div/div/div/div['
                                                               '1]/div/div/div['
                                                               '2]/div/div/div/div'
                                                               '/div['
                                                               '2]/div/div/div/div'
                                                               '/span['
                                                               '9]/div/div/div/div'
                                                               '/div[3]/div/label['
                                                               '2]/span')
                self.navegador.execute_script(
                    "arguments[0].click();", botao_societaria)

            if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
                # Como você se auto identifica?
                botao_auto_declaracao = self.navegador.find_element(By.XPATH,
                                                                    '/html/body/div['
                                                                    '1]/div/div['
                                                                    '2]/div['
                                                                    '2]/div/div/div'
                                                                    '/div['
                                                                    '1]/div/div/div['
                                                                    '2]/div/div/div'
                                                                    '/div/div['
                                                                    '2]/div/div/div'
                                                                    '/div/span['
                                                                    '10]/div/div/div'
                                                                    '/div/div['
                                                                    '3]/div/label['
                                                                    '5]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_auto_declaracao)

                # Confirme o seu nível de escolaridade atual
                botao_escolaridade_escriturario = self.navegador.find_element(By.XPATH,
                                                                              '/html'
                                                                              '/body'
                                                                              '/div['
                                                                              '1]/div'
                                                                              '/div['
                                                                              '2]/div[2'
                                                                              ']/div/di'
                                                                              'v/div/di'
                                                                              'v[1]/di'
                                                                              'v/div/di'
                                                                              'v[2]/d'
                                                                              'iv/div'
                                                                              '/div/d'
                                                                              'iv/div[2'
                                                                              ']/div/'
                                                                              'div/div'
                                                                              '/div/sp'
                                                                              'an[11]'
                                                                              '/div/d'
                                                                              'iv/div/'
                                                                              'div/di'
                                                                              'v[3]/di'
                                                                              'v/label'
                                                                              '[3]/sp'
                                                                              'an')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_escolaridade_escriturario)

                # Situação do Ensino Superior
                botao_situacao_ensino_superior_escrit = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/'
                    'div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[12]/d'
                    'iv/div/div/div/div[3]/div/label[1]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_situacao_ensino_superior_escrit)

                # Qual das opções abaixo melhor descreve o seu curso superior?
                botao_area_curso_superior = self.navegador.find_element(By.XPATH,
                                                                        '/html/body/div'
                                                                        '[1]/div/div[2'
                                                                        ']/div[2]/div'
                                                                        '/div/div/div'
                                                                        '[1]/div/div/'
                                                                        'div[2]/div/d'
                                                                        'iv/div/div/d'
                                                                        'iv[2]/div/di'
                                                                        'v/div/div/sp'
                                                                        'an[13]/div/d'
                                                                        'iv/div/div/d'
                                                                        'iv[3]/div/la'
                                                                        'bel[1]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_area_curso_superior)

                # Estudou na Fundação Bradesco?
                botao_estudou_fundacao_bradesco_escrit = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/di'
                    'v/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span['
                    '14]/div/div/div/div/div[3]/div/label[2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_estudou_fundacao_bradesco_escrit)

                # Possui alguma das certificações abaixo?
                # botao_certificacao_escrit = self.navegador.find_element(By.XPATH,
                #                                                    '/html/body/div'
                #                                                    '/div/div[2]/di'
                #                                                    'v[2]/div/div/d'
                #                                                    'iv/div[1]/div'
                #                                                    '/d'
                #                                                    'iv/div[2]/div'
                #                                                    '/div/div/div/'
                #                                                    'div[2]/div/di'
                #                                                    'v/div/div/spa'
                #                                                    'n[14]/div/div/'
                #                                                    'div/div/fields'
                #                                                    'et/div[3]/div'
                #                                                    '/div/div/labe'
                #                                                    'l/div')
                # botao_certificacao_escrit.click()

                # Possui experiència anterior no setor financeiro?
                botao_experiencia_setor_financeiro = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/di'
                    'v/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[1'
                    '6]/div/div/div/div/div[3]/div/label[2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_experiencia_setor_financeiro)

                # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
                botao_atuou_estag_fundacao_brad_escrit = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div'
                    '/div/div[2]/div/div/div/div/div[2]/div/div/div/div/span[17]'
                    '/div/div/div/div/div[3]/div/label[2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_atuou_estag_fundacao_brad_escrit)

                # Qual a distância aproximada da sua residência até o local da
                # vaga?
                botao_distancia = self.navegador.find_element(By.XPATH,
                                                              '/html/body/div[1]/di'
                                                              'v/div[2]/div[2]/div/di'
                                                              'v/div/div[1]/div/div/d'
                                                              'iv[2]/div/div/div/div/'
                                                              'div[2]/div/div/div/div'
                                                              '/span[18]/div/div/div/'
                                                              'div/div[3]/div/label[1'
                                                              ']/span')
                self.navegador.execute_script(
                    "arguments[0].click();", botao_distancia)

            # PRÓXIMA PÁGINA
            self.navegador.find_element(By.CSS_SELECTOR,
                                        'button[type="button"][dat'
                                        'a-tag="btnNext"]').click()

            # ----------------------- #
            # --- TERCEIRA PÁGINA --- #
            # ----------------------- #

            if tipo_de_vaga.__contains__('APRENDIZ'):
                WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located((
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div['
                    '1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span['
                    '1]/div/div/div/div/div[3]/div/label[3]/span')))
                # Confirme o seu nível de escolaridade atual
                botao_escolaridade = self.navegador.find_element(By.XPATH,
                                                                 '/html/body/div['
                                                                 '1]/div/div[2]/div['
                                                                 '2]/div/div/div/div['
                                                                 '1]/div/div/div['
                                                                 '2]/div/div/div/div'
                                                                 '/div/div/div/div'
                                                                 '/div/span['
                                                                 '1]/div/div/div/div'
                                                                 '/div[3]/div/label['
                                                                 '3]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_escolaridade)

                # Estuda ou concluiu o ensino médio em Instituição de Ensino:
                botao_situacao_ensino = self.navegador.find_element(By.XPATH,
                                                                    '/html/body/div['
                                                                    '1]/div/div['
                                                                    '2]/div['
                                                                    '2]/div/div/div'
                                                                    '/div['
                                                                    '1]/div/div/div['
                                                                    '2]/div/div/div'
                                                                    '/div/div/div'
                                                                    '/div/div/div/'
                                                                    'span[2]/div/d'
                                                                    'iv/div/div/di'
                                                                    'v[3]/div/labe'
                                                                    'l[1]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_situacao_ensino)

                # ESTUDOU NA FUNDAÇÃO BRADESCO?
                botao_fundacao_bradesco = self.navegador.find_element(By.XPATH,
                                                                      '/html/body'
                                                                      '/div['
                                                                      '1]/div/div['
                                                                      '2]/div['
                                                                      '2]/div/div/di'
                                                                      'v/div[1]/div/'
                                                                      'div/div[2]/div'
                                                                      '/div/div/div/di'
                                                                      'v/div/div/div/d'
                                                                      'iv/span[3]/div'
                                                                      '/div/div/div/di'
                                                                      'v[3]/div/label['
                                                                      '2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_fundacao_bradesco)

                # Já trabalhou como Aprendiz?
                botao_aprendiz = self.navegador.find_element(By.XPATH,
                                                             '/html/body/div['
                                                             '1]/div/div[2]/div['
                                                             '2]/div/div/div/div['
                                                             '1]/div/div/div['
                                                             '2]/div/div/div/div/div'
                                                             '/div/div/div/div/span['
                                                             '4]/div/div/div/div/div['
                                                             '3]/div/label[2]/span')
                self.navegador.execute_script(
                    "arguments[0].click();", botao_aprendiz)

            if tipo_de_vaga.__contains__('ESTÁGIO'):
                WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located((
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div['
                    '1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span['
                    '1]/div/div/div/div/div[3]/div/label[3]/span')))
                # Confirme o seu nível de escolaridade atual
                botao_nivel_escolaridade = self.navegador.find_element(By.XPATH,
                                                                       '/html/body'
                                                                       '/div['
                                                                       '1]/div/div['
                                                                       '2]/div['
                                                                       '2]/div/div'
                                                                       '/div/div['
                                                                       '1]/div/div'
                                                                       '/div['
                                                                       '2]/div/div'
                                                                       '/div/div/div '
                                                                       '/div/div/div'
                                                                       '/div/span['
                                                                       '1]/div/div'
                                                                       '/div/div/div['
                                                                       '3]/div/label['
                                                                       '3]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_nivel_escolaridade)

                # Informe o nome do curso
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div['
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div/div/div/div/div'
                                            '/span[2]/div/div/div/div/div['
                                            '3]/div/div/div/div/div'
                                            '/div/input').send_keys(
                    nome_do_curso)

                # Situação do Ensino Superior
                botao_situacao_ensino_superior = self.navegador.find_element(By.XPATH,
                                                                             '/html'
                                                                             '/body'
                                                                             '/div['
                                                                             '1]/div'
                                                                             '/div['
                                                                             '2]/div['
                                                                             '2]/div/'
                                                                             'div/div'
                                                                             '/div[1]'
                                                                             '/div/di'
                                                                             'v/div[2'
                                                                             ']/div/d'
                                                                             'iv/div/'
                                                                             'div/div'
                                                                             '/div/di'
                                                                             'v/div/d'
                                                                             'iv/span'
                                                                             '[3]/div'
                                                                             '/div/di'
                                                                             'v/div/d'
                                                                             'iv[3]/d'
                                                                             'iv/labe'
                                                                             'l[1]/sp'
                                                                             'an')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_situacao_ensino_superior)

                # Ano de término
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div['
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div/div/div/div/div'
                                            '/span[4]/div/div/div/div/div['
                                            '3]/div/div/div/div/div'
                                            '/div/input').send_keys(
                    ano_conclusao)

                # Estudou na Fundação Bradesco?
                botao_estudou_fundacao_bradesco = self.navegador.find_element(By.XPATH,
                                                                              '/html'
                                                                              '/body'
                                                                              '/div['
                                                                              '1]/div'
                                                                              '/div['
                                                                              '2]/div'
                                                                              '[2]/d'
                                                                              'iv/div'
                                                                              '/div/d'
                                                                              'iv[1]/'
                                                                              'div/di'
                                                                              'v/div['
                                                                              '2]/div'
                                                                              '/div/d'
                                                                              'iv/div'
                                                                              '/div/d'
                                                                              'iv/div'
                                                                              '/div/d'
                                                                              'iv/spa'
                                                                              'n[5]/d'
                                                                              'iv/div'
                                                                              '/div/d'
                                                                              'iv/div'
                                                                              '[3]/di'
                                                                              'v/labe'
                                                                              'l[2]/s'
                                                                              'pan')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_estudou_fundacao_bradesco)

                # Já atuou como Estagiário ou Aprendiz na Organização Bradesco?
                botao_atuou_estagiario_fundacao_bradesco = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div['
                    '1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/span['
                    '7]/div/div/div/div/div[3]/div/label[2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_atuou_estagiario_fundacao_bradesco)

            if tipo_de_vaga.__contains__('ESCRITURÁRIO'):
                WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located((
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div['
                    '1]/div/div/div[2]/div/div/div/div/div['
                    '2]/div/div/div/div/span[1]/div/div/div/div/div['
                    '3]/div/div/div/div/div/div/input')))
                # NOME COMPLETO MAE
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div['
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '1]/div/div/div/div/div['
                                            '3]/div/div/div/div/d'
                                            'iv/div/input').send_keys(
                    nome_mae)

                # DATA DE NASCIMENTO MAE
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div['
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '2]/div/div/div/div/div['
                                            '3]/div/div/div/input').send_keys(
                    nascimento_mae)

                # PROFISSAO MAE
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div[ '
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '3]/div/div/div/div/div['
                                            '3]/div/div/di'
                                            'v/div/div/div/input').send_keys(
                    profissao_mae)

                # NOME COMPLETO PAI
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div[ '
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '4]/div/div/div/div/div['
                                            '3]/div/div/div/div'
                                            '/div/div/input').send_keys(
                    nome_pai)

                # DATA DE NASCIMENTO PAI
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div[ '
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '5]/div/div/div/div/div['
                                            '3]/div/div/div/input').send_keys(
                    nascimento_pai)

                # PROFISSAO PAI
                self.navegador.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div[2]/div[ '
                                            '2]/div/div/div/div[1]/div/div/div['
                                            '2]/div/div/div/div/div['
                                            '2]/div/div/div/div/span['
                                            '6]/div/div/div/div/div['
                                            '3]/div/div/div/d'
                                            'iv/div/div/input').send_keys(
                    profissao_pai)

                # ESTADO CIVIL
                botao_estado_civil = self.navegador.find_element(By.XPATH,
                                                                 '/html/body/div['
                                                                 '1]/div/div[2]/div['
                                                                 '2]/div/div/div/div['
                                                                 '1]/div/div/div['
                                                                 '2]/div/div/div/div'
                                                                 '/div['
                                                                 '2]/div/div/div/div'
                                                                 '/span['
                                                                 '7]/div/div/div/div '
                                                                 '/div[3]/div/label['
                                                                 '1]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_estado_civil)

                # Algum parente ou conhecido que trabalha na Organização
                # Bradesco te indicou para trabalhar conosco?
                botao_parente_bradesco_escriturario = self.navegador.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div['
                    '1]/div/div/div[2]/div/div/div/div/div['
                    '2]/div/div/div/div/span[8]/div/div/div/div/div['
                    '3]/div/label[2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_parente_bradesco_escriturario)

            # PRÓXIMA PÁGINA
            self.navegador.find_element(By.CSS_SELECTOR,
                                        'button[type="button"][d'
                                        'ata-tag="btnNext"]').click()

            # ----------------------- #
            # --- QUARTA PÁGINA --- #
            # ----------------------- #

            if tipo_de_vaga.__contains__('ESTÁGIO') or tipo_de_vaga.__contains__(
                    'APRENDIZ'):
                WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
                    (By.XPATH, '/ html/body/div/div/div['
                     '2]/div[2]/div/div/div/div['
                     '1]/div/div/div[ '
                     '2]/div/div/div/div/div[ '
                     '2]/div/div/div/div/span['
                     '1]/div/div/div/div/div['
                     '3]/div/div/div/div/div/div'
                     '/input')))
                # NOME COMPLETO MAE
                self.navegador.find_element(By.XPATH, '/ html/body/div/div/div[2]/div['
                                            '2]/div/div/div/'
                                            'div[1]/div/div/div[ '
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '1]/div/div/div/div/div['
                                            '3]/div/div/div/d'
                                            'iv/div/div/input').send_keys(
                    nome_mae)

                # DATA DE NASCIMENTO MAE
                self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                            '2]/div/div/div/d'
                                            'iv[1]/div/div/div['
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '2]/div/div/div/div/div['
                                            '3]/div/div/div/input').send_keys(
                    nascimento_mae)

                # PROFISSAO MAE
                self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                            '2]/div/div/di'
                                            'v/div[1]/div/div/div['
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '3]/div/div/div/div/div['
                                            '3]/div/div/div/di'
                                            'v/div/div/input').send_keys(
                    profissao_mae)

                # NOME COMPLETO PAI
                self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                            '2]/div/div/div/div['
                                            '1]/div/div/div[ '
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '4]/div/div/div/div/div['
                                            '3]/div/div/div/d'
                                            'iv/div/div/input').send_keys(
                    nome_pai)

                # DATA DE NASCIMENTO PAI
                self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                            '2]/div/div/div/div['
                                            '1]/div/div/div[ '
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '5]/div/div/div/div/div['
                                            '3]/div/div/div/input').send_keys(
                    nascimento_pai)

                # PROFISSAO PAI
                self.navegador.find_element(By.XPATH, '/html/body/div/div/div[2]/div['
                                            '2]/div/div/div/div['
                                            '1]/div/div/div[ '
                                            '2]/div/div/div/div/div[ '
                                            '2]/div/div/div/div/span['
                                            '6]/div/div/div/div/div['
                                            '3]/div/div/di'
                                            'v/div/div/div/input').send_keys(
                    profissao_pai)

                # ESTADO CIVIL
                botao_estado_civil = self.navegador.find_element(By.XPATH,
                                                                 '/html/body/div/div'
                                                                 '/div[2]/div['
                                                                 '2]/div/div/div/div['
                                                                 '1]/div/div/div[ '
                                                                 '2]/div/div/div/div'
                                                                 '/div[ '
                                                                 '2]/div/div/div/div'
                                                                 '/span['
                                                                 '7]/div/div/div/div'
                                                                 '/div[3]/div/label[ '
                                                                 '1]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_estado_civil)

                # DISPENSA MILITAR
                botao_dispensa_militar = self.navegador.find_element(By.XPATH,
                                                                     '/html/body/div'
                                                                     '/div/div['
                                                                     '2]/div['
                                                                     '2]/div/div/div'
                                                                     '/div[ '
                                                                     '1]/div/div/div['
                                                                     '2]/div/div/div'
                                                                     '/div/div[ '
                                                                     '2]/div/div/div'
                                                                     '/div/span['
                                                                     '8]/div/div/div'
                                                                     '/div/div['
                                                                     '3]/div/label[ '
                                                                     '2]/span')
                self.navegador.execute_script("arguments[0].click();",
                                              botao_dispensa_militar)

                # PARENTE BRADESCO #Estágio
                if tipo_de_vaga.__contains__('ESTÁGIO'):
                    botao_parente_bradesco_estagio = self.navegador.find_element(
                        By.XPATH,
                        '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                        '1]/div/div/div[2]/div/div/div/div/div['
                        '2]/div/div/div/div/span[8]/div/div/div/div/div['
                        '3]/div/label[2]/span')
                    self.navegador.execute_script("arguments[0].click();",
                                                  botao_parente_bradesco_estagio)

                # PARENTE BRADESCO #Aprendiz
                if tipo_de_vaga.__contains__('APRENDIZ'):
                    botao_parente_bradesco_aprendiz = self.navegador.find_element(
                        By.XPATH,
                        '/html/body/div/div/div[2]/div[2]/div/div/div/div['
                        '1]/div/div/div[2]/div/div/div/div/div['
                        '2]/div/div/div/div/span[9]/div/div/div/div/div['
                        '3]/div/label[2]/span')
                    self.navegador.execute_script("arguments[0].click();",
                                                  botao_parente_bradesco_aprendiz)

                # PRÓXIMA PÁGINA
                self.navegador.find_element(By.CSS_SELECTOR,
                                            'button[type="button"][dat'
                                            'a-tag="btnNext"]').click()
                WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div/div['
                     '2]/div[2]/div/div/div/div[ '
                     '1]/div/div/div['
                     '2]/div/div/div/div/div[ '
                     '2]/div/div/div/div/span['
                     '1]/div/div/div/div/div[ '
                     '3]/div/label[1]/span')))

            # ----------------------- #
            # --- QUINTA PÁGINA --- #
            # ----------------------- #

            WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[2]/div['
                 '2]/div/div/div/div[ '
                 '1]/div/div/div['
                 '2]/div/div/div/div/div[ '
                 '2]/div/div/div/div/span['
                 '1]/div/div/div/div/div[ '
                 '3]/div/label[1]/span')))
            # Está participando de algum outro Processo Seletivo na Organização
            # Bradesco?
            botao_processo_seletivo = self.navegador.find_element(By.XPATH,
                                                                  '/html/body/div/div'
                                                                  '/div[2]/div['
                                                                  '2]/div/div/div/div[ '
                                                                  '1]/div/div/div['
                                                                  '2]/div/div/div/div'
                                                                  '/div[ '
                                                                  '2]/div/div/div/div'
                                                                  '/span['
                                                                  '1]/div/div/div/div'
                                                                  '/div[ '
                                                                  '3]/div/la'
                                                                  'bel[1]/span')
            self.navegador.execute_script("arguments[0].click();",
                                          botao_processo_seletivo)

            # Como soube das oportunidades de construir sua carreira na
            # Organização Bradesco?
            botao_soube_carreira = self.navegador.find_element(By.XPATH,
                                                               '/html/body/div/div'
                                                               '/div[2]/div['
                                                               '2]/div/div/div/div[ '
                                                               '1]/div/div/div['
                                                               '2]/div/div/div/div'
                                                               '/div[ '
                                                               '2]/div/div/div/div'
                                                               '/span['
                                                               '2]/div/div/div/div'
                                                               '/div[3]/div/label[ '
                                                               '1]/span')
            self.navegador.execute_script(
                "arguments[0].click();", botao_soube_carreira)

            # Como foi a sua experiência ao utilizar o site e realizar o
            # processo de candidatura?
            botao_feedback = self.navegador.find_element(By.XPATH,
                                                         '/html/body/div/div/div['
                                                         '2]/div[2]/div/div/div/div['
                                                         '1]/div/div/div[ '
                                                         '2]/div/div/div/div/div[ '
                                                         '4]/div/div/div/div/span['
                                                         '1]/div/div/div/div/div['
                                                         '3]/div/label[5]/span')
            self.navegador.execute_script(
                "arguments[0].click();", botao_feedback)

            # BOTÃO ENVIAR! self.navegador.find_element(By.CSS_SELECTOR, 'button[
            # type="button"][data-tag="btnSubmit"]').click() time.sleep(5)

            print(
                f'O preenchimento da vaga {i + 1} foi concluído com sucesso!')

        print(
            'O processo de preenchimento de formulários, '
            'foi concluído com sucesso!')

    def obter_vagas(self):
        filtro = input(
            'Digite o(s) tipo(s) de vaga(s) desejada(s). \n*Preencha sem as aspas e com a seguinte separação: "APRENDIZ|ESTAGIÁRIO|ESCRITURÁRIO": >>>')

        # Entrando no site
        print('Entrando no site...')
        self.navegador.get(
            "https://bradesco.csod.com/ux/ats/careersite/1/home?c=bradesco&lang"
            "=pt-BR")
        WebDriverWait(self.navegador, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[1]/div['
             '2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[ '
             '2]/div/span/div/div/nav/button[2]')))

        # Botão cookie
        try:
            self.navegador.find_element(By.CLASS_NAME, 'c-btn').click()
            time.sleep(0.5)
        except Exception:
            pass
        ##########################################################################
        # Obtendo o último botão de passar a página
        pagina_inicial = self.navegador.page_source
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
            pagina_atual = self.navegador.page_source
            site_geral = BeautifulSoup(pagina_atual, 'html.parser')
            vagas_geral = site_geral.find(
                'div', attrs={'class': 'p-view-jobsearchresults'})
            print(
                f'Coletando e armazenando as vagas da página {numero_pagina}...')
            for vaga in vagas_geral:
                vaga_info = vaga.find(
                    'a', attrs={'data-tag': 'displayJobTitle'})
                vaga_url = vaga.find(
                    'a', attrs={'data-tag': 'displayJobTitle'})
                vaga_local = vaga.find(
                    'p', attrs={'data-tag': 'displayJobLocation'})
                vaga_info = vaga_info.text if vaga_info else 'vazio'
                if vaga_url:
                    vaga_url = 'https://bradesco.csod.com' + vaga_url['href']
                else:
                    vaga_url = 'vazio'

                vaga_local = vaga_local.text if vaga_local else 'vazio'
                dados_vagas.append([vaga_info, vaga_local, vaga_url])

            print('Passando para a proxima página...')
            self.navegador.find_element(By.CSS_SELECTOR, ".next").click()
            numero_pagina += 1
            if numero_pagina == ultimo_botao + 1:
                print('Encontrada a última página!')
            time.sleep(3)
        ##########################################################################
        # Transformando os dados da lista em um dataframe e filtrando o local
        df = pd.DataFrame(dados_vagas, columns=['Título', 'Local', 'URL'])
        dados = df[df['Local'].str.contains('BRASIL', case=False)]
        dados = dados[df['Título'].str.contains(filtro,
                                                case=False)]
        dados = dados[~df['Título'].str.contains('PCD', case=False)]

        print('Criando arquivo excel...')
        # Convertendo para um arquivo excel
        dados.to_excel('VagasBradesco.xlsx', index=False)
        print('Concluído!')


if __name__ == '__main__':
    VB = VagasBradesco()
    VB.obter_vagas()
    VB.enviar_curriculo()
