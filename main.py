from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

web = "https://deportesweb.madrid.es/DeportesWeb/Login"

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Anton\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get(web)

# sede_electronica = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//article[@class='navigation-section-widget-collection-item']/h4[@title='Sede electrónica']")))
# sede_electronica.click()

gym = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//article[@class='navigation-section-widget-collection-item']/h4[@title='Sala multitrabajo']")))

driver.execute_script("arguments[0].scrollIntoView();", gym)
gym.click()

search_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ContentFixedSection_uAltaEventos_uCentrosSeleccionar_txtBuscar")))
search_bar.send_keys("Pradillo")
search_bar.send_keys(Keys.RETURN)

center = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'Pradillo')]")))
center.click()


day_to_select = "04/02/2025"
#calendar_day = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//td[@data-day='04/02/2025']")))

days = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//td[@data-action='selectDay']"))
)

for day in days:
    print(day.get_attribute("data-day"))  # Debug all available days
    if day.get_attribute("data-day") == "04/02/2025":
        driver.execute_script("arguments[0].scrollIntoView(true);", day)
        style = driver.execute_script("return window.getComputedStyle(arguments[0]);", day)

        break


 
# hour = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), '21:00')]")))
# hour.click()

# reservation_details = driver.find_elements(By.XPATH, "//span")
# reservation_details = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[h4[contains(text(), '21:00')]]/span")))
# for span in reservation_details:
#     print(span.text)





sleep(3)
driver.quit()