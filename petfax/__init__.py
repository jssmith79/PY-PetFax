from flask import Flask 
from flask_migrate import Migrate
def create_app(): 
    app = Flask(__name__)


#complete later with DB config

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rusty123-@localhost:5432/petfax'
    app.config['SQLALCHEM_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate( app, models.db)
    
    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)


    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    return app
