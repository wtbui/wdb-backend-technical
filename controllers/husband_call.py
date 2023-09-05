from extensions import mongo
from models.contestant import ContestantSchema
from flask import jsonify

def get_score(name):
    try:
        contestant = mongo.db.contestants.find_one({"contestantName": name})

        if not contestant:
            return "Contestant not registered", 406

        if contestant['vocalRange'] < contestant['location']:
            return "Contestant vocal range is less than location", 406

        result = { "score": None }
        if contestant['vocalRange'] == contestant['location']:
            result['score'] = contestant['vocalRange']
        else:
            result['score'] = abs(contestant['vocalRange'] - contestant['location'])

        return jsonify(result)
    
    except:
        return 500
    
