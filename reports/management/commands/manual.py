from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests

with open("C:/Data_manual/20_08/" + "HHZZ.00" ) as f:
    print(f)
    s1 = open(f)
    fil_hh = f.encoding()
    print(fil_hh)

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("я команда")
        with open("C:/Data_manual/20_08/" + "HHZZ.00", "r") as f:
            fil_hh = f.encoding()
            print(fil_hh)

        #
        #
        #
        # zap = requests.get('http://gcst.meteo.gov.ua/armua/index.phtml',user,parol)
        # print(zap)
        # service = Service('C://gidroBot//chromedriver.exe')
        # service.start()
        # driver = webdriver.Remote(service.service_url)
        # driver.get('http://gcst.meteo.gov.ua/armua/index.phtml')
        #
        # element = driver.find_elements_by_css_selector("newuser")
        # element.s("chernovcgm")
        # element.send_keys(Keys.RETURN)
        # time.sleep(5)
        # element_pasw = driver.find_element_by_name("Пароль")
        # element_pasw.sendKeys('(zBLFX$#)b')


        # time.sleep(5)  # Let the user actually see something!
        # driver.quit()


