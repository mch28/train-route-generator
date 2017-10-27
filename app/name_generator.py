import bs4 as bs
import urllib.request
import pandas as pd
import random




'''Probably will refactor this later'''

class namegen:


    def __init__(self):
        self.order = 5 #default

   # order = 5  # n-size of ngram. will create a set_order method soon

    def prepare_text(self):
        source = urllib.request.urlopen(
            'https://en.wikipedia.org/wiki/Category:Lists_of_railway_stations_in_the_United_Kingdom')
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
                txt += name + ' '

        return txt

    def create_ngrams_dict(self, txt):

        ngrams = {} # is this being inialised inside the method somethign to do with the loss of randomness to the names. All start with eagle now

        for i in range(0, (len(txt) - 1)):
            gram = txt[i:i + self.order]

            if not gram in ngrams:
                ngrams[gram] = []

            if (i + self.order) < len(txt):
                ngrams[gram].append(txt[i + self.order])

        return ngrams

    def markov_it(self, txt, ngrams):
        current_gram = txt[0:self.order]
        result = current_gram

        for i in range(0, 12):
            possibilities = ngrams[current_gram]
            next_char = random.choice(possibilities)
            result += next_char
            current_gram = result[len(result) - self.order:len(result)]

        return result


# text = prepare_text()
# create_ngrams_dict(text)
# print(markov_it(text, ngrams))
