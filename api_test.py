import requests

def search_profiles(location):
    payload = {"latitude": location["lat"], "longitude": location["lng"]}  
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with real token
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    response = requests.post("https://api.hinge.com/v1/search", json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch profiles", "details": response.text}
