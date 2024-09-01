import requests
from dotenv import load_dotenv
import os

# URL of the API endpoint

load_dotenv()

api_key = os.getenv("HYPIXEL_API_KEY")

uuid = input("Input the UUID (with dashes!) of the player you want to search: ")

base_endpoint_url = "https://api.hypixel.net/v2/player"
params = {
    'uuid': uuid,
    'key': api_key
}

# Send a GET request
response = requests.get(base_endpoint_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    print("Received 200 status code, parsing JSON...")
    # Parse the JSON response
    data = response.json()

    # Check for a specific key and its value
    key_to_check = "ranksGiven"
    if key_to_check in data:
        value = data[key_to_check]
        print(f"The value of '{key_to_check}' is: {value}")
    else:
        print(f"'{key_to_check}' not found in the JSON response.")
else:
    print(f"Request failed with status code: {response.status_code}")
