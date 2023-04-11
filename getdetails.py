import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.imdb.com/title/tt0111161/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('title').text.strip()
rating = float(soup.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV').text)
vote_count = int(soup.find('div', class_='AggregateRatingButton__TotalRatingAmount-sc-1ll29m0-3 jkCVKJ').text.replace(',', ''))
description = soup.find('span', class_='GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA').text.strip()
release_date = soup.find('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex').text.strip()

movie_data = {
    'title': title,
    'rating': rating,
    'vote_count': vote_count,
    'description': description,
    'release_date': release_date
}

with open('movie_data.json', 'w') as json_file:
    json.dump(movie_data, json_file, indent=4)

print("Data saved to movie_data.json")


