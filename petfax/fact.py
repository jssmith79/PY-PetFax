from flask import ( Blueprint, render_template, request, redirect ) 
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new():
    return render_template('facts/new.html')


#index route

@bp.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()
        return redirect('/facts')
    
    elif request.method == 'GET':
        results = models.Fact.query.all()
        for result in results:
            print(result.fact_id)
        return render_template('facts/index.html', facts=results)



#return to index route

    @bp.route('/<int:pet_id>/return')
    def return_to_index(pet_id):
        return redirect(url_for('fact.index'))


 
