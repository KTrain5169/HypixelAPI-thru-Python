import requests
import textwrap
import json
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

api_key = os.getenv("HYPIXEL_API_KEY")

def json_key_search(data, key):
    if key in data:
        return data[key]
    for k, v in data.items():
        if isinstance(v, dict):
            result = json_key_search(v, key)
            if result is not None:
                return result
    return None

uuid = input("Input the UUID (with dashes!) of the player you want to search: ")
endpoint = str(input("What endpoint would you like to search? "))

url = f"https://api.hypixel.net/v2/{endpoint}"

params = {
    'uuid': uuid,
    'key': api_key
}

# Send a GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    print("Received 200 status code, parsing JSON...")
    # Parse the JSON response
    data = response.json()

    key_to_check = str(input("What key are you looking for? "))

    if key_to_check.lower() == "all" or key_to_check.lower() == "all of them":
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"Hypixel_API_{endpoint}_endpoint_{uuid}_at_{current_time}.json"

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"JSON file saved! Find it at {filename}")
    
    else:
        # Check for a specific object, key, and its value
        result = json_key_search(data, key_to_check)

        if result is not None:
            print(f"The value of '{key_to_check}' is {result}")
            with open("output.txt", "a") as f:
                f.write('\n')
                f.write('--BEGIN COPY FROM HERE--\n')
                f.write(f"UUID: {uuid}, endpoint: {endpoint}, checked key {key_to_check}\n")
                wrap_text = f"Result: {result}"
                f.write(textwrap.fill(f"Result: {result}"))
                f.write('\n--STOP COPYING HERE--')
                f.write("\n")
        else:
            print(f"Couldn't find '{key_to_check}' in the JSON response.")
else:
    print(f"Request failed with status code: {response.status_code}")
