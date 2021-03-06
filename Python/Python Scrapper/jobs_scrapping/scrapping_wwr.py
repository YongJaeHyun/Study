import requests
from bs4 import BeautifulSoup


def get_jobs_list(URL):
    jobs_list = []
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    sections = soup.find_all("section", {"class": "jobs"})
    for section in sections:
        jobs_list += section.find_all("li", {"class": "feature"})
    return jobs_list


def get_result(job_list, URL):
    if job_list.find("a"):
        company = job_list.find("span", {"class": "company"}).get_text()
        info = job_list.find("span", {"class": "title"}).get_text()

        deadline = job_list.find("span", {"class": "date"})
        if deadline:
            deadline = deadline.get_text()
        else:
            deadline = job_list.find("span", {"class": "featured"}).get_text()
            print(deadline)
        link = job_list.find("a")["href"]
        if deadline == "featured":
            link = None
        else:
            link = f"https://weworkremotely.com{link}"
    else:
        company, info, deadline, link = [None]*4
    return {"company": company, "info": info, "deadline": deadline, "link": link}


def get_wwr_jobs(word):
    URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = []
    jobs_list = get_jobs_list(URL)
    cnt = 0
    for job_list in jobs_list:
        jobs.append(get_result(job_list, URL))
        cnt += 1
        print(f"Scrapping WeWorkRemotely: List {cnt}")
    return jobs
