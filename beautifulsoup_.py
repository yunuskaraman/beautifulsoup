import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html , "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")

count=0

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    reyting=tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}:filmin adi : {title.ljust(30)} filmin yılı : {year} film değerlendirmesi : {reyting}")
    count+=1
