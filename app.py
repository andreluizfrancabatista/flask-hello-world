import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

"""# Configuração do Web-Driver"""

# Utilizando o WebDriver do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-crash-reporter')
options.add_argument('--log-level=3')


# Criação do WebDriver do Chrome
wd_Chrome = webdriver.Chrome('chromedriver',options=options)

"""# Importando as Bibliotecas"""

# import pandas as pd
# from tqdm import tqdm
import time
from selenium.webdriver.common.by import By

"""# Iniciando a Raspagem de Dados"""

# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com/") 
time.sleep(2)

## Para jogos do dia seguinte / Comentar essa linha para os jogos agendados de hoje 
wd_Chrome.find_element(By.CSS_SELECTOR,'button.calendar__navigation--tomorrow').click()
time.sleep(2)

# Pegando o ID dos Jogos
id_jogos = []
## Para jogos agendados (próximos)
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')

## Para jogos ao vivo (live)
# jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--live')

for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'
id_jogos = [i[4:] for i in id_jogos]

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", id_jogos=id_jogos)

if __name__ == "__main__":
    app.run()
