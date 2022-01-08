import requests
from bs4 import BeautifulSoup

base_site = "https://en.wikipedia.org/wiki/Music"
response = requests.get(base_site)
#print(response.ok)

html = response.content
#print(html[:100])  # prints first 100 elements

soup = BeautifulSoup(html, "html.parser")

with open('wikie_response.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

#soup contains html
#finding elements
soup.find("head")
soup.find('a')  #find only returns first instance 
links =soup.find_all('a') #find_all returns a list 
#find returns None if not found
#find_all returns empty list if not found
#print(len(links))

table = soup.find('tbody')
table.find_all('td')

#navigate down the html tree
table.contents #returns children elements of table
len(table.contents)

#ways to navigate up the html tree
table.parent
table.parent.parent

#Search by attribute
#find div with a given id
#print(soup.find('div', id = 'siteSub'))

#print(soup.find_all('a', class_='mw-jump-link'))

soup.find('a', class_='mw-jump-link', href = '#p-search')

#The above can also be done using a dictionary
#print(soup.find('a', attrs={'class':'mw-jump-link', 'href':'#mw-head'}))

soup.find('div', {'id':'footer'}) #can also use dictionary without attrs


#extract data from html tree
a = soup.find('a', class_='mw-jump-link')
a.name

#can access values by enterin key values like in dict
#print(a['href'])

#a['class_']  ##returns error if not found

#another way to access values
a.get('href')  ## return None if not found

#print(a.attrs)  #returns all attributes: key/value


###extract text from tags
#both return string within tag
a.string
a.text


p = soup.find_all('p')[1]  #second paragraph in html

#print(p.text)
#print(p.string)

p.parent #navigates up the tree 
#print(p.parent.text)  #extract text from parent

#iterate through all strings in element
for s in p.strings:
    print(repr(s))  #repr forces string representation

#removes extra spaces
for s in p.stripped_strings:
    print(repr(s))


#links
link = links[26]  #selects link stored in 26th location of link array
link.string

link['href'] #get link
#however in this case link is relative to current location
#returns '/wiki/Culture'
#in order to get full url need to join base_url + returned path

from urllib.parse import urljoin
relative_url = link['href']
full_url = urljoin(base_site, relative_url)
#print(full_url)

#use list comprehension to grab all links
[l.get('href') for l in links]
#get list without None values
clean_links = [l for l in links if l.get('href')!= None ]
relative_urls = [l.get('href') for l in clean_links]
full_urls = [urljoin(base_site, url) for url in relative_urls]
#print(full_urls)

#get links to another wikipage
internal_links = [url for url in full_urls if 'wikipedia.org' in url]
#print(internal_links)


#extract data from nested tags
div_notes = soup.find_all('div', {'role':'note'})
div_notes[0].find('a') #find link in first

#fails to return all links because using find
div_links = [div.find('a') for div in div_notes]

div_links = []
for div in div_notes:
    anchors = div.find_all('a')

    for a in anchors:
        div_links.append(a)
note_urls = [urljoin(base_site, l.get('href')) for l in div_links]
print(note_urls)


#extract main text from multiple pages
par_text = []
i = 0
for url in note_urls:
    note_resp = requests.get(url)
    if note_resp.status_code == 200:
        print('URL #{0}: {1}'.format(i+1, url))
    else:
        print("Status code {0}: Skipping URL #{1}: {2}".format(note_resp.status_code, i+1, url))
        i = i + 1
        continue
    note_html = note_resp.content
    note_soup = BeautifulSoup(note_html, 'lxml')
    note_pars = note_soup.find_all('p')
    text = [p.text for p in note_pars]
    par_text.append(text)
    i = i + 1

par_text[0]
page_text = "".join(par_text[0])

page_text = ["".join(text) for text in par_text]

print(page_text[3])
#retrieve text by entering url
url_to_text = dict(zip(note_urls, page_text))

print(url_to_text['url'])
