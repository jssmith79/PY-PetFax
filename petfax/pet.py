from flask import ( Flask, Blueprint, render_template, request, redirect, url_for )
import json

#index route

bp = Blueprint('pet', __name__, url_prefix="/pets")
pets = json.load(open('pets.json'))

@bp.route('/')
def index():
    return render_template("pets/index.html", pets=pets)

#show route

@bp.route('/<int:pet_id>')
def show(pet_id):
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)   
    if pet: 
        return render_template("pets/show.html", pet=pet)
    else:
        return "pet not found."

# add or create route

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        return redirect(url_for('pets/index.html'))
    else:
        return render_template("pets/create.html")

@bp.route('/<int:pet_id>/return')
def return_to_index(pet_id):
    return redirect(url_for('pets/index.html'))