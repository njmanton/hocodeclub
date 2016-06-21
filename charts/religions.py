# use beautiful soup
import bs4, codecs

# text from https://en.wikipedia.org/wiki/List_of_religions_and_spiritual_traditions
filename = './religions.htm'

fl = codecs.open(filename, encoding="utf-8")
soup = bs4.BeautifulSoup(fl, 'html.parser')

# define a custom bs4 filter to limit tags to h3>span (headers) or li>a (list items)
# this is really crude, but effective at getting the raw text of religion names
def filter(tag):
    return (tag.name == 'span' and tag.parent.name == 'h3') or (tag.name == 'a' and tag.parent.name == 'li')


tags = soup.findAll(filter)
out = []
# loop through the tags
for tag in tags:
  # the edit link appears in a h3>span tag
  if tag.get_text() != '[edit]':
    # thi sis a header
    if tag.name == 'span':
      ele = '*' + tag.get_text() + '*'
    else:
      # go up the parse tree to see if this is a sub category
      # only go up level as main goal is to extract religion name
      if tag.parent.parent.parent.name == 'li':
        ele = '- ' + tag.get_text()
      else:
        ele = tag.get_text()
    out.append(ele)

# dump results to stdout
for e in out:
  print(e)
