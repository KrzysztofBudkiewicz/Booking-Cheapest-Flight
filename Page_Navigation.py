from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Chrome_Driver import *
import time
import datetime

class MainPage():
    # open start page
    def select_page():
        driver.get("https://www.booking.com/")
        driver.implicitly_wait(5)

    # accept cookies and go to the "flights" tab
    def select_flights():
        accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookies.click()
        flights = driver.find_element(By.ID, "flights")
        flights.click()

    # select ticket
    def select_ticket(ticket):
        try:
            ticket_type = driver.find_element(By.ID, ticket)
            ticket_type.click()
        except Exception:
            pass
        time.sleep(2)

    # select cabin class
    def select_cabin_class(cabin):
        try:
            cabin_type = Select(driver.find_element(
                By.XPATH, '//select[@data-ui-sr="cabin_class_input"]'))
            cabin_type.select_by_index(cabin)
        except Exception:
            pass
        time.sleep(2)

    # select extra adult passengers, 1 adult is the default result
    def select_adult_passengers(numbers):
        travelers = driver.find_element(
            By.XPATH, '//button[@data-ui-sr="occupancy_input"]')
        travelers.click()
        time.sleep(2)
        for number in range(numbers):
            try:
                adults = driver.find_element(
                    By.XPATH, '//button[@data-ui-sr="occupancy_adults_input_plus"]')
                adults.click()
            except Exception:
                pass
        time.sleep(2)
        print("The number of adult passengers is:", 1 + numbers)

    # select the number of children and the age for each child
    def select_children_passengers(numbers: int, *ages: int):
        for number in range(numbers):
            try:
                children = driver.find_element(
                    By.XPATH, '//button[@data-ui-sr="occupancy_children_input_plus"]')
                children.click()
                xpath_variable = 0
                for age in ages:
                    children_age = Select(driver.find_element(
                        By.XPATH, '//select[@data-ui-sr="occupancy_children_age_input_%s"]' % xpath_variable))
                    children_age.select_by_index(age+1)
                    xpath_variable += 1
            except Exception:
                pass
        time.sleep(2)
        print("The number of children passengers is:", numbers)

    # if you want a direct flight
    def select_only_direct_flights():
        only_direct_flights = driver.find_element(
            By.XPATH, '//span[2][@class="InputCheckbox-module__field___lH8uR"]')
        only_direct_flights.click()
        time.sleep(2)

    # select departure city
    def select_departure_city(city):
        fly_from = driver.find_element(
            By.XPATH, '//button[1][@data-ui-sr="location_input_from_0"]')
        fly_from.click()
        time.sleep(2)
        delete_proposed_airport = driver.find_element(
            By.XPATH, '//span[2][@class="Icon-module__root___0jUKs css-lyj9ft Icon-module__root--size-small___AvlR0"]')
        delete_proposed_airport.click()
        time.sleep(2)
        departure_airport = driver.find_element(
            By.XPATH, '//input[@class="css-1ejj2j9"]')
        departure_airport.click()
        departure_airport.clear()
        departure_airport.send_keys(city)
        time.sleep(2)
        first_airport = driver.find_element(
            By.XPATH, '//*[@id="__bui-10"]/div/div/div/div/div/div/ul/li[1]/span[2]/span/b')
        first_airport.click()
        time.sleep(2)

    # select arrival city
    def select_arrival_city(city):
        fly_to = driver.find_element(
            By.XPATH, '//span[@class="Text-module__root--variant-body_2___EUWSn Text-module__root--color-disabled___7nWnK"]')
        fly_to.click()
        arrival_airport = driver.find_element(
            By.XPATH, '//input[@class="css-1ejj2j9"]')
        arrival_airport.click()
        arrival_airport.clear()
        arrival_airport.send_keys(city)
        time.sleep(2)
        first_airport = driver.find_element(
            By.XPATH, '//*[@id="__bui-12"]/div/div/div/div/div/div/ul/li[1]/span[2]/span/b')
        first_airport.click()
        time.sleep(2)

    # select departure date
    def select_departure_date(days_from_today: int):
        calendar_button = driver.find_element(
            By.XPATH, '//*[@id="basiclayout"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/button/div[1]/span[2]/span')
        calendar_button.click()
        time.sleep(2)
        date = (datetime.datetime.today() +
                datetime.timedelta(days=days_from_today)).strftime("%Y-%m-%d")
        departure_date = driver.find_elements(By.XPATH, "//table/tbody/tr/td/span")
        for i in departure_date:
            if i.get_attribute("data-date") == date:
                i.click()
                time.sleep(2)
                break

    # select arrival date           
    def select_arrival_date(days_from_today: int):
        date = (datetime.datetime.today() +
                datetime.timedelta(days=days_from_today)).strftime("%Y-%m-%d")
        arrival_date = driver.find_elements(By.XPATH, "//table/tbody/tr/td/span")
        for i in arrival_date:
            if i.get_attribute("data-date") == date:
                i.click()
                time.sleep(2)
                break

    # click the "search" button       
    def search_flights():
        search_button = driver.find_element(
            By.XPATH, '//*[@id="basiclayout"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div/button/span')
        search_button.click()
        time.sleep(5)
