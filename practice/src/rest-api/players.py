import flask
from flask import request,jsonify

players = [
{
'id':0,
'player_name':'Sachin'
},
{
'id':1,
'player_name':'Ricky'
},
{
'id':2,
'player_name':'Virat'
},
{
'id':3,
'player_name':'Kevin'
}
]

app=flask.Flask(__name__)
app.config["DEBUG"]=True



@app.route('/all', methods=['GET'])
def getAllPlayer():
    return jsonify(players)


@app.route('/player',methods=['GET'])
def getBook():
    player_id=0
    if 'id' in request.args:
        player_id=int(request.args['id'])
    else:
        return jsonify("id parameter not sent in request")

    results=[]

    for player in players:
        print(player,player_id)
        if player['id']==player_id:
            return player

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
