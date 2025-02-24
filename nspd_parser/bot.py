import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def nspd_bot(cad_number, driver, act):
    """
    Открывает сайт, выполняет необходимые действия для поиска по кадастровому номеру
    и возвращает текстовое содержимое страницы.
    """
    driver.get("https://nspd.gov.ru/map")

    try:
        button = driver.find_element(By.ID, 'details-button')
        button.click()
        button = driver.find_element(By.ID, 'proceed-link')
        button.click()
    except Exception:
        pass

    time.sleep(3.5)

    driver.find_element(By.XPATH, "//div[@id='map']//m-sidebar").click()

    for _ in range(27):
        act.send_keys(Keys.TAB).perform()

    act.send_keys(cad_number).perform()
    act.send_keys(Keys.ENTER).perform()

    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@id='map']//m-sidebar").click()

    for _ in range(3):
        act.send_keys(Keys.TAB).perform()
    act.send_keys(Keys.ENTER).perform()

    driver.find_element(By.XPATH, "//div[@id='map']//m-sidebar").click()
    time.sleep(1)

    return driver.find_element(By.TAG_NAME, "body").text
