import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://recreation.northeastern.edu/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')


print(soup)

# s = soup.find_all('div')
# print(s)

# content = s.find_all('span')
# print(content)