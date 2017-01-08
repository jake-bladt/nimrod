import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse

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
    self.target = target;

  def grab_image(self, url):
    filename = urlparse(url).path;
    print(self.target + filename)

# urllib.urlretrieve("http://images2.fanpop.com/images/photos/6900000/cute-kitten-cats-6987468-500-431.jpg", "/mounted/nimrod/kitten.jpg")

url = sys.argv[1];
depth = sys.argv[2];
target = sys.argv[3];

pa = PageAssets().parse_page(url, depth)
print(pa.page_title)
for link in pa.links:
  print(link)

for img in pa.images:
  print(img)
  grabber = ImageGrabber(target)
  grabber.grab_image(img)


