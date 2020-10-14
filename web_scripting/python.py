import requests 

from bs4 import BeautifulSoup

URL = "https://www.indeed.co.uk/jobs?q=software+developer&l=Hatfield"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser') 
results = soup.find(id= 'resultsBody')
# print(results.prettify())

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result') 

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_="title")
    company_elem = job_elem.find('span', class_="company")
    location_elem = job_elem.find('div', class_="location accessible-contrast-color-location")
    salary_elem = job_elem.find('span', class_="salaryText")
    if None in (title_elem, company_elem, location_elem, salary_elem):
        continue
    print(title_elem.text.strip(), end="\n"*2) 
    print(company_elem.text.strip(), end="\n"*2)
    print(location_elem.text.strip(), end="\n"*2)
    print(salary_elem.text.strip(), end="\n"*2)
    
    
