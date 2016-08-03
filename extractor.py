import requests
import re
from bs4 import BeautifulSoup

def parse_page(title, type):
  print('extracting '+ title)
  soup = to_soup(format_url(title, type))
  section = soup.find_all('div', class_='page-content')
  rel_data = re.findall('<hr/>.*', str(section))
  if not rel_data:
    print('Cannot find hr')
    print(to_soup_encoded(format_url(title, type)))
    return []
  result = find_folders(BeautifulSoup(rel_data[0]), title.replace(' ', ''))
  if not len(result):
    result = find_folders(section[0], title.replace(' ', ''))
  return result

def parse_subpage(url):
  soup = to_soup(url)
  return find_folders(soup)

def find_folders(data, title=''):
  print('here')
  folders = data.find_all('div', class_='folder')
  if folders:
    print('extracting folders')
    result = []
    for folder in folders:
      result += e(folder, extract_trope)
    return result
  else:
    print('here2')
    print(data)
    def cb(uls):
      return test_sub(uls, title.replace(' ', ''))
    result = e(data, cb)
    return result

def e(text, cb):
  print('here3')
  print(text)
  uls = text.find_all('ul', recursive = False)
  print(uls)
  if(not uls):
    print('no links after hr')
    return []
  return cb(uls)

def extract_trope(uls):
  #remove ymmv?
  holder = []
  for ul in uls:
    for entry in ul:
      #only first layer
      trope = entry.find('a')
      if trope:
        href = str(trope['href']).lower()
        holder.append(href)
  return holder

def test_sub(uls, title):
  first_link = str(uls[0].find('a')['href']).lower()
  if title not in first_link:
    return extract_trope(uls)
  else:
    print('extracting subpages')
    result = []
    for ul in uls:
      for entry in ul:
        trope = entry.find('a')
        if trope:
          href = str(trope['href']).lower()
          result += parse_subpage(href)
    return result

def format_url(title, type):
  type = type.replace(' ', '')
  title = title.replace(' ', '')
  return 'http://tvtropes.org/pmwiki/pmwiki.php/' + type + '/' + title

def to_soup(url):
  r = requests.get(url)
  return BeautifulSoup(r.content)

def to_soup_encoded(url):
  r = requests.get(url)
  return BeautifulSoup(r.content, 'html5lib')