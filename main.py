from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import logging
from lib.config import SleepTime , TargetLang , CsvFileName , InitUrl

logging.basicConfig(level=logging.INFO)

### No GPU mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

class GetAwsAllServicesList():
    def __init__(self) -> None:
        pass
    
    def open_web_page(url:str):
        logging.info(url)
        try:      
            driver.get(url)
            time.sleep(SleepTime)
        except Exception as e:
            raise e

    def check_page_lang_is_en(self):
        try:
            language_selector = driver.find_element(By.ID, 'm-nav-language-selector')
            caret_down_icon = language_selector.find_element(By.CLASS_NAME, "icon-caret-down")
            chinese_text = language_selector.text
        except Exception as e:
            raise e
        
        return chinese_text , caret_down_icon


    def swift_page_to_en(self, caret_down_icon:str):
        try:
            action_chains = ActionChains(driver)
            action_chains.move_to_element(caret_down_icon).click().perform()
            popover = driver.find_element(By.ID, "popover-language-selector")
            language_list = popover.find_elements(By.XPATH, ".//ul[@class='lb-txt-none lb-ul lb-list-style-none lb-tiny-ul-block']/li")
            for language in language_list:
                if language.text == TargetLang:
                    english_link = language.find_element(By.TAG_NAME, "a")
                    english_link.click()
                    break
        except Exception as e:
            raise e
        
    def export_to_csv(self, data: list, fields_list: list):
        try:
            csv_file_path = f"{CsvFileName}.csv"
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.DictWriter(csvfile, fieldnames=fields_list)
                csv_writer.writeheader()
                csv_writer.writerows(data)
            logging.info(f"資料已成功寫入至 {csv_file_path}")
        except Exception as e:
            raise e

    def extract_data(self):   
        data_list = []  
        while True:
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                finder = soup.select("li.lb-xbcol.m-showcase-card.aws-card-item")
                
                for i in finder:
                    data = {
                        'category': i.select_one(".m-category span").text.strip() if i.select_one(".m-category span") else "No data",
                        'service': i.select_one(".m-headline").text.strip() if i.select_one(".m-headline") else "No data",
                        'description': i.select_one(".m-desc").text.strip() if i.select_one(".m-desc") else "No data",
                        'url': i.select_one(".m-card-container a")['href'] if i.select_one(".m-card-container a") else "No data",
                    }                   
                    data_list.append(data)
                    
            except Exception as e:
                raise e
                
            try:
                next_page = soup.select_one("a.m-icon-angle-right.m-active")['href']
                driver.get(next_page)
                time.sleep(SleepTime)
                logging.info(next_page)
            except:
                break
            
        return data_list

    def retrieve_fields_name(self, data_dict:dict):
        return list(set(key for key in data_dict.keys()))
        

    def process(self):
        self.open_web_page(InitUrl)

        current_lang , caret_down_icon = self.check_page_lang_is_en()
        if current_lang != TargetLang:
            self.swift_page_to_en(caret_down_icon)
            time.sleep(SleepTime)

        data = self.extract_data()
        fields_list = self.retrieve_fields_name(data[0])
        self.export_to_csv(data, fields_list)
    
    
if __name__ == "__main__":
    start = GetAwsAllServicesList()
    start.process()






