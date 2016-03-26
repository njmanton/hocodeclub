# use requests and beautiful soup libraries
import requests, bs4, csv, datetime

weeks = [] # list to hold scores
baseUrl = 'http://billboard.com/charts/hot-100/'
out = './weeks_bb.csv'
startdate = datetime.date(1960, 8, 27) # match to first uk top 40 
enddate = datetime.date(2016, 3, 26)

myfile = open(out, 'w', newline='\n')
# write the responses out to a file
wr = csv.writer(myfile, dialect="excel", delimiter=',')

def extractWoC(date):
  '''
  Given a date string,
  Scrape the top 40 WoC figures and aggregate them

  the chart data is in the main table on the page,
  the individual tracks are in the <tr> _without_ a class attribute
  '''
  url = baseUrl + date
  page = requests.get(url)

  if (page.status_code == 404):
    print ('{0} [Not found]'.format(url))
  else:
    s = 0
    new = 0
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    for div in soup('div', class_='chart-row__stats')[0:40]:
      values = div.find_all('span', class_='chart-row__value')
      if (values[0].get_text() == '--' or int(values[0].get_text()) > 40):
        new = new + 1
      s += int(values[2].get_text())

  print(date, s, new)
  wr.writerow([date, s, new])

dt = startdate
# loop through each week
while (dt <= enddate):
  dt = dt + datetime.timedelta(days = 7)
  extractWoC(dt.strftime('%Y-%m-%d'))
