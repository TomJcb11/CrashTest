import requests

api_url = 'https://api.api-ninjas.com/v1/population?country=Algeria'
response = requests.get(api_url, headers={'X-Api-Key': 'QZ2s4vD9a9igD/xja3Q1FQ==xgkKqgn6jWfRBpYW'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)