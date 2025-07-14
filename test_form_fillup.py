from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

# To print the page title in log
if not log.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)


class TestRegister():
    def test_registration(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Register.html")
        driver.implicitly_wait(10)
        # driver.save_screenshot(r"C:\Users\dilip\PycharmProjects\pythonProject1\pytest_frameword\screenshots\dilip.png")
        log.info("Page title is : {}".format(driver.title))
        time.sleep(3)

    def test_basicinfo(self):
        # Basic Info
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Sameer")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Sharma")
        driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("Puri Gate, B.R. Nagar, PIN-721306, Kharagpur, West Bengal")
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("dilipjolly@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("8637060998")
        print("Personal details have been submitted")

        # Gender and Hobbies

    def test_generalhobbies(self):
        driver.find_element(By.XPATH, "//input[@value='Male']").click()
        driver.find_element(By.ID, "checkbox1").click()
        driver.find_element(By.ID, "checkbox2").click()
        driver.find_element(By.ID, "checkbox3").click()
        log.info("Hobbies selected")

        # Language selection

    def test_language(self):
        driver.find_element(By.ID, "msdd").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/a[text()='Hindi']"))).click()
        driver.find_element(By.XPATH, "//label[text()='Languages']").click()  # Clicked outside to close dropdown
        log.info("Language selected")

        # Skills

    def test_skills(self):
        skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
        skills_dropdown.select_by_visible_text("Python")
        log.info("Skills selected")

        # Country selection

    def test_country(self):
        driver.find_element(By.XPATH, "//span[@role='combobox']").click()
        driver.find_element(By.XPATH, "//li[text()='India']").click()
        log.info("Country selected")

        # DOB selection

    def test_dob(self):
        Select(driver.find_element(By.ID, "yearbox")).select_by_visible_text("1996")
        Select(driver.find_element(By.XPATH, "//select[@placeholder='Month']")).select_by_index(10)
        Select(driver.find_element(By.XPATH, "//select[@placeholder='Day']")).select_by_index(24)
        log.info("DOB selected")

        # Password

    def test_password(self):
        driver.find_element(By.ID, "firstpassword").send_keys("Password")
        driver.find_element(By.ID, "secondpassword").send_keys("Password")

        # Alert Handling

    def test_alerts(self):
        driver.find_element(By.XPATH, "//a[text()='SwitchTo']").click()
        driver.find_element(By.XPATH, "//a[text()='Alerts']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
        driver.switch_to.alert.accept()

        driver.find_element(By.XPATH, "//a[text()='Alert with OK & Cancel ']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        driver.switch_to.alert.dismiss()

        driver.find_element(By.LINK_TEXT, "Alert with Textbox").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
        driver.switch_to.alert.send_keys("Dilip")
        driver.switch_to.alert.accept()
        log.info("Alert textbox handled")

        # Windows Handling

    def test_windowhandles(self):
        driver.find_element(By.XPATH, "//a[text()='SwitchTo']").click()
        driver.find_element(By.XPATH, "//a[text()='Windows']").click()
        driver.find_element(By.XPATH, "//a/button[@class='btn btn-info']").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        log.info("Switched to new window")
        # time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='Documentation']").click()
        driver.close()
        driver.switch_to.window(windows[0])
        # time.sleep()2

        ##Date Picker

    def test_datepicker(self):
        driver.find_element(By.XPATH, "//a[text()='Widgets']").click()
        driver.find_element(By.XPATH, "//a[text()= ' Datepicker ']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@class = 'form-control is-datepick']").click()

        year = Select(driver.find_element(By.XPATH, "//select[@title= 'Change the year']"))
        time.sleep(3)
        year.select_by_visible_text("2024")
        time.sleep(3)
        month = Select(driver.find_element(By.XPATH, "//select[@title='Change the month']"))
        time.sleep(3)
        month.select_by_index(11)

        try:
            driver.find_element(By.XPATH, "//a[text()='31']").click()
        except:
            log.info("Date 31 not available in the selected month")

        driver.find_element(By.ID, "datepicker1").click()
        for _ in range(12):
            driver.find_element(By.XPATH, "//span[text()='Next']").click()
        driver.find_element(By.XPATH, "//a[text()='24']").click()
        time.sleep(5)

        log.info("Form Fill up Automation Completed")

        driver.quit()

    # Run the automation

# obj = TestRegister()
# obj.test_registration()
