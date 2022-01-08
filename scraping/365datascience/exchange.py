import requests
import json  #load string -> python object  dumps object -> string
base_url = 'http://api.exchangeratesapi.io/v1/latest?access_key=08b93791f69179c067d94fdbfc899ca6'
response = requests.get(base_url)

response.ok
print(response.status_code)
#print(response.text)  #returns text
#print(response.content  # RETURNS CONTENT IN BYtes
#print(response.json())
print(json.dumps(response.json(), indent = 4))   # turns python object back to string
print(response.json().keys())   #returns keys of the dictionary/python object

param_url = 'http://api.exchangeratesapi.io/v1/latest?access_key=08b93791f69179c067d94fdbfc899ca6&symbols=USD,GBP'
response = requests.get(param_url)
data = response.json()  #turns json into python object...a dict
print(data)
print(data['base'])  #since it is a dict, we can access values by entering key
print(data['rates'])

param_url = 'http://api.exchangeratesapi.io/v1/latest?access_key=08b93791f69179c067d94fdbfc899ca6&symbols=GBP'
data = requests.get(param_url).json()
print(data)


#access data from date in past
base_url = 'http://api.exchangeratesapi.io/v1'
historical_url = base_url + "/2016-01-26" + '?access_key=08b93791f69179c067d94fdbfc899ca6&'
response = requests.get(historical_url)
data = response.json()
print(json.dumps(data, indent = 4))


#access data from a range of time
time_pediod = 'http://api.exchangeratesapi.io/v1' + '/timeseries' + '?access_key=08b93791f69179c067d94fdbfc899ca6&' + '&start_date=2017-04-26&end_date=2018-04-26'+'&symbols=GBP'


data = requests.get(time_pediod).json()
print(json.dumps(data, indent = 4))

