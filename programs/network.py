import urllib.request

url = "http://example.com"
response = urllib.request.urlopen(url)
data = response.read()
print(len(data))
