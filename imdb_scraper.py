import requests
from bs4 import BeautifulSoup

url = """https://www.imdb.com/showtimes/location?ref_=shlc_ref_rt_usr&
sort=moviemeter,asc&\nst_dt=2019-07-23&mode=showtimes_grid&page=1&user_rating=7.0%2C"""

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
print(soup.find_all("div", {"id":"user_rating"}))
ratings = soup.find_all("div", {"id":"user_rating"})

for x in ratings:
    print(x.strong.text)
print(soup.div['id'])
# movies = soup.find_all("div", class_="lister-item mode-grid")
movies = soup.find_all("div", class_="lister-item-image ribbonize")

# for x in movies:
#     print('---------------')
#     # if x.span['name'] == "alpha":
#     #     print('pass')
#     print(x)

# print(soup.find_all("a"))

print("Movies that have an IMDb rating > 7.0 and currently showing in theaters: ")
movie_id = 0
for movie_title in soup.find_all("div", class_="title"):
    if movie_title.a:
        print(movie_title.a.text.replace("\n", " ").strip(), ratings[movie_id].strong.text)
    else:
        print(movie_title.contents[0].strip())
    movie_id += 1