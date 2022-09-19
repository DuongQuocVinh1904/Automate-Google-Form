
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("--headless")
#option.add_argument("disable-gpu")
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=option)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeP0RWgZk51ycFKpcFeiB041kykbwLQKcc6_LBoRcrtedgo9g/viewform")
time.sleep(3)

name = driver.find_element_by_xpath("//*[@id='i20']/div[3]/div")
name.click() #choose the name Quốc Vinh

age = driver.find_element_by_xpath("//*[@id='i30']/div[3]/div")
age.click()

gender = driver.find_element_by_xpath('//*[@id="i46"]/div[3]/div')
gender.click()

education = driver.find_element_by_xpath('//*[@id="i59"]/div[3]/div')
education.click()

income = driver.find_element_by_xpath('//*[@id="i75"]/div[3]/div')
income.click()

job = driver.find_element_by_xpath('//*[@id="i85"]/div[3]/div')
job.click()

family = driver.find_element_by_xpath('//*[@id="i95"]/div[3]/div')
family.click()

location = driver.find_element_by_xpath('//*[@id="i108"]/div[3]/div')
location.click()

status = driver.find_element_by_xpath('//*[@id="i118"]/div[3]/div')
status.click()

health = driver.find_element_by_xpath('//*[@id="i141"]/div[2]')
health.click()

env = driver.find_element_by_xpath('//*[@id="i164"]/div[2]')
env.click()

beer = driver.find_element_by_xpath('//*[@id="i177"]/div[3]/div')
beer.click()

beer_spending = driver.find_element_by_xpath('//*[@id="i190"]/div[3]/div')
beer_spending.click()

ecom_platform = driver.find_element_by_xpath('//*[@id="i207"]/div[2]')
ecom_platform.click()

shopping = driver.find_element_by_xpath('//*[@id="i233"]/div[2]')
shopping.click()

news = driver.find_element_by_xpath('//*[@id="i247"]/div[2]')
news.click()

ads = driver.find_element_by_xpath('//*[@id="i270"]/div[2]')
ads.click()

entertainment = driver.find_element_by_xpath('//*[@id="i290"]/div[2]')
entertainment.click()

choose_product = driver.find_element_by_xpath('//*[@id="i313"]/div[2]')
choose_product.click()

choose_product2 = driver.find_element_by_xpath('//*[@id="i310"]/div[2]')
choose_product2.click()

material_package = driver.find_element_by_xpath('//*[@id="i324"]/div[2]')
material_package.click()

social_media_fb = driver.find_element_by_xpath('//*[@id="i344"]/div[2]')
social_media_fb.click()

social_media_ig = driver.find_element_by_xpath('//*[@id="i347"]/div[2]')
social_media_ig.click()

social_spending = driver.find_element_by_xpath('//*[@id="i366"]/div[3]/div')
social_spending.click()

tivi_content = driver.find_element_by_xpath('//*[@id="i386"]/div[2]')
tivi_content.click()

tivi_spending = driver.find_element_by_xpath('//*[@id="i402"]/div[3]/div')
tivi_spending.click()

social_act = driver.find_element_by_xpath('//*[@id="i419"]/div[2]')
social_act.click()

social_act2 = driver.find_element_by_xpath('//*[@id="i416"]/div[2]')
social_act2.click()

drink = driver.find_element_by_xpath('//*[@id="i433"]/div[2]')
drink.click()

submit = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
submit.click()


