from flask import Blueprint, request, redirect, url_for, render_template
from models.allergen_model import get_all_allergens
from models.flavor_model import get_flavors_by_allergens, get_all_flavors

allergen_bp = Blueprint('allergens', __name__)

@allergen_bp.route('/add_allergen', methods=['POST'])
def add_allergen_route():
    allergen_name = request.form.get('allergen_name')
    add_allergen(allergen_name)
    return redirect(url_for('flavors.index'))

@allergen_bp.route('/', methods=['GET'])
def index():
    allergens = get_all_allergens()  
    selected_allergens = request.args.getlist('allergen')  
    flavors = get_flavors_by_allergens(selected_allergens) if selected_allergens else get_all_flavors()
    return render_template('index.html', flavors=flavors, allergens=allergens)
