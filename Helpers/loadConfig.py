import json

with open("config.json") as f:
    config = json.load(f)

DISCORD_TOKEN = config["DISCORD_TOKEN"]
