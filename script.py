from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome()
driver.get("https://monkeytype.com/")

print("Você tem 10 segundos para aceitar os cookies e configurar o teste...")
time.sleep(10)

print("Começando a digitar!")

try:
    
    input_escondido = driver.find_element(By.ID, "wordsInput")
    
    while True:
        
        palavra_ativa = driver.find_element(By.CSS_SELECTOR, ".word.active")
        
        
        letras = palavra_ativa.find_elements(By.TAG_NAME, "letter")
        texto_para_digitar = "".join([letra.get_attribute("textContent") for letra in letras])
        
        
        for letra in texto_para_digitar:
            input_escondido.send_keys(letra)
            time.sleep(random.uniform(0.01, 0.05)) 
        
        
        input_escondido.send_keys(Keys.SPACE)
        
        
        time.sleep(random.uniform(0.02, 0.08))

except Exception as e:
    
    print(f"\n⚠️ O robô parou! Motivo: {e}")
    

time.sleep(10)
driver.quit()