import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"

def get_html():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    html = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li")
    return html

def get_links(jobs_html):
    companies = []
    for html in jobs_html[:-2]:
        name = html.find("a").find("span", {"class": "company"}).get_text().replace("/", "&")
        link = html.find("a")["href"]
        companies.append({"name": name, "link": link})
    return companies

def get_link_html(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    link_html = soup.find("div", {"id": "NormalInfo"}).find("table").find("tbody").find_all("tr", {"class": ""})
    return link_html

def get_job_lists(link_html):
    if link_html.find("td", {"class": "local"}):
        place = link_html.find("td", {"class": "local"}).get_text().replace(u'\xa0',u' ')
        title = link_html.find("td", {"class": "title"}).find("a").find("span", {"class": "company"}).get_text(strip=True)
        time = link_html.find("td", {"class": "data"}).find("span").get_text()
        pay = link_html.find("td", {"class": "pay"}).get_text()
        date = link_html.find("td", {"class": "regDate"}).get_text()
    else:
        place, title, time, pay, date = [None]*5
    return {"place": place, "title": title, "time": time, "pay": pay, "date": date}
    
    
        
def get_jobs():
    html = get_html()
    companies = get_links(html)
    cnt = 0
    for company in companies:
        company["job"] = []
        link_html = get_link_html(company["link"])
        for html in link_html:
            company["job"].append(get_job_lists(html))
        cnt += 1
        print(f"Scrapping Alba: Link {cnt}")
    return companies
