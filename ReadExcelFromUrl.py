import requests

url = "https://github.com/SheetJS/xlsx-nw-demo/raw/master/test.xlsx"
session = requests.session()
response = session.get(url)
with open("download.xlsx", 'w') as outfile:
    outfile.write(response.content)
a = 1
