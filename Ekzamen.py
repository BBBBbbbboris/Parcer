import requests
from bs4 import BeautifulSoup

url = "https://kups.club/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.Session()

response = session.get(url, headers=header)

def get_info():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row mt-4")  # div со всеми карточками
        products = allProduct.find_all("div",class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
        for i in range(len(products)):
            print(products[i])
            break

get_info()
