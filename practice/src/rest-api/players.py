import flask
from flask import request,jsonify
import json


players = [
]

app=flask.Flask(__name__)
app.config["DEBUG"]=True

def readPlayers():
    try:
        f1=open('../../resources/players.json','r')
        players=json.load(f1)
        f1.close()
        return players
    except:
        return ("Error reading from file")
        f1.close()

def addPlayers(data):
    players=[]
    try:
        players=readPlayers()
        players.append(data)
    except:
        print("Error reading from file")

    try:
        f2=open('../../resources/players.json','w')
        json.dump(players,f2)
        f2.close()
        return ("Player added")
    except:
        f2.close()
        return ("Player couldnt be added")

@app.route('/all', methods=['GET'])
def getAllPlayer():
    return jsonify(readPlayers())


@app.route('/player',methods=['GET'])
def getPlayer():
    player_id=0
    players=readPlayers()
    if 'id' in request.args:
        player_id=int(request.args['id'])
    else:
        return jsonify("id parameter not sent in request")

    results=[]

    for player in players:
        print(player,player_id)
        if player['id']==player_id:
            return player

@app.route('/addplayer',methods=['POST'])
def addPlayer():
    data=request.json
    return jsonify(addPlayers(data))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run(port=8080)
