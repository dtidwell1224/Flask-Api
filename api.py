#!/bin/python
 
from flask import Flask
from flask_restful import Api, Resource, reqparse
 
app = Flask(__name__)
api = Api(app)
 
statearray = [
    {
        "state": "current",
        "inthepool": "yes"
    }
]
 
class STATE(Resource):
    def get(inthepoolstate, state):
        for user in statearray:
            if(state == user["state"]):
                return user, 200
        return "User not found", 404
 
    def post(inthepoolstate, state):
        parser = reqparse.RequestParser()
        parser.add_argument("inthepool")
        args = parser.parse_args()
 
        for user in statearray:
            if(state == user["state"]):
                global statearray
                statearray = [user for user in statearray if user["state"] != state]
 
        user = {
            "state": state,
            "inthepool": args["inthepool"]
        }
        statearray.append(user)
        return user, 201
 
    def put(inthepoolstate, state):
        parser = reqparse.RequestParser()
        parser.add_argument("inthepool")
        args = parser.parse_args()
 
        for user in statearray:
            if(state == user["state"]):
                user["inthepool"] = args["inthepool"]
                return user, 200
        
        user = {
            "state": state,
            "inthepool": args["inthepool"]
        }
        statearray.append(user)
        return user, 201
 
    def delete(inthepoolstate, state):
        global statearray
        statearray = [user for user in statearray if user["state"] != state]
        return "{} is deleted.".format(state), 200
      
api.add_resource(STATE, "/api/<string:state>")
 
#app.run(debug=True)
app.run(port=8080)
