import requests
from bs4 import BeautifulSoup
base_site = "https://editorial.rottentomatoes.com/guide/140-essential-action-movies-to-watch-now/"
response = requests.get(base_site)

html = response.content
soup = BeautifulSoup(html, 'lxml')
#with open('Rotten_tomatoes_lxml_parser.html', 'wb') as file:
#        file.write(soup.prettify('utf-8'))

divs = soup.find_all('div', {'class':'col-sm-18 col-full-xs countdown-item-content'})
#extract title and year of each movie
headings = [div.find('h2') for div in divs]
movie_names = [heading.find('a').string for heading in headings]
print(movie_names)

years = [heading.find('span', class_ = 'start-year').string for heading in headings]
years = [year.strip('()') for year in years]
years = [int(year) for year in years]
print(years)


