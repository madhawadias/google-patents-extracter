from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.webdriver.chrome.options import Options

def patentExtractiion(firstName, secondName):

    options = Options()
    options.add_argument("--headless") #making the browser invisible
    options.add_argument('window-size=1920x1080');
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path= PATH)

    ###############################Start Scraping#################################

    print("Opening Browser")
    driver.get("https://patents.google.com/")
    ##############################################################################
    try:
        print("Searching for text box")
        search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'searchInput'))
                 )
        print("Entering the text in search field")
        if not secondName:  # The variable
            print('It is None')
            search_input.send_keys(firstName)
        else:
            search_input.send_keys('(((' + firstName + ') OR (' + secondName + ')))')
        ##########################################################################

        print("Searching for submit button")
        search_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'searchButton'))
                 )
        print("Clicking the search button")
        search_btn.click()
        ##############################################################################
        print("Searching for the dropdown")
        dropdown_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div[1]/div/metadata-editor/div[4]/restrict-editor/div/div[1]/dropdown-menu[1]/span/span[1]'))
                 )
        print("clicking the dropdown button")
        dropdown_btn.click()
        #############################################################################
        print("searching for US from dropdown")
        dropdown_selection = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div[1]/div/metadata-editor/div[4]/restrict-editor/div/div[1]/dropdown-menu[1]/iron-dropdown/div/div/div/div[2]'))
                 )
        time.sleep(2)
        print("Clicking US from dropdown")
        dropdown_selection.click()

        ################################opening the csv##############################################
        file = open('patent.csv', 'w', newline='', encoding='utf-8')
        header = ['PATENT TITLE', 'PATENT NUMBER', 'PATENT ABSTRACT']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        #############################################################################################



        for i in range(1, 11):
            print(" ##############################################################################")
            print("Searching for the patent link "+ str(i))
            patent_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[2]/div/div/div[1]/section/search-result-item['+str(i)+']/article/state-modifier/a/h3/raw-html/span'))
                     )
            time.sleep(5)
            print(patent_link.text.upper())
            print("clicking on the patent link")
            patent_link.click()
            ##############################################################################
            patent_title = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'title'))
                     )
            patent_title = patent_title.text.upper()
            print(patent_title)
            ##############################################################################
            patent_number = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'pubnum'))
                     )
            patent_number = patent_number.text
            print(patent_number)
            ##############################################################################
            patent_abstract = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'abstract'))
                     )
            patent_abstract = patent_abstract.text
            print(patent_abstract)

            ################################ End Scraping ##############################################

            patent_list = [patent_title,patent_number,patent_abstract]
            print(patent_list)
            writer.writerow({'PATENT TITLE': patent_title,
                             'PATENT NUMBER':patent_number,
                             'PATENT ABSTRACT': patent_abstract})

            ##############################################################################

            driver.back()

        success = ("sucess")
        return  success


    finally:
       driver.quit()











