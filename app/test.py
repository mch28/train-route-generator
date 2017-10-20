import bs4 as bs
import urllib.request
import pandas as pd
import random

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Category:Lists_of_railway_stations_in_the_United_Kingdom')
soup = bs.BeautifulSoup(source, 'html.parser')

az_links = soup.find_all('div', class_='mw-category-group')[1]

links_dict = {}

for link in az_links.find_all('a'):
    links_dict[link.text] = link['href']

txt = ""

for link in links_dict.values():


    dfs = pd.read_html('https://en.wikipedia.org' + link)
    name_df = dfs[1][0][1:]
    for name in name_df:
        #print(name)
        txt += name + " "

#print(txt)

order = 5
ngrams = {}



def createNgramsDict(txt):
    for i in range(0, (len(txt) - 1)):
        gram = txt[i:i + order]

        if not gram in ngrams:
            ngrams[gram] = []

        if (i + order) < len(txt):
            ngrams[gram].append(txt[i + order])


def markovIt(txt, ngrams):
    currentGram = txt[0:order]
    result = currentGram

    for i in range(0, 12):
        possibilities = ngrams[currentGram]
        nextChar = random.choice(possibilities)
        result += nextChar
        currentGram = result[len(result) - order:len(result)]

    return result


createNgramsDict(txt)
print(markovIt(txt, ngrams))



