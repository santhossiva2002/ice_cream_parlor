
from flask import Flask
from models.database import initialize_database
from controllers.flavor_controller import flavor_bp
from controllers.cart_controller import cart_bp
from controllers.allergen_conroller import allergen_bp

app = Flask(__name__)


initialize_database()


app.register_blueprint(flavor_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(allergen_bp)

if __name__ == '__main__':
    app.run(debug=True)
