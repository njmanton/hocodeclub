# use requests and beautiful soup libraries
import requests, bs4, csv, datetime

weeks = [] # list to hold scores
baseUrl = 'http://officialcharts.com/charts/uk-top-40-singles-chart/'
out = './weeks.csv'
startdate = datetime.date(1960, 3, 10) # first week with a top 40
enddate = datetime.date(2016, 3, 18)
#enddate = datetime.date(1960, 3, 24)

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
  url = baseUrl + date + '/750140/'
  page = requests.get(url)

  if (page.status_code == 404):
    print ('{0} [Not found]'.format(url))
  else:
    soup = bs4.BeautifulSoup(page.text, 'html5lib')
    s = 0
    new = 0
    for row in soup.find_all('tr', attrs={'class': None}):
      tds = row.find_all('td')
      try:
        woc = int(tds[4].get_text())
        if woc == 1:
          new = new +1
        s += woc 
      except:
        pass

  print(date, s, new)
  wr.writerow([date, s, new])

dt = startdate
# loop through each week
while (dt <= enddate):
  dt = dt + datetime.timedelta(days = 7)
  extractWoC(dt.strftime('%Y%m%d'))



