import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def csv(DT, Status):
    with open('WhatsAppening.csv', 'a') as f:
        f.write(f'{DT.strftime("%x")},{DT.strftime("%X")},{Status}')

def main():
    print('Starting WhatsAppening v1.1.0, It can take a few seconds.')
    driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com')
    input('\nScan the QR code from Whatsapp Web & Open the contact which you want to track. \n\nPress Enter to continue...')
    while True:
        WebDriverWait(driver, 43200).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//span[@title="online"]')
            )
        )
        DT = datetime.datetime.now()
        print('\nOnline  : ' + DT.strftime('%X'))
        csv(DT, 'Online\n')
        WebDriverWait(driver, 43200).until(
            EC.invisibility_of_element_located(
                (By.XPATH, '//span[@title="online"]')
            )
        )
        DT = datetime.datetime.now()
        print('Offline : ' + DT.strftime('%X'))
        csv(DT, 'Offline\n')


if __name__ == "__main__":
    main()
