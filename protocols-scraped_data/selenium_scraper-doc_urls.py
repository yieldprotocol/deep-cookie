import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def driversetup(DRIVER_PATH):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    return driver

def pagesource(url, driver):
    driver = driver
    driver.get(url)
    page_source = driver.page_source
    # soup = BeautifulSoup(page_source)
    driver.close()
    return page_source #, soup

#          ------main------
# patterns = ['faq', 'doc']

with open("all_protocol_urls.txt", "r") as f:
    data = f.read()
    all_protocol_urls = data.split("\n")
    
all_doc_urls, no_doc_urls, not_parsed_urls = [], [], []
for url in all_protocol_urls:
    driver = driversetup(DRIVER_PATH='/chromedriver')
    try: 
        raw_html = pagesource(url=url, driver=driver)
        urls_on_page = set(re.findall(r'(https?://[^\s]+)', raw_html))
        urls_on_page = [u.split('''"''')[0] for u in urls_on_page]
        urls_on_page = [u for u in urls_on_page if len(u)<55]
        urls_on_page = [u for u in urls_on_page if 'doc' in u or 'blog' in u or 'faq' in u]
        urls_on_page = [u for u in urls_on_page if '.png' not in u and '.jpg' not in u and '.jpeg' not in u]
        all_doc_urls.extend(urls_on_page)
        if len(urls_on_page)==0: no_doc_urls.append(url)

        with open('all_doc_urls.txt','w') as f:
            f.write('\n'.join(all_doc_urls))
        with open('no_doc_urls.txt','w') as f:
            f.write('\n'.join(no_doc_urls))

        print(f"scraped--{url}")
    except: 
        not_parsed_urls.append(url)
        with open('not_parsed_urls.txt','w') as f:
            f.write('\n'.join(not_parsed_urls))
        pass

    time.sleep(5)