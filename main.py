import json
import requests
import wikipedia
url = 'https://ru.wikipedia.org/wiki/'
with open('countries.json') as json_file:
    data = json.load(json_file)



class Countries_iterator:
    def __init__(self, list_of_countries):
        self.list_of_countries = list_of_countries
        self.country_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = self.list_of_countries[self.country_index]
        if self.country_index != len(self.list_of_countries):
            with open('doc.txt', 'a', encoding='utf-8') as file:
                file.write(f' {wikipedia.page(wikipedia.search(item)[0]).links} - {item["name"]["common"]} \n')
            self.country_index += 1
        else:
            raise StopIteration
        return item



for p in Countries_iterator(data):
    print(p['name']['common'])


