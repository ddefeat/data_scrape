import requests
from bs4 import BeautifulSoup

# Define a function to scrape a single page
def scrape_page(url):
    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table containing data
    table = soup.find('table')
    if not table:
        return []  # If no table is found, return an empty list

    # Initialize the list to store team data
    team_data = []  # list of lists with [name, year, wins, losses, draws]

    # Find all rows with class 'team'
    rows = table.find_all("tr", class_="team")
    
    for row in rows:
        # Extract each field, checking for existence to avoid AttributeError
        team_name = row.find('td', class_='name').text.strip() if row.find('td', class_='name') else 'N/A'
        year = row.find('td', class_='year').text.strip() if row.find('td', class_='year') else 'N/A'
        wins = row.find('td', class_='wins').text.strip() if row.find('td', class_='wins') else 'N/A'
        losses = row.find('td', class_='losses').text.strip() if row.find('td', class_='losses') else 'N/A'
        draws = row.find('td', class_='draws').text.strip() if row.find('td', class_='draws') else 'N/A'
        
        # Append the row data as a list to team_data
        team_data.append([team_name, year, wins, losses, draws])

    return team_data

# Main function to scrape multiple pages
def main():
    all_teams_data = []

    # Loop through pages
    for i in range(1, 25):  # 24 pages, adjust as necessary
        page_url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
        page_data = scrape_page(page_url)
        all_teams_data.extend(page_data)

    # Print the complete data
    for team in all_teams_data:
        print(team)

    return all_teams_data

# Execute the main function and collect data
all_teams_data = main()