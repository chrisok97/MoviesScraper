import requests

url = 'http://www.omdbapi.com/?y=205&apikey=b43c7099'

r = requests.get(url)

data = r.json()

# rating = data['Ratings'][0]['Value']

# print("IMDb score: {}" .format(rating))
print(data)