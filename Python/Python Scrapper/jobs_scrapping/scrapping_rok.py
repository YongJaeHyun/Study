from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)


def get_jobs_list(URL):
    driver.get(URL)
    driver.implicitly_wait(10)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    jobs_list = soup.find("tbody").find_all("tr", {"class": "job"})
    return jobs_list


def get_result(job_list, URL):
    if job_list.find("td"):
        company = job_list.find("h3", {"itemprop": "name"}).get_text()
        info = job_list.find("h2", {"itemprop": "title"}).get_text()
        deadline = job_list.find("time").get_text().replace(
            "d", "day").replace("mo", "month").replace("yr", "year")
        deadline = "~" + deadline
        link = job_list.find("td", {"class": "source"})
        if link.find("a"):
            link = link.find("a")["href"]
            link = f"https://remoteok.io{link}"
        else:
            link = None
    else:
        company, info, deadline, link = [None]*4
    return {"company": company, "info": info, "deadline": deadline, "link": link}


def get_rok_jobs(word):
    URL = f"https://remoteok.io/{word}"
    jobs = []
    jobs_list = get_jobs_list(URL)
    cnt = 0
    for job_list in jobs_list:
        jobs.append(get_result(job_list, URL))
        cnt += 1
        print(f"Scrapping RemoteOK: List {cnt}")
    return jobs
