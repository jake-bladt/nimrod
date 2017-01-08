from bs4 import BeautifulSoup
import urllib
# urllib.urlretrieve("http://images2.fanpop.com/images/photos/6900000/cute-kitten-cats-6987468-500-431.jpg", "/mounted/nimrod/kitten.jpg")

r = urllib.open("http://www.google.com").read()
soup = BeautifulSoup(r)

print(soup.prettify()[0:1000])
