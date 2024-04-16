from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)

@app.route('/process-data',methods=['POST'])
def process_data():
    data_input = request.json['plaintext']
    key_input = request.json['key']
    data = main.run(data_input,key_input)
    data_to_send = ''.join(data)
    return jsonify(data_to_send)

if __name__ == '__main__':
    app.run(debug=True)