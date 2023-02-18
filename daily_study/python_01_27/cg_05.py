from urllib.request import	urlretrieve
from urllib.request import	urlopen
from bs4 import	BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
home_image = bs.find('img', {'class':'pagelayer-img'})
img_location = home_image['src']
print(img_location)
urlretrieve(img_location,'logo.jpg')