# EXPLANATION;
# temporarily we do not have api key for refinitiv eikon
# this is a webscraper that we can deploy to cme group to sample what realtime swap prices may look like

import requests
from bs4 import BeautifulSoup
import csv

# url specification
url = "https://www.cmegroup.com/trading/interest-rates/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# this is the hard part
# find the right table to scrape and access it cleanly
data_table = soup.find("table", attrs={"class": "your_class_name"})

# this extracts data and writes to csv with specified title
with open("interest_rate_swaps.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data_table.find_all("tr"):
        columns = [col.text for col in row.find_all("td")]
        writer.writerow(columns)
