from flask import Blueprint, render_template, redirect, url_for
from models.cart_model import add_to_cart, get_cart_items, clear_cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
def view_cart():
    cart_items = get_cart_items()
    return render_template('cart.html', cart_items=cart_items)

@cart_bp.route('/add_to_cart/<int:flavor_id>', methods=['GET'])
def add_to_cart_route(flavor_id):
    add_to_cart(flavor_id)
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/clear_cart', methods=['GET'])
def clear_cart_route():
    clear_cart()
    return redirect(url_for('cart.view_cart'))
