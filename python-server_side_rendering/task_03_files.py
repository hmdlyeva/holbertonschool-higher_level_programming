from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    file_name = "items.json"
    items = read_json(file_name)
    return render_template('items.html', items=items)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        products = [product for product in products if str(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products)

def read_json(file_path):
    try:
        return pd.read_json(file_path).to_dict(orient='records')
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    try:
        return pd.read_csv(file_path).to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True, port=5000)
