import requests
import json
APP_ID ='ee6b6ad5'
APP_KEY = 'a24f747f0ca3877c37bd7555aba9f278'
api_endpoint = 'https://api.edamam.com/api/nutrition-details'

url = api_endpoint + "?app_id=" + APP_ID + "&app_key=" + APP_KEY

#send post request
headers = {'Content-Type': 'application/json'}
recipe = {
    'title': 'Cappuccino',
    'ingr': ['18g ground espresso', '150ml milk']
}

r = requests.post(url, headers  = headers, json = recipe)
print(r.status_code)
capp_info = r.json()
capp_info.keys()
print(json.dumps(capp_info["totalNutrients"], indent = 4))

#import pandas to build dataframe/table))

import pandas as pd
pd.DataFrame(capp_info["totalNutrients"])

capp_nutrients = pd.DataFrame(capp_info["totalNutrients"]).transpose()
capp_nutrients.to_csv("Cappucchino_nutrients.csv")
