from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from time import sleep


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

def extract_url_cars():
    url_base = "https://www.carsguide.com.au/buy-a-car?page={}"
    num_pages = 120
    car_data = []

    for page_number in range(0, num_pages + 1):
        url = url_base.format(page_number)
        driver.get(url)
        time.sleep(10)
        car_listings = driver.find_elements(By.CSS_SELECTOR, "a.carListing")

        for car in car_listings:
            try:
                car_name = car.find_element(By.CSS_SELECTOR, ".carListing--title").text.strip()
                car_url = car.get_attribute("href")
                car_data.append((car_name, car_url))  # Append as a tuple
            except Exception as e:
                print(f"Erreur lors de l'extraction des informations : {e}")

    return car_data

def extract_rows():
    data_list = []
    tables = driver.find_elements(By.CSS_SELECTOR, "table.table")
    for table in tables:
        rows = table.find_elements(By.CSS_SELECTOR, "tr.table--row")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text.strip() for cell in cells]
            data_list.append(row_data)
    return data_list

link_car_data = extract_url_cars()
data = {}
for link in link_car_data:
    driver.get(link[1])
    #search button details
    button_details = driver.find_element(By.CLASS_NAME, "vehicleDetails--seeAllLink")
    button_details.click()
    #extract row data
    wait = WebDriverWait(driver, 10)
    tabs = ["DETAILS", "SPECS"]
    all_details =[]
    for tab_name in tabs:
        tab_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{tab_name}')]")))
        tab_button.click()

        tables = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table")))
        tab_data = extract_rows()
        all_details.extend(tab_data)

        #cleaned data
        cleaned_data = []
        seen = set()
        for row in all_details:
            row_tuple = tuple(row)
            if row_tuple and row_tuple not in seen:
                seen.add(row_tuple)
                cleaned_data.append(row)

        data[link[0]] = cleaned_data


#transfrom to dataframe
data_list = []
for car, details in data.items():
    car_details = dict(details)
    car_details['Car'] = car  # Ajouter le nom de la voiture comme une clé
    data_list.append(car_details)

# Créer le DataFrame
df = pd.DataFrame(data_list)

# Réorganiser les colonnes pour que 'Car' soit la première colonne
columns = ['Car'] + [col for col in df.columns if col != 'Car']
df = df[columns]

df.to_excel('data_car.xlsx', index=False)