from selenium import webdriver
from selenium.webdriver.common.by import By


def dynamicUrlHard(url,length)->str:
    array = list()
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options = options)


    for i in range(length):
        driver.get(url)
        div = driver.find_element(By.CLASS_NAME,'page1')
        a = div.find_elements(By.TAG_NAME,'a')
        a[-1].click()
        array.append(driver.current_url)
        url = driver.current_url
    driver.close()
    return array

