import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import time

browsers = ["chrome", "edge"] 

class BookCartTest(unittest.TestCase):
    
    def test_success_logintocheckout(self):
        for browser in browsers:
            try:
                if browser == "chrome":
                    options = ChromeOptions()
                    options.add_argument("--headless") 
                    options.add_argument("--disable-gpu")
                    options.add_argument("--window-size=1920,1080")
                    driver = webdriver.Chrome( options=options)
                elif browser == "edge":
                    options = EdgeOptions()
                    options.add_argument("--headless") 
                    driver = webdriver.Edge(options=options)
                
                driver.maximize_window()
                driver.get("https://bookcart.azurewebsites.net")
                
                self.subTest(browser=browser)
                time.sleep(5)
                driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys("Sabr")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("S@brin4i")
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Login'])[2]").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[@class='mdc-list-item__content'])[2]").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[@class='mdc-list-item__content'])[3]").click()
                time.sleep(5)
                slider = driver.find_element(By.XPATH, "//input[@type='range']")
                driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));", slider, "4k")
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Add to Cart'])[1]").click()
                time.sleep(5)
                cart_icon = driver.find_element(By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[3]")
                ActionChains(driver).move_to_element(cart_icon).click().perform()
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[normalize-space()='CheckOut'])[1]").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='name']").send_keys("Sabrina")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='addressLine1']").send_keys("Lorem Ipsum Dolor")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='addressLine2']").send_keys("Sabr")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='pincode']").send_keys("123456")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='state']").send_keys("Konoha")
                time.sleep(5)
                driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[normalize-space()='Place Order'])[1]").click()
                time.sleep(5)
            finally:
                driver.quit()

    def test_failed_login(self):
        for browser in browsers:
            try:
                if browser == "chrome":
                    options = ChromeOptions()
                    options.add_argument("--headless=new")
                    options.add_argument("--disable-gpu")
                    options.add_argument("--window-size=1920,1080")
                    driver = webdriver.Chrome(options=options)
                elif browser == "edge":
                    options = EdgeOptions()
                    options.add_argument("--headless")
                    driver = webdriver.Edge( options=options)
                
                driver.maximize_window()
                driver.get("https://bookcart.azurewebsites.net")
                
                self.subTest(browser=browser)
                time.sleep(5)
                driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys("Vina")
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("S4brin4i")
                time.sleep(5)
                driver.find_element(By.XPATH, "(//span[@class='mdc-button__label'][normalize-space()='Login'])[2]").click()
                time.sleep(5)
            finally:
                driver.quit()
    
    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
