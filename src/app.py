from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)
CORS(app)

@app.route('/process-data',methods=['POST'])
def process_data():
    data_input = request.json['plaintext']
    key_input = request.json['key']
    data = main.run(data_input,key_input)
    result_string = ''
    for sublist in data:
        for item in sublist:
            for element in item:
                result_string += element
    return jsonify(result_string)

if __name__ == '__main__':
    app.run(debug=True)