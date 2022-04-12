import requests
from bs4 import BeautifulSoup

# Get article text from online news sites. Only tested on Ghanaian sites.
# Arguments: `url` for link to relevant webpage, `tag` for article text id and `class_id` for CSS class id 

def scrape(url, tag, class_id): 
    
    r = requests.get(url)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, "lxml")
    soup_html = soup.find(tag, class_= class_id)
    text = soup_html.text

    return text

e_levy = scrape(url="https://www.myjoyonline.com/e-levy-full-list-of-transfers-that-will-not-attract-charges/", tag="div", class_id="mt-3")

print(e_levy)