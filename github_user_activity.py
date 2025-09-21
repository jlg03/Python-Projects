import requests
import json

base_url = "https://api.github.com/users/"

def get_github_info(username):
    url = f"{base_url}{github_username}/events"
    response = requests.get(url)
    print(response)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


github_username = input("Github username: ")
user_info = get_github_info(github_username)

if user_info:
    for dictionaries in user_info:
        activity = dictionaries['type']
        location =dictionaries['repo']['name']
        print(f"Activity {activity} to repo {location}")
