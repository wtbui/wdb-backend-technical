from extensions import mongo
from models.contestant import ContestantSchema
from flask import jsonify

def get_contestants(request_args):
    try:
        contestant_collection = mongo.db.contestants.find({})
        contestant_list = list(contestant_collection)
        args_dict = request_args.to_dict()

        if len(args_dict):
            if args_dict['sortedByName'].lower() == 'true':
                contestant_list = sorted(contestant_list, key=lambda contestant: contestant["contestantName"])
        
        result = {"pairs": []}

        for contestant in contestant_list:
            pair = {"contestantName": contestant["contestantName"], 
                    "husbandName": contestant["husbandName"]}
            
            result["pairs"].append(pair)

        return jsonify(result), 200
    
    except:
        return 500

def add_contestant(request_json):
    try:
        contestant_collection = mongo.db.contestants

        err = ContestantSchema().validate(request_json)

        if err:
            return err, 422
        
        contestant_dict = ContestantSchema().load(request_json)
        contestant_collection.insert_one(contestant_dict)
        
        return "OK", 201
    
    except:
        return 500