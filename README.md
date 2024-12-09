# Ice Cream Parlor

A simple web application for an Ice Cream Parlor where users can browse ice cream flavors, add them to a shopping cart, and apply filters for seasonal flavors and allergens.

## Features

- **Browse Flavors**: View a list of ice cream flavors with descriptions.
- **Search**: Search for specific flavors.
- **Filter**: Filter flavors by seasonality (seasonal or non-seasonal) and allergens (e.g., Milk, Peanuts).
- **Shopping Cart**: Add flavors to your cart, view the cart, and remove items.
- **Clear Cart**: Remove all items from the cart.

## Technologies

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ice-cream-parlor.git
   cd ice-cream-parlor

2. Install dependencies:
  
    pip install -r requirements.txt

3. Initialize the database:

    from app import initialize_database
    initialize_database()

4. Run the application:

    python app.py

5. The app will be available at http://127.0.0.1:5000/

## File Structure

ice-cream-parlor/
    app.py # Main application file

    requirements.txt # Project dependencies 

   - **Models**/ # Database setup and models

        database.py # Database configuration
        cart_model.py # Cart schema 
        flavor_model.py #flavor Schema 

    - **controllers**/ # Logic for handling routes and requests

        flavor_controller.py # Ice cream flavor actions 
        cart_controller.py # Cart actions 
        allergen_controller.py # Allergen-related actions 

    - **static**/ # Static files (CSS, JS) 

        style.css # Styles for the app 
        index.js # JavaScript for interactivity

    - **templates**/ # HTML files for rendering 

        index.html # Home page showing flavors 
        cart.html # Cart page 

    README.md # Project documentation


## Running the Application with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t ice_cream_parlor .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 ice_cream_parlor
   ```

3. **Access the application**:
   Open your browser and navigate to `http://localhost:5000` to use the application.
