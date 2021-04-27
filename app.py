'''
Created on Apr 25, 2021

@author: sogunfowora
'''

import flask
from flask import request, jsonify
from postcode_functions import format_postcode, validate_postcode

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Api to format and validate UK postcodes</h1> \
            <p>Usage</p> \
            <p>/api/v1/validate?postcode=</p>"
            

@app.route('/api/v1/validate', methods=['GET'])
def api_validate():
    # Check if postcode was provided as part of the URL.
    # If postcode is provided, validate it
    # If no postcode is provided, display an error in the browser.
    if 'postcode' in request.args:
        postcode = request.args['postcode']
    else:
        return "Error: No postcode provided. Please specify postcode."

    postcode_format_result = format_postcode(postcode)
    if postcode_format_result['format_status'] is True:
        validation_result = validate_postcode(postcode_format_result['formatted_postcode'])
        postcode_format_result['validation_status'] = validation_result
        
    return jsonify(postcode_format_result)

app.run()
