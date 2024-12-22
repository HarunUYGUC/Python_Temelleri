from selenium import webdriver
import time

# chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver" => Mac için.
# chrome_driver_path = r"C:\Users\Harun\Downloads\chromedriver-win64" => Windows için ama gerek yok, çalışmıyor.

# driver = webdriver.Chrome(executable_path=chrome_driver_path) => Mac için.

driver = webdriver.Chrome()

driver.get("https://github.com/HarunUYGUC")
driver.maximize_window() # Ekranı tam ekran yapar.
driver.save_screenshot(r"C:\Users\Harun\Desktop\Python_Temelleri\Selenium ile Bot Yazımı\GitHub-HarunUYGUC.png")
time.sleep(2) # 2 saniye bekle.

# Scroll down the page by 1000 pixels
driver.execute_script("window.scrollBy(0, 100);") # Sayfayı 100 piksel aşağı kaydırır
driver.save_screenshot(r"C:\Users\Harun\Desktop\Python_Temelleri\Selenium ile Bot Yazımı\GitHub-HarunUYGUC_2.png")
time.sleep(2) # 2 saniye bekle.

driver.close()
