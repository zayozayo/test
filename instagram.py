import sys
import requests
from bs4 import BeautifulSoup

tag=sys.argv[-1]
url = "https://www.instagram.com/explore/tags/" + str(tag)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}
source_code = requests.get(url, headers=headers)
plain_text = source_code.text

soup = BeautifulSoup(plain_text, "html.parser")
# Extract total number of posts in this hashtag
nposts = soup.find('span', {'class': 'g47SY'}).text
 
print 'Number of posts is ' + nposts
