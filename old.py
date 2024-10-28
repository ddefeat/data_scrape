import requests
from bs4 import BeautifulSoup

# NOTE: This code is just reading the first page of the table!

# URL of the website
url = 'https://www.scrapethissite.com/pages/forms/'

# Send a GET request to fetch the raw HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <tr> tags for each row in the table
table = soup.find('table')
#print(table)

titles = table.find_all("tr")[0]

titles_list = [title.text.strip() for title in titles]

cleaned_data = [item.strip() for item in titles_list if item.strip()]

#print(cleaned_data)
rows=table.find_all("tr",class_ = "team")

list=[] # list with [name, year, wins, losses, draws]
for row in rows:
    # Extract each field with a check to avoid AttributeError

    team_name=(row.find('td', class_='name').text.strip())
    year=(row.find('td', class_='year').text.strip())
    wins=(row.find('td', class_='wins').text.strip())
    losses=(row.find('td', class_='losses').text.strip())
    draws=(row.find('td', class_='draws'))
    list.extend([[team_name, year, wins, losses, draws]])

    # Print the data if the field exists, else assign a placeholder (e.g., "N/A")

print("Teams: ",team_name)
print(list)
print(list[3])