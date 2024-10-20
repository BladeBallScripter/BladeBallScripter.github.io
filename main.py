from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple route
@app.route('/hello')
def home():
    return "Welcome to the simple API!"

# Example of a GET request
@app.route('/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Software Developer'
    }
    return jsonify(data)

# Example of a POST request
@app.route('/data', methods=['POST'])
def post_data():
    new_data = request.json
    response = {
        'message': 'Data received!',
        'received_data': new_data
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
