import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import update


class Amo:
    URL = "https://www.mysupertestaccount.amocrm.ru/"
    SETTINGS_URL = "https://mysupertestaccount.amocrm.ru/amo-market/#category-installed"
    # Данные для ввода
    EMAIL = '@gmail.com'
    PASSWORD = "password"
    PATH_TO_WIDGET_ZIP = "C:\\widget\\widget.zip"
    WIDGET_CLASS = "agitq3-7Fh6"

    def __init__(self) -> None:
        self.path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        self.options.add_argument("--ignore-certificate-error")
        self.options.add_argument("--ignore-ssl-errors")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.caps = webdriver.DesiredCapabilities.CHROME.copy()
        self.caps['acceptInsecureCerts'] = True
        self.caps['acceptSslCerts'] = True
        
    def make_driver(self):
        self.driver = webdriver.Chrome(
            executable_path=self.path,
            options=self.options,
            desired_capabilities=self.caps
        )
    
    def autorization (self):
        self.driver.get(url=self.URL)
        time.sleep(3)
        email_input = self.driver.find_element(By.ID, "session_end_login")
        email_input.send_keys(self.EMAIL)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(self.PASSWORD)
        # нажимаем кнопку авторизации
        self.driver.find_element(By.ID, "auth_submit").click()
        time.sleep(2)
            
    def update_widget(self):
        # Нажимаем кноку редактировать
        self.driver.find_element(By.ID, "edit-button").click()
        time.sleep(2)
        load_button = self.driver.find_element(By.ID, "input-upload-archive")
        #здесь введите путь до файла 
        load_button.send_keys(self.PATH_TO_WIDGET_ZIP)
        #Сохраняем
        self.driver.find_element(By.ID, "keygen-button").click()
        time.sleep(5)

    def select_widget(self):
        self.driver.get(self.SETTINGS_URL)
        time.sleep(5)
        self.driver.find_elements(By.CLASS_NAME, self.WIDGET_CLASS)[0].click()

    def close_connection(self):
        self.driver.close()
        self.driver.quit()

def main():
    try:
        connection = Amo()
        connection.make_driver()
        connection.autorization()
        connection.select_widget()
        while True:
            input("Нажмите Enter, когда требуется обновление")
            update.modify_manifest()
            update.remove_widget_zip()
            update.add_files_to_archive()
            connection.update_widget()

    except Exception:
        print(Exception)
    except KeyboardInterrupt:
        print("Спасибо за использование программы :)")

    finally:
        connection.close_connection()

if __name__ == '__main__':
    main()
