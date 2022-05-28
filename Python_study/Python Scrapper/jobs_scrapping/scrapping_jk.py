import requests
from bs4 import BeautifulSoup


def get_jobs_list(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs_list = soup.find("div", {"class": "list-default"}).find_all("li")
    return jobs_list


def get_result(job_list, URL):
    if job_list.find("div", {"class": "post-list-info"}):
        company = job_list.find(
            "div", {"class": "post-list-corp"}).find("a").get_text()
        info = job_list.find(
            "div", {"class": "post-list-info"}).find("a")["title"]
        deadline = job_list.find(
            "span", {"class": "date"}).get_text().replace("~", "")
        link = job_list.find(
            "div", {"class": "post-list-info"}).find("a")["href"]
    else:
        company, info, deadline = [None]*3
    return {"company": company, "info": info, "deadline": deadline, "link": f"https://www.jobkorea.co.kr{link}"}


def get_jk_jobs(word):
    URL = f"https://www.jobkorea.co.kr/search/?stext={word}"
    jobs = []
    jobs_list = get_jobs_list(URL)
    cnt = 0
    for job_list in jobs_list:
        jobs.append(get_result(job_list, URL))
        cnt += 1
        print(f"Scrapping JK: List {cnt}")
    return jobs
