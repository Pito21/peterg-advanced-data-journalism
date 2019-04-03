#Imports two libraries - urllib2 used for fetching URLs, and csv used for reading and writing .csv files.
import urllib2, csv

#Imports the BeautifulSoup library
from bs4 import BeautifulSoup

#Opens the jaildata .csv file in write mode and calls the writer
outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)

#References the URL containing the data to be scraped, sets the max rows to 500 so that all detainees will be displayed on a single page.
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#Reads the url and stores the result of calling the read() method in the variable "html"
html = urllib2.urlopen(url).read()

#Parses the html using BeautifulSoup, the result is stored in the variable "soup"
soup = BeautifulSoup(html, "html.parser")

#tbody with class "stripe" contains the table with the targeted data. BeautifulSoup locates the tag with this class, isolating it from other irrelevant information on the website.
tbody = soup.find('tbody', {'class': 'stripe'})

#Creates a new variable "rows" pulling the values of all rows (odd and even).
rows = tbody.find_all('tr')

#Loops through the rows.
for row in rows:

#Creates a new variable "cells" pulling the value of each individual cell.
    cells = row.find_all('td')

#Creates an empty list to fill with the collected data in a string format.
    data = []

#Loops through all individual cells and copies their content into the list.
    for cell in cells:
        data.append(cell.text.encode('utf-8'))

#Writes the collected data into the specified file.
writer.writerow(data)
