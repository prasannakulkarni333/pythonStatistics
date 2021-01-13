#!/usr/local/bin/python3
# !python3

# Source - https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask


import flask
from flask import request
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

customers = [
    {'id': 1,
     'emailAdd': 'test@flask.com',
     'endDate': '10-10-2020'
     },
    {'id': 2,
     'emailAdd': 'test@flask.com',
     'endDate': '10-12-2020'
     }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask API Example</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# TODO: Present in the database flask API APp


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/persons/customers/all', methods=['GET'])
def api_all():
    return jsonify(customers)


@app.route('/api/v1/persons/customers', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for customer in customers:
        if customer['id'] == id:
            results.append(customer)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
