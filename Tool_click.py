from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chromedriver_path = 'C:\\Users\\ASUS\\Downloads\\chromedriver_win32\\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument("webdriver.chrome.driver=" + chromedriver_path)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://dangcapthucung.joygame.vn/activity/20200929/index.html')

button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'header__btns-wraper__login-btn'))
)
button.click()
sleep(1)

user = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'username'))
)
user.send_keys('hduc1')
sleep(1)

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'userpass'))
)
password.send_keys('zzzzzz')
sleep(1)

button_login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'login_btn1'))
)
button_login.click()
sleep(1)

server = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'userzone'))
)
server.send_keys('1364')
sleep(2)

button_server = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'server_btn'))
)
button_server.click()
sleep(3)

button_reserve = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'header__btns-wraper__reward-btn'))
)
button_reserve.click()
sleep(5)

button_close = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ClASS_NAME, 'close'))
)
button_close.click()
sleep(2)

button_esc = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'header__user-info__drop-btn'))
)
button_esc.click()
sleep(2)


driver.quit()
