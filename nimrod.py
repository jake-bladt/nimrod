from bs4 import BeautifulSoup
from urllib.request import urlopen

# urllib.urlretrieve("http://images2.fanpop.com/images/photos/6900000/cute-kitten-cats-6987468-500-431.jpg", "/mounted/nimrod/kitten.jpg")

r = urlopen("http://www.google.com").read()
soup = BeautifulSoup(r)

print(soup.prettify()[0:1000])
