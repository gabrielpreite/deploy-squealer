import json

with open("data.json", "r") as f:
    data = json.load(f)
    EMAIL = data["email"]
    PWD = data["password"]
