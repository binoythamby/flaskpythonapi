from flask import Flask , jsonify , request
from flask_restful import  Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if(functionName== "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):

        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code!= 200):
            retJson = {
                "Message": "An error happened",
                "status_code": status_code
            }
            return jsonify(retJson)


        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    pass

class Multply(Resource):
    pass

class Divide(Resource):
    pass


api.add_resource(Add, "/add")




if __name__=="__main_ _":
    app.run(debug = true)









#
#@app.route('/')
#def hello_world():
#    return "Hello Binoy! Get this shit done


    #Get x,y from the posted data
"""
@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():

  dataDict = request.get_json(force=true)
    x = dataDict["x"]
    y = dataDict["y"]
    #Add z=x+y
    z = x+y
    #Prepare a JSON. "z": z
    retJSON = {
        "z":z
    }
    #return jsonify(map_prepared)
    return jsonify(retJSON), 200






def wow_user():

    age = 46/2

    retJson = {

	"Name": "Mbappe",
	"Age": "age",
	"Jerseys": [{
			"jerseyteam": "PSG",
			"jerseynumber": 10
		},
		{
			"jerseyteam": "france",
			"jerseynumber": 7

		}
	]
}

    return jsonify(retJson)"""
