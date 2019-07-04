import datetime
import os
import platform
import sys
import tarfile
import zipfile
from sys import exit
from urllib.parse import urlparse

import firebase_admin
import requests
import tqdm
from bs4 import BeautifulSoup
from firebase_admin import credentials, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def geckodriverCheck():
    if not (os.path.isfile('geckodriver') or os.path.isfile('geckodriver.exe')) :
        print('Unable to locate geckodriver in ' + os.getcwd() + '\n')
        os_name = platform.system()
        bit = '64' if sys.maxsize > 2 ** 32 else '32'
        if os_name == 'Linux':
            host_os = 'linux' + bit
        elif os_name == 'Windows':
            host_os = 'win' + bit
        elif os_name == 'Darwin':
            host_os = 'macos'
        
        release_url = "https://github.com/mozilla/geckodriver/releases/latest/"
        release_response = requests.get(release_url)
        soup = BeautifulSoup(release_response.text, features='html.parser')
        for a in soup.find_all('a', href = True):
            if r'/download' and host_os in a['href']:
                download_url = 'https://www.github.com' + a['href']
        
        filename = os.path.split(urlparse(download_url).path)[1]
        download_url_response = requests.get(download_url, stream = True)
        with open(filename, 'wb') as f:
            chunk_size = 1024
            expeced_size = int(download_url_response.headers['Content-Length'])
            for chunk in tqdm.tqdm(download_url_response.iter_content(chunk_size), desc= filename, total=expeced_size/chunk_size, unit='kb'):
                f.write(chunk)

        if filename.lower().endswith('.tar.gz'):
            with tarfile.open(filename, mode = 'r') as tar:
                tar.extractall()
        elif filename.lower().endswith('.zip'):
            with zipfile.ZipFile(filename, mode = 'r') as zip:
                zip.extractall()

def csv(DT, Status):
    with open('WhatsAppening.csv', 'a') as f:
        f.write(f'{DT.strftime("%x")},{DT.strftime("%X")},{Status}')
    
def firebaseAuth():
    url = input('Enter the Realtime Database URL [https://your-project.firebaseio.com]:')
    try:
        cred = credentials.Certificate('FirebaseAdminSDK.json')
    except FileNotFoundError:
        print('Unable to find FirebaseAdminSDK.json file in ' + os.getcwd)
        exit(1)
    firebase_admin.initialize_app(cred, {
        'databaseURL': url
    })

def firebaseWrite(DT, value):
    dateFormat = DT.strftime("%x")
    timeFormat = DT.strftime("%X")
    ref = db.reference('/Logs')
    ref.push({
        'Date': dateFormat,
        'Time': timeFormat,
        'Status': value
    })

def main():
    print('Starting WhatsAppening v1.3.0, It can take a few seconds.\n')
    geckodriverCheck()
    firebaseAuth()
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get('https://web.whatsapp.com')
    input('\nScan the QR code from Whatsapp Web & Open the contact which you want to track. \n\nPress Enter to continue...')
    try:
        while True:
            WebDriverWait(driver, 86400).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[@title="online"]')
                )
            )
            DT = datetime.datetime.now()
            print('\nOnline  : ' + DT.strftime('%X'))
            csv(DT, 'Online\n')
            firebaseWrite(DT, 'Online')
            WebDriverWait(driver, 86400).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, '//span[@title="online"]')
                )
            )
            DT = datetime.datetime.now()
            print('Offline : ' + DT.strftime('%X'))
            csv(DT, 'Offline\n')
            firebaseWrite(DT, 'Offline')
    except ValueError as VE:
        print(VE)
        exit(1)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt Received, Exiting WhatsAppening')
        exit(0)


if __name__ == "__main__":
    main()
