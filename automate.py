from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
def connection(user,psw):
    driver.get("https://facebook.com")
    login = driver.find_element(By.ID,"email")
    login.send_keys(user)
    password = driver.find_element(By.ID,"pass")
    
    password.send_keys(psw)
    password.send_keys(Keys.RETURN)
    time.sleep(10)
    

def search(search_term):
    driver.get(f"https://web.facebook.com/search/pages/?q={search_term}")
    time.sleep(5)
    
def click_page(number):
    page = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[{number}]/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a")
    page.click()
    time.sleep(5)
def post(comment):
    find_comment = driver.find_element(By.XPATH,'//*[@aria-label="Comment as Mohammed Hajoubi"]')
    driver.execute_script('window.scrollBy(0, 40)')
    time.sleep(5)
    find_comment.send_keys(comment)
    find_comment.send_keys(Keys.RETURN)
    time.sleep(5)
connection("","")

i=1
searching_terms = ["fun movies","popular series","streaming tv","best channels"]
for terms in searching_terms:
    i= 1
    while i < 4:
        search(terms)
        click_page(i)
        try:
            post("www.hapyiptv.com")
        except:
            i= i+1
            continue
        i= i + 1