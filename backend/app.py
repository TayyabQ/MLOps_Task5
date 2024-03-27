from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('database', 27017)
db = client.my_database
collection = db.my_collection

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    result = collection.insert_one({'name': name, 'email': email})
    if result.acknowledged:
        return jsonify({'message': 'Data inserted successfully'}), 200
    else:
        return jsonify({'message': 'Error inserting data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
