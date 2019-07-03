import datetime
from sys import exit

import firebase_admin
from firebase_admin import credentials, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def csv(DT, Status):
    with open('WhatsAppening.csv', 'a') as f:
        f.write(f'{DT.strftime("%x")},{DT.strftime("%X")},{Status}')
    
def firebaseAuth():
    url = input('Enter the Realtime Database URL [https://your-project.firebaseio.com]:')
    try:
        cred = credentials.Certificate('FirebaseAdminSDK.json')
    except FileNotFoundError:
        print('Unable to find FirebaseAdminSDK.json file in path.')
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
    print('Starting WhatsAppening v1.2.0, It can take a few seconds.')
    firebaseAuth()
    driver = webdriver.Firefox()
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
