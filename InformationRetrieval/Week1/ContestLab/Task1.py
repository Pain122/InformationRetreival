import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import re

with open('input.txt', 'r') as fin:
    url = fin.read()

loot = 'some random text'

arr = url.split('/')
uri=''
for i in arr[:-1]:
  uri+=i + "/"

visited = []

def check_url(link):
  if ('.htm' in link) and not (link in visited):
    return True
  else:
    return False

# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def crawling(html):
  base = True
  page = requests.get(uri + '/' + html)
  soup = BeautifulSoup(page.content, 'html.parser')
  for l in soup.find_all('a'):
    link = l.get('href')
    link = link.split('/')[-1]
    if check_url(link):
      visited.append(link)
      loot = crawling(link)
      if loot:
        return loot
    base = False 
  for form in soup.find_all('form'):
    link = form.get('action').split('/')[-1]
    if check_url(link):
      visited.append(link)
      loot = crawling(link)
      if loot:
        return loot
    base = False
  for iframe in soup.find_all('iframe'):
    link = iframe.get('src')
    if check_url(link):
      visited.append(link)
      loot = crawling(link)
      if loot:
        return loot
    base = False
  if base:
    # https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

visited.append(arr[-1])
text = crawling(arr[-1])
loot = re.findall(r'LOOT:(.*)\r', text)[0]

with open('output.txt', 'w') as fout:
    fout.write(loot)
