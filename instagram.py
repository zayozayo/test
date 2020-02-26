import sys
import requests
from bs4 import BeautifulSoup

tag=requests.get(sys.argv[-1])
url = "https://www.instagram.com/explore/tags/" + str(tag)
source_code = requests.get(url)
plain_text = source_code.text

soup = BeautifulSoup(plain_text,"lxml")
tagname = tag
# Extract total number of posts in this hashtag
nposts = soup.find('span', {'class': 'g47SY'}).text
 
print 'Number of posts is ' + nposts
