import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
	'desc':'Tableau is mandatory and analytical skills are needed.'
}

r = requests.post(url,json=payload)

print(r.json())
