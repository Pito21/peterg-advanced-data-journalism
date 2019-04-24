import urllib2, csv
import json, ast
from bs4 import BeautifulSoup

csvfile = open('bills.csv', 'a')
bill_writer = csv.writer(csvfile, delimiter="-")

url = 'https://www.senate.mo.gov/19info/BTS_Web/TrulyAgreed.aspx?SessionType=R'
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tbody = soup.find('table', {'id': 'dgBillList'})

rows = tbody.find_all('tr')

for row in rows:

    data = []

    cells = row.find_all('tr')

    for cell in cells:

        data.append(cell.text.replace("\n", "").replace("'","").split("-"))

    datajoin = ast.literal_eval(json.dumps(data))

    print datajoin

    bill_writer.writerow(datajoin)
