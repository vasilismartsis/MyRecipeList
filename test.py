import requests
params = {"words": 10, "paragraphs": 1, "format": "json"}

response = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Doublelift/",
                        params="api_key=RGAPI-73aaf59d-0ba3-4425-b5d4-f169612f844c")

anotherVariable = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/" + response.json()["puuid"],
                               params="api_key=RGAPI-73aaf59d-0ba3-4425-b5d4-f169612f844c")

# print(type(response.json()))
# print(response.json())
print("hhaahahahahaha")
print(anotherVariable)
