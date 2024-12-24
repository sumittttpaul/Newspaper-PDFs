import requests
from datetime import datetime
from bs4 import BeautifulSoup

print('Retrieving Newspapers')

URLs = []
Newspapers = []

GoogleDrive_Keyword = 'drive.google.com'

EconomicsTimes_Keywords = 'economic-times'
TimesOfIndia_Keywords = 'times-of-india'
FinancialExpress_Keywords = 'financial-express'
Statesman_Keywords = 'statesman'
AsianAge_Keywords = 'the-asian-age'

res = requests.get('https://www.dailyepaper.in/daily-news/')
soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        URLs.append(href)

EconomicsTimes_Link = [i for i in URLs if EconomicsTimes_Keywords in i]
TimesOfIndia_Link = [i for i in URLs if TimesOfIndia_Keywords in i]
FinancialExpress_Link = [i for i in URLs if FinancialExpress_Keywords in i]
Statesman_Link = [i for i in URLs if Statesman_Keywords in i]
AsianAge_Link = [i for i in URLs if AsianAge_Keywords in i]

print('Economics Times')

# Economics Times
if len(EconomicsTimes_Link) > 0:
    URLs.clear()
    res = requests.get(str(EconomicsTimes_Link[0]))
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            URLs.append(href)
    EconomicsTimes_Link = [i for i in URLs if GoogleDrive_Keyword in i]
    if len(EconomicsTimes_Link) > 0:
        Newspapers.append(str(EconomicsTimes_Link[0]))
else:
    Newspapers.append('Not Available')

print('Times Of India')

# Times Of India
if len(TimesOfIndia_Link) > 0:
    URLs.clear()
    res = requests.get(str(TimesOfIndia_Link[0]))
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            URLs.append(href)
    TimesOfIndia_Link = [i for i in URLs if GoogleDrive_Keyword in i]
    if len(TimesOfIndia_Link) > 0:
        Newspapers.append(str(TimesOfIndia_Link[0]))
else:
    Newspapers.append('Not Available')

print('Financial Express')

# Financial Express
if len(FinancialExpress_Link) > 0:
    URLs.clear()
    res = requests.get(str(FinancialExpress_Link[0]))
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            URLs.append(href)
    FinancialExpress_Link = [i for i in URLs if GoogleDrive_Keyword in i]
    if len(FinancialExpress_Link) > 0:
        Newspapers.append(str(FinancialExpress_Link[0]))
else:
    Newspapers.append('Not Available')

print('Statesman')

# Statesman
if len(Statesman_Link) > 0:
    URLs.clear()
    res = requests.get(str(Statesman_Link[0]))
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            URLs.append(href)
    Statesman_Link = [i for i in URLs if GoogleDrive_Keyword in i]
    if len(Statesman_Link) > 0:
        Newspapers.append(str(Statesman_Link[0]))
else:
    Newspapers.append('Not Available')

print('Asian Age')

# Asian Age
if len(AsianAge_Link) > 0:
    URLs.clear()
    res = requests.get(str(AsianAge_Link[0]))
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            URLs.append(href)
    AsianAge_Link = [i for i in URLs if GoogleDrive_Keyword in i]
    if len(AsianAge_Link) > 0:
        Newspapers.append(str(AsianAge_Link[0]))
else:
    Newspapers.append('Not Available')

Date = datetime.now().date().strftime("%d %b %Y")

File = open("Latest Newspapers.txt", "w")
File.write('*News Paper - ' + str(Date) +'*' + '\nEconomics Times : ' + str(Newspapers[0]) + '\nTimes of India : ' + str(Newspapers[1]) + '\nFinancial Express : ' + str(Newspapers[2]) + '\nStatesman : ' + str(Newspapers[3]) + '\nAsian Age : ' + str(Newspapers[4]))
File.close()

print('Newspapers save successfully on "Latest Newspapers.txt"')
