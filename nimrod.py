import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen

class PageAssets:
  def parse_page(self, url, depth):
    self.url = url

    r = urlopen(url).read()
    soup = BeautifulSoup(r)
    self.page_title = soup.title.string

    all_anchors = soup.find_all('a')
    self.links = map((lambda a: a.href), all_anchors)

    all_images = soup.find_all('img')
    self.images = map((lambda i: i.src), all_images)

    return self

# urllib.urlretrieve("http://images2.fanpop.com/images/photos/6900000/cute-kitten-cats-6987468-500-431.jpg", "/mounted/nimrod/kitten.jpg")

url = sys.argv[1];
depth = sys.argv[2];

pa = PageAssets().parse_page(url, depth)
print(pa.page_title)
