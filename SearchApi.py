import requests
import json

# The API endpoint
url = "https://theta.boomconcole.com/api/search-api-clean?search=nischal&type=the_first_name&composition=the_user"

# A GET request to the API
response = requests.get(url)
response_json = response.json()
print(response_json)
with open("./meow.txt", "w", encoding="utf-8") as f:
    quality_content = json.dumps(response_json[0])
    f.write(quality_content)
# Print the response
