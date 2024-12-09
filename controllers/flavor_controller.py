from flask import Blueprint, render_template
from models.flavor_model import get_all_flavors

flavor_bp = Blueprint('flavors', __name__)

@flavor_bp.route('/')
def index():
    flavors = get_all_flavors()
    return render_template('index.html', flavors=flavors)
