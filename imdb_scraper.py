import requests
from bs4 import BeautifulSoup
from datetime import date
from email_client import send_email

### todo: add options for more sophisticated parameters and output format

today = date.today()

url = ("""https://www.imdb.com/showtimes/location/{}?ref_=shlc_ref_rt_usr&
sort=moviemeter,asc&st_dt={}&mode=showtimes_grid&page=1&user_rating=7.0%2C""" .format(today, today))

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")

ratings = soup.find_all("div", {"id":"user_rating"})
movies = soup.find_all("div", class_="title")
# movies = soup.find_all("div", class_="lister-item mode-grid")
# movies = soup.find_all("div", class_="lister-item-image ribbonize")

print("Movies that have an IMDb rating > 7.0 and currently showing in theaters: ")
movie_id = 0
result = "\n"
for movie_title in movies:
    if movie_title.a:
        print(movie_title.a.text.replace("\n", " ").strip(), ratings[movie_id].strong.text)
        result += movie_title.a.text.replace("\n", " ").strip() + " --- IMDb rating: "
        result += ratings[movie_id].strong.text + "\n"
    else:
        print(movie_title.contents[0].strip())
    movie_id += 1

print(result)
send_email('chrisok97@gmail.com', result, "Some movies?")