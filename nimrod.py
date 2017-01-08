import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse
from datetime import datetime

class PageAssets:
  def parse_page(self, url, depth):
    self.url = url

    r = urlopen(url).read()
    soup = BeautifulSoup(r)
    self.page_title = soup.title.string

    all_anchors = soup.find_all('a')
    self.links = map((lambda a: a.get('href')), all_anchors)

    all_images = soup.find_all('img')
    self.images = map((lambda i: i.get('src')), all_images)

    return self

class ImageGrabber:
  def __init__(self, target):
    self.target = target + datetime.now().strftime('%Y%m%d%H%M%s') + '/';

  def grab_image(self, url):
    path = urlparse(url).path;
    filename = path.split('/')[-1]
    print('Copying ' + url + ' to ' + self.target + filename)
    urlretrieve(url, self.target + filename)




url = sys.argv[1];
depth = sys.argv[2];
target = sys.argv[3];

pa = PageAssets().parse_page(url, depth)
print(pa.page_title)
for link in pa.links:
  print(link)

grabber = ImageGrabber(target)
for img in pa.images:
  grabber.grab_image(img)
