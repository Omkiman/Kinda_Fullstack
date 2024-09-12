from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


categories =[
    {"catid":1,"desc":"meat"},
    {"catid":2,"desc":"dairy"},
    {"catid":3,"desc":"bakery"},
    {"catid":3,"desc":"Good stuff"}]


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/categories')
def get_categories():
    return jsonify(categories)



@app.route('/test/<id>')
def test(id):
    print(f"Selected category ID: {id}")
    return jsonify({"message": f"Category {id} received"})  # Return a response

if __name__ == '__main__':
    app.run(debug=True)