
import re
import sys
import requests
from bs4 import BeautifulSoup

url = ''
if len(sys.argv) > 1:
  url = sys.argv[1]
else :
  sys.exit('Error: Please enter a URL')

r = requests.get(url)

print('Download about to start')

soup = BeautifulSoup(r.content, 'html.parser')
result = ''
for val in soup.findAll("script"):
  if(re.search('props', str(val))) is not None:
    result = str(val)


result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url =  result_mp4 + "mp4"

print("Downloading video from ........ " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1][0:21] +".mp4"


print("Storing video in ....... " + file_name)

r = requests.get(mp4_url)

with open (file_name, 'wb') as f:
  f.write(r.content)

print('Download Process finished')