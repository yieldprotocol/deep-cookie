# import re
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# def driversetup(DRIVER_PATH):
#     options = Options()
#     options.headless = True
#     options.add_argument("--window-size=1920,1200")

#     driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#     return driver

# def pagesource(url, driver):
#     driver = driver
#     driver.get(url)
#     time.sleep(5) # to let the page load
#     page_source = driver.page_source
#     # soup = BeautifulSoup(page_source)
#     driver.close()
#     return page_source #, soup

# def get_corpus(soup):
#     corpus = ""
#     for s in soup.find_all(['header', 'title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
#         corpus += str(s.text) + '\n'
#     return corpus

# def save_corpus(corpus, url, save_dir):
#     with open(f"{save_dir}/{'_'.join(url.split('/')).replace('https:', '')}.txt",'w') as f:
#         f.write(corpus)

# def get_all_contents(url, save_dir):
#     driver = driversetup(DRIVER_PATH='/chromedriver')
#     raw_html = pagesource(url=url, driver=driver)
#     soup = BeautifulSoup(raw_html, 'html.parser')
#     corpus = get_corpus(soup)
#     save_corpus(corpus, url, save_dir)
    
#     urls_on_page = set(re.findall(r'(https?://[^\s]+)', raw_html))
#     urls_on_page = [u.split('''"''')[0] for u in urls_on_page]
#     urls_on_page = [u for u in urls_on_page if len(u)<65]
#     urls_on_page = [u for u in urls_on_page if 'doc' in u or 'blog' in u or 'faq' in u]
#     urls_on_page = [u for u in urls_on_page if '.png' not in u and '.jpg' not in u and '.jpeg' not in u and '.pdf' not in u]
#     # print(urls_on_page)
#     # return 
#     with open('done_scraping_docs.txt','r') as f:
#         data = f.read()
#         done_scraping_docs = data.split("\n")
#     done_scraping_docs.append(url)
#     done_scraping_docs = set(done_scraping_docs)
#     with open('done_scraping_docs.txt','w') as f:
#         f.write('\n'.join(done_scraping_docs))

#     for url_on_page in urls_on_page: 
#         if url_on_page in done_scraping_docs: continue
#         try:
#             get_all_contents(url_on_page, save_dir)
#         except:
#             with open('not_parsed_doc_urls.txt','r') as f:
#                 data = f.read()
#                 not_parsed_doc_urls = data.split("\n")
#             not_parsed_doc_urls.append(url_on_page)
#             not_parsed_doc_urls = set(not_parsed_doc_urls)
#             with open('not_parsed_doc_urls.txt','w') as f:
#                 f.write('\n'.join(not_parsed_doc_urls))
#             pass



# #          ------main------
# with open("all_doc_urls.txt", "r") as f:
#     data = f.read()
#     all_doc_urls = data.split("\n")
    
# save_dir = "protocol-documentations"
# for url in all_doc_urls:
#     try: 
#         get_all_contents(url, save_dir)
#     except: 
#         with open('not_parsed_doc_urls.txt','r') as f:
#             data = f.read()
#             not_parsed_doc_urls = data.split("\n")
#         not_parsed_doc_urls.append(url)
#         not_parsed_doc_urls = set(not_parsed_doc_urls)
#         with open('not_parsed_doc_urls.txt','w') as f:
#             f.write('\n'.join(not_parsed_doc_urls))
#         pass

import re
import time
import os, sys, requests, json
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
    time.sleep(5) # to let the page load
    page_source = driver.page_source
    # soup = BeautifulSoup(page_source)
    driver.close()
    return page_source #, soup

def get_corpus(soup):
    corpus = ""
    for s in soup.find_all(['header', 'title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        corpus += str(s.text).strip() + '\n'
    return corpus

def save_corpus(corpus, url, parent_url):
    url = re.sub("http:|https:", '', url)
    parent_url = re.sub("http:|https:", '', parent_url)
    os.makedirs(f"{'_'.join(parent_url.split('/'))}", exist_ok=True)
    if not os.path.exists(f"{'_'.join(parent_url.split('/'))}.json"):
        name_map = {}
    else:
        with open(f"{'_'.join(parent_url.split('/'))}.json", 'r') as f:
            name_map = json.load(f)
    num = len(name_map.keys())
    name_map[num] = url
    with open(f"{'_'.join(parent_url.split('/'))}.json", 'w') as f:
        json.dump(name_map, f)
    with open(f"{'_'.join(parent_url.split('/'))}/{num}.txt",'w') as f:
        f.write(corpus)


def get_all_contents(url, parent_url, depth):
    try:
        driver = driversetup(DRIVER_PATH='/chromedriver')
        raw_html = pagesource(url=url, driver=driver)
    except:
        with open('not_parsed_doc_urls.txt','r') as f:
            data = f.read()
            not_parsed_doc_urls = data.split("\n")
        not_parsed_doc_urls.append(url)
        not_parsed_doc_urls = set(not_parsed_doc_urls)
        with open('not_parsed_doc_urls.txt','w') as f:
            f.write('\n'.join(not_parsed_doc_urls))
        return

    # raw_html = response.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    corpus = get_corpus(soup)
    save_corpus(corpus, url, parent_url)
    print(url)

    urls_on_page = set(re.findall(r'(https?://[^\s]+)', raw_html))
    urls_on_page = [u.split('''"''')[0] for u in urls_on_page]
    urls_on_page = [u.split(')')[0] for u in urls_on_page]
    urls_on_page = [u for u in urls_on_page if len(u)<65]
    urls_on_page = [u for u in urls_on_page if 'doc' in u or 'blog' in u or 'faq' in u]
    urls_on_page = [u for u in urls_on_page if '.png' not in u and '.jpg' not in u and '.jpeg' not in u and '.pdf' not in u]
    
    with open('done_scraping_docs.txt','r') as f:
        data = f.read()
        done_scraping_docs = data.split("\n")
    done_scraping_docs.append(url)
    done_scraping_docs = set(done_scraping_docs)
    with open('done_scraping_docs.txt','w') as f:
        f.write('\n'.join(done_scraping_docs))

    for url_on_page in urls_on_page: 
        if url_on_page not in done_scraping_docs:
            depth += 1 
            if depth>depth_allowed: return
            get_all_contents(url_on_page, parent_url, depth)



#          ------main------
with open("all_doc_urls.txt", "r") as f:
    data = f.read()
    all_doc_urls = data.split("\n")

depth_allowed = 10
for url in all_doc_urls:
    get_all_contents(url, url, depth=0)