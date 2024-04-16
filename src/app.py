from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)

@app.route('/process-data',methods=['POST'])
def process_data():
    data_input = request.json['text']
    key_input = request.json['key']
    data = main.run(data_input)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)