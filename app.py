from flask import Flask
from routes.contestants import contestants_bp
from routes.husband_call import husband_call_bp
from extensions import mongo, mp
from secret import db_pw

def create_app():
    app = Flask(__name__)
    
    ## MONGO SETUP ##
    mongo_uri = f"mongodb+srv://buiwilliam30:{db_pw}@cluster0.5ujtnbw.mongodb.net/database1?retryWrites=true&w=majority"
    app.config["MONGO_URI"] = mongo_uri
    mongo.init_app(app)
    mp.init_app(app)

    ## ROUTES ##
    app.register_blueprint(contestants_bp, url_prefix='/contestants')
    app.register_blueprint(husband_call_bp, url_prefix='/husbandCall')

    return app
