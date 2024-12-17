import requests

def json_key_search(data, key):
    if key in data:
        return data[key]
    for k, v in data.items():
        if isinstance(v, dict):
            result = json_key_search(v, key)
            if result is not None:
                return result
    return None

productID = str(input("Enter the ID of the item: "))

url = f"https://api.hypixel.net/v2/skyblock/bazaar"
response = requests.get(url)

if response.status_code == "200":
    print("Received HTTP 200 code, parsing JSON...")
    data = response.json()

    result = json_key_search(data, "productID")

    if result == productID:
        json_key_search(data, productID)