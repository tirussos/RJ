from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera
import os
import time

# https://notacarioca.rio.gov.br/errortimeout.htm

""" Configurações básicas para o funcionamento adequado do código, 
                somente alterar com algum auxílio!                """

download_path = os.path.join(os.getcwd(), "downloads")



if not os.path.isdir(download_path):
    try:
        os.mkdir(download_path)
        print("Pasta criada com sucesso!!!")
    except OSError as e:
        print(f"Erro - {e} ao criar o diretório - {download_path}")
else:
    print("Pasta encontrada!!")


chrome_options_list = [
    "--disable-notifications",
    "--disable-infobars"
]

chrome_options = Options()


for option in chrome_options_list:
    chrome_options.add_argument(option)

prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)

chrome_driver_path = ChromeDriverManager().install()
chrome_driver_executable = os.path.join(os.path.dirname(chrome_driver_path), 'chromedriver.exe')
web = webdriver.Chrome(service=Service(chrome_driver_executable), options=chrome_options)

web.get("https://notacarioca.rio.gov.br/senhaweb/login.aspx")

input("Pressione Enter para finalizar o navegador")
web.quit()

# Login CPF (xpath)
# //*[@id="ctl00_cphCabMenu_tbCpfCnpj"] 

# Senha
# //*[@id="ctl00_cphCabMenu_tbSenha"]

def login_function():
    diretorio_atual = os.getcwd()
    caminho_login = os.path.join(diretorio_atual, "credenciais", "login.txt")
    caminho_senha = os.path.join(diretorio_atual, "credenciais", "pass.txt")
    
    try:
        with open(caminho_login, 'r') as file:
            login = file.read().strip()
    except:
        print("Login não existe")
    try:

        with open(caminho_senha, 'r') as file:
            senha = file.read().strip()
    except:
        print("Senha não existe")

    return login, senha

login, senha = login_function()

def click_xpath(xpath):
    web.find_element(By.XPATH, xpath).click()
    return

def typing_id(id, value):
    web.find_element(By.ID, id).send_keys(value)
    return


# DeclaraçãO de NF'S recebida - menuDivAux

# button XPATH //*[@id="ctl00_cphCabMenu_btCadastrar"] | Clicar

# Tomador de Serviços | Xpath - //*[@id="ctl00_cphCabMenu_ctrlInscricoes_ddlInscricoes"]/option[2] 

# CNPJ Prestador de serviços | ID - ctl00_cphCabMenu_tbCPFCNPJPrestador   {Digitar lentamente} | I

# N da nota fiscal | ID - ctl00_cphCabMenu_tbNFNumero | G

# Serie da Nota fiscal | ID - ctl00$cphCabMenu$tbNFSerie | Resposta padrão: E

# Data de emissão | ID - ctl00$cphCabMenu$tbNFEmissao | A

# Código de serviço | XPATH - //*[@id="ctl00_cphCabMenu_ctrlServicos_ddlGrupos"]/option[X] | H

# Sub Código de serviço | XPATH - //*[@id="ctl00_cphCabMenu_ctrlServicos_ddlSubGrupos"]/option[5] | H

# Serviço | Xpath - ///*[@id="ctl00_cphCabMenu_ctrlServicos_ddlServicos"]/option[X] | H

# Total da nota | Xpath - //*[@id="ctl00_cphCabMenu_tbValor"] | N

# Total deduçoes | Xpath - //*[@id="ctl00_cphCabMenu_tbDeducao"] | M

# Aliquota | Xpath - //*[@id="ctl00_cphCabMenu_ctrlServicos_tbAliquota"] | L
 
# ISS Retido Input | Xpath - //*[@id="ctl00_cphCabMenu_rblISSRetido_0"] ou 1 | 

# Simples nacional | Xpath - //*[@id="ctl00_cphCabMenu_rblSimplesNacional_0"] ou 1 |

# Data de prestação | Xpath - //*[@id="ctl00_cphCabMenu_tbDataReferencia"] | Mesma data da coluna "A"

# Declarar >> | Xpath - //*[@id="ctl00_cphCabMenu_btEmitir"] | Cliclar

# Inscrição Municipal | //*[@id="ctl00_cphCabMenu_ctrlInscricoes_ddlInscricoes"]/option[2]

# Guia de recolhimento | Xpath - //*[@id="ctl00_Vcab_mnuRotinasn8"]/td/table/tbody/tr/td/a | Clicar

# Contribuente | Value - value="1011928" | Alterar value de acordo com os números da coluna  "E"


# Linha do Emitir Guia | Xpath - //*[@id="ctl00_cphCabMenu_dgGuias"]/tbody/tr[2] 

# Data de Emissão | ELEMENTO - <td align="center">05/08/2024</td> | Se o texto for igual a data de hoje, clicar no próximo elemento

# Emitir Guia | Xpath - //*[@id="ctl00_cphCabMenu_dgGuias"]/tbody/tr[2]/td[5]/a | Clicar

# Emitir a Guia | Xpath - //*[@id="ctl00_cphCabMenu_btGerarGuia"] | Clicar

# Gerar PDF | Xpath - //*[@id="ctl00_cphBase_btExportar"] | Clicar