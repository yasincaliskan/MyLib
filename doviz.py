import requests

url = "http://data.fixer.io/api/latest?access_key=6137d7b1bfd317793997f93f83eb4281"
response = requests.get(url)
json_data = response.json()
birim = input("Hangi birime?:")
miktar = int(input("Ne kadar?:"))

print(str(miktar) + " EUR = " + str(json_data["rates"][birim]*miktar) + " " + birim)