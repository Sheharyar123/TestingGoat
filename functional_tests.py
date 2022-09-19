from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/Phantom Lover/Downloads/Dev/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='http://localhost:8000'
browser.get(url)