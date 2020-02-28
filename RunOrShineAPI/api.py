import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Items

items = [
    {'id': 1,
     'name': "Tank Top",
     'description': "XXX"},
    {'id': 2,
     'name': "Shorts",
     'description': "XXX"},
    {'id': 3,
     'name': "Short-Sleeve T-Shirt",
     'description': "XXX"}
    





]
@app.route('/', methods=['GET'])
def home():
    return "<h1>RunOrShineAPI</h1><p>Prototype</p>"

# A route to return running gear.

@app.route('/api/v1/resources/items/all', methods=['GET'])
def api_all():
    return jsonify(items)

#Adds ability to filter items

@app.route('/api/v1/resources/items', methods=['GET'])

def api_id():
    # Check if ID was provided as part of URL.
    # Assigns ID to variable if ID is provided.
    # Displays erros in browser if no ID is provided.

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID field provided. Please specify ID."

    # Empty list for item results
    results = []

    # Loop through data and match results that fit the ID that was requested.

    for item in items:
        if item['id'] == id:
            results.append(item)

    return jsonify(results)


app.run()
