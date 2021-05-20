import requests
import json
import flask


player=json.dumps({"id": 10, "player_name": "Amit"})
r =requests.post('http://127.0.0.1:8080/addplayer',json=player)
print(r.content)
print(r.status_code)
