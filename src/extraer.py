import pandas as pd
from datetime import datetime
import asyncio
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from tqdm.notebook import tqdm
# opciones del driver
opciones=Options()

# quita la bandera de ser robot
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado

# guardar las cookies
#opciones.add_argument('user-data-dir=selenium')    # mantiene las coockies

import warnings
warnings.filterwarnings('ignore')

Season_list = []
db_concat = pd.DataFrame()
def scraping_matches():
    global db_concat
    global Season_list
    print("Downloading data for Season 2022")
    Season_2022 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/2223/SP1.csv")
    print("Downloading data for Season 2021")
    Season_2021 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/2122/SP1.csv")
    print("Downloading data for Season 2020")
    Season_2020 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/2021/SP1.csv")
    print("Downloading data for Season 2019")
    Season_2019 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1920/SP1.csv")
    print("Downloading data for Season 2018")
    Season_2018 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1819/SP1.csv")
    print("Downloading data for Season 2017")
    Season_2017 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1718/SP1.csv")
    print("Downloading data for Season 2016")
    Season_2016 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1617/SP1.csv")
    print("Downloading data for Season 2015")
    Season_2015 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1516/SP1.csv")
    print("Downloading data for Season 2014")
    Season_2014 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1415/SP1.csv")
    print("Downloading data for Season 2013")
    Season_2013 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1314/SP1.csv")
    print("Downloading data for Season 2012")
    Season_2012 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1213/SP1.csv")
    print("Downloading data for Season 2011")
    Season_2011 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1112/SP1.csv")
    print("Downloading data for Season 2010")
    Season_2010 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1011/SP1.csv")
    print("Downloading data for Season 2009")
    Season_2009 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/0910/SP1.csv")
    print("Downloading data for Season 2008")
    Season_2008 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/0809/SP1.csv")
    print("Downloading data for Season 2007")
    Season_2007 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/0708/SP1.csv")
    print("Downloading data for Season 2006")
    Season_2006 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/0607/SP1.csv")
    print("Downloading data for Season 2005")
    Season_2005 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/0506/SP1.csv")
    print("Defining list of all seasons")
    Season_list = [Season_2022, 
                   Season_2021,
                   Season_2020,
                   Season_2019,
                   Season_2018,
                   Season_2017,
                   Season_2016,
                   Season_2015,
                   Season_2014,
                   Season_2013,
                   Season_2012,
                   Season_2011,
                   Season_2010,
                   Season_2009,
                   Season_2008,
                   Season_2007,
                   Season_2006,
                   Season_2005
           ]
    print("Concatenating all data into one dataframe")
    db_concat = pd.concat(Season_list)
    print("Saving csv")
    db_concat.to_csv(r'../data/matches.csv')
    print("File Saved")
    

DATOS=[]

CABECERAS=[]

def scraping_cabe():
    PATH=ChromeDriverManager().install()
    driver = webdriver.Chrome(PATH,options = opciones)
    driver.get('https://fbref.com/en/comps/12/stats/La-Liga-Stats')
    time.sleep(2)
    acepto=driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')

    acepto.click()

    time.sleep(2) 

    tabla=driver.find_elements(By.TAG_NAME,'table')[9]

    filas=tabla.find_elements(By.TAG_NAME, 'tr')
    cab = [c.text for c in filas[1].find_elements(By.TAG_NAME, 'th')]
    return cab

def scraping_teams(url):
    
    global DATOS, CABECERAS
    
    PATH=ChromeDriverManager().install()
    driver = webdriver.Chrome(PATH,options = opciones)
    driver.get(url)
    time.sleep(2)

    acepto=driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')

    acepto.click()

    time.sleep(2) 

    tabla=driver.find_elements(By.TAG_NAME,'table')[9]

    filas=tabla.find_elements(By.TAG_NAME, 'tr')

    data=[]

    for f in filas[2:]:

        equipo = f.find_element(By.TAG_NAME, 'th')

        elementos=f.find_elements(By.TAG_NAME, 'td') 

        tmp=[]
        elementos.insert(0, equipo)
        for e in elementos:

            tmp.append(e.text)

        data.append(tmp)

    #cab = [c.text for c in filas[1].find_elements(By.TAG_NAME, 'th')]
    driver.quit()
    return data
    #CABECERAS=cab
    
def scraping_cols():
    PATH=ChromeDriverManager().install()
    driver = webdriver.Chrome(PATH,options = opciones)
    driver.get('https://fbref.com/en/comps/12/stats/La-Liga-Stats')
    time.sleep(2)
    acepto=driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')

    acepto.click()

    time.sleep(2) 

    tabla=driver.find_elements(By.TAG_NAME,'table')[11]

    filas=tabla.find_elements(By.TAG_NAME, 'tr')
    cab = [c.text for c in filas[1].find_elements(By.TAG_NAME, 'th')]
    return cab
    
def scraping_players(url):
    
    PATH=ChromeDriverManager().install()
    driver = webdriver.Chrome(PATH,options = opciones)
    driver.get(url)
    time.sleep(2)

    acepto=driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')

    acepto.click()

    time.sleep(2) 

    tabla=driver.find_elements(By.TAG_NAME,'table')[11]
    
    filas=tabla.find_elements(By.TAG_NAME, 'tr')

    data=[]

    for f in filas[2:]:

        ids = f.find_element(By.TAG_NAME, 'th')

        elementos=f.find_elements(By.TAG_NAME, 'td') 

        tmp=[]
        elementos.insert(0, ids)
        for e in elementos:

            tmp.append(e.text)

        data.append(tmp)
    driver.quit()
    return data