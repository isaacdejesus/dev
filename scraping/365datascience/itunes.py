import requests
import json
base_site = "https://itunes.apple.com/search"
url = base_site + '?term=the+beatles&country=us'
requests.get(url)

#another way to do the same thing
r = requests.get(base_site, params = {'term': "the beatles", 'country': "us"})
print(r.status_code)
info = r.json()  #create python object
print(json.dumps(info, indent = 4))  #create formatted string from object
print(info.keys())
print(json.dumps(info['results'][0], indent = 4))  #print first item in results/key
info['resultCount']   #returns number of results which is stored in resultCount key
r = requests.get(base_site, params = {'term': "the beatles", "country": "us", "limit": 200})


import pandas as pd
#create table
song_df = pd.DataFrame(info['results'])
print(song_df)
from openpyxl import Workbook
song_df.to_csv("songs_info.csv")  # turn data into excel files
song_df.to_excel("songs_info.xlsx")
