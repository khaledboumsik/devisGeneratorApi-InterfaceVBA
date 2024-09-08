from inputConstructor import InputConstructor
#from wordGeneratorPrompt import WordGenerator
from wordGeneratorJson import WordGeneratorJson
from jsonConstructor import InformationProcessorJson
import os
from flask import Flask, request, jsonify

#inputer=InputConstructor()
#wordGenerator=WordGenerator("GeneratedFiles",inputer)

app = Flask(__name__)
@app.route("/process-json", methods=['POST'])
def process_json():
    # Get the JSON data from the request
    data = request.get_json()
    inputer2=InformationProcessorJson("information.json")
    WordGenerator=WordGeneratorJson("GeneratedFiles",inputer2,data)
    print(data)
    if not data:
        return jsonify({"error": "No data provided"}), 400

    client_name = data.get('Client', {}).get('Name')
    products = data.get('Products', [])

    # Example response with processed data
    response = {
        "message": "Data processed successfully",
        "client_name": client_name,
        "number_of_products": len(products)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
