import requests

response = requests.get("http://localhost:23512/pdf/Odisea")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson)

response = requests.get("http://localhost:23512/audio/Don Quijote")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson)

