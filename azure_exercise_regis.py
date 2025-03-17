import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time 

browsers = ["chrome", "edge"] 
# sudah oke
class GoogleTestCase(unittest.TestCase):
    def test_success_register(self):
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
                driver.find_element(By.XPATH,"//span[normalize-space()='Login']").click()
                time.sleep(2)
                driver.find_element(By.XPATH,"//span[normalize-space()='Register']").click()
                time.sleep(10)
                driver.find_element(By.XPATH, "//input[@formcontrolname='firstName']").send_keys("Sabrina")
                time.sleep(10)
                driver.find_element(By.XPATH, "//input[@formcontrolname='lastName']").send_keys('Insani')
                time.sleep(10)
                driver.find_element(By.XPATH, "//input[@formcontrolname='userName']").send_keys('Saaabr')
                time.sleep(10)
                driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys('S@brin4i')
                time.sleep(10)
                driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']").send_keys('S@brin4i')
                time.sleep(10)
                gender_button=driver.find_element(By.ID,"mat-radio-1-input")
                driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
                if gender_button.is_selected():
                    pass
                else:
                    gender_button.click()
                time.sleep(5)

                oke=driver.find_element(By.XPATH,"//span[normalize-space()='Register']")
                driver.execute_script("arguments[0].scrollIntoView(true);", oke)
                oke.click()
                time.sleep(10)

            finally:
                driver.quit()

if __name__ == '__main__':
    unittest.main()