#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
web='https://www.magicbricks.com/'
driver.get(web)
city_button = driver.find_element(By.XPATH,'.//a[@class="mb-header__main__link js-menu-link"]')
city_button.click()
links=[]
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True
cities = WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH,'.//ul[@class="city-drop-link-group"]/li/a')))
for i in cities:
    links.append(i.get_attribute("href"))
for i in range(5,len(links)):
    driver.get(links[i])
    rent_button=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH,'.//div[@id="tabRENT"]')))
    rent_button[0].click()
    search_button=driver.find_element(By.XPATH,'.//div[@class="mb-search__btn"]')
    search_button.click()
    """close_flat=WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH,'.//div[@class="filter__component topPropertyType"]/span')))
    close_flat[0].click()
    select_all=driver.find_element(By.XPATH,'.//div[text()="Property Type"]')
    select_all.click()
    flat_select=driver.find_element(By.XPATH,'.//label[@for="propResidential_propertyType_10002_10003_10021_10022_10020"]')
    flat_select.click()
    house_select=driver.find_element(By.XPATH,'.//label[@for="propResidential_propertyType_10001_10017"]')
    house_select.click()
    done=driver.find_element(By.XPATH,'.//div[@class="filter__component__cta-done"]')
    done.click()"""
    driver.implicitly_wait(4)
    table_no=driver.find_element(By.XPATH,'.//div[@class="mb-srp__title--text1"]')
    table=driver.find_elements(By.XPATH,'.//div[@class="mb-srp__card"]')
    t_no=0
    for i in table_no.text:
        if i in "0123456789":
            t_no=t_no*10+int(i)
    table_values=[]
    runner=0
    while t_no!=runner:
            if check_exists_by_xpath('.//a[@class="close_chat_box"]'):
                close_chat_bot=driver.find_element(By.XPATH,'.//a[@class="close_chat_box"]')
                close_chat_bot.click()
                yes_chat_bot=driver.find_element(By.XPATH,'.//button[@class="sb_yes_btn"]')
                yes_chat_bot.click()
            table=driver.find_elements(By.XPATH,'.//div[@class="mb-srp__card"]')
            driver.implicitly_wait(0.3)
            name_location=[]
            name=table[runner].find_element(By.XPATH,'.//h2[@class="mb-srp__card--title"]')
            name_location.append(name.text)
            if check_exists_by_xpath('.//div[@class="mb-srp__card__summary__action"]'):
                table_button = table[runner].find_element(By.XPATH, './/div[@class="mb-srp__card__summary__action"]')
                table_button.click()
            table_contents_name=[]
            table_contents_value=[]
            b=table[runner].find_elements(By.XPATH,'.//div[contains(@class,"mb-srp__card__summary--value")]')
            c=table[runner].find_elements(By.XPATH,'.//div[contains(@class,"mb-srp__card__summary--label")]')
            cash=table[runner].find_element(By.XPATH,'.//div[@class="mb-srp__card__price--amount"]')
            temp=""
            for i in cash.text:
                if i not in "₹\n":
                    temp+=i
            name_location.append(temp)
            for k in b:
                table_contents_value.append(k.get_attribute("textContent"))
            for k in c:
                table_contents_name.append(k.get_attribute("textContent"))
            df=pd.DataFrame(table_contents_name)
            print(name_location)
            print(table_contents_name)
            print(table_contents_value)
            runner+=1
