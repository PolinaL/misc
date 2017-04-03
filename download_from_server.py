import re
import urllib.request
import pycurl

url = "http://littleheron.iwr.uni-heidelberg.de:8081/"
pattern = '(?<=a href=").*py(?=")'
response = urllib.request.urlopen(url).read()


for filename in re.findall(pattern, response.decode("utf-8")):
    print(filename)
    fp = open(filename, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url+filename)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()