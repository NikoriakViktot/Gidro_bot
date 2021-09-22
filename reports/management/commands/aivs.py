from django.core.management import BaseCommand
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("я команда")
        service = Service('C://gidroBot//chromedriver.exe')
        service.start()
        driver = webdriver.Remote(service.service_url)
        driver.get('http://hydro.meteo.gov.ua/')
        time.sleep(5)  # Let the user actually see something!
        element = driver.find_element_by_name("station")
        print(element)


        # element.Keys.RETURN
        # element1 = driver.find_elements_by_css_selector(value="storozhynech")
        # element1.Keys.RETURN

        # driver.quit()

