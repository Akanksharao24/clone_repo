import requests
url = "http://18.216.110.130:5000/api/messages"
data = {
"message": "AK pak"
}
response = requests.post(url,json=data)
print(response.text)
