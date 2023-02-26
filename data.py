
import requests
import json
from requests.exceptions import HTTPError

try:
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    # print("Entire JSON response")
    # print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

question_data = jsonResponse
