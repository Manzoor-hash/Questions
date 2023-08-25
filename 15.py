import requests
from bs4 import BeautifulSoup
import csv


url = 'https://example.com'  

response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')


data_list = []
for item in soup.find_all('div', class_='item'):
    title = item.find('h2').text.strip()
    description = item.find('p').text.strip()
    data_list.append((title, description))


csv_file = 'scraped_data.csv'


with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Title', 'Description'])  # Write header row
    csv_writer.writerows(data_list)

print(f"Scraped data saved to {csv_file}")