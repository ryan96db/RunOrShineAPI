import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Items

items = [
    {'name': "Tank Top",
     'description': "XXX"},
    {'name': "Shorts",
     'description': "XXX"},
    {'name': "Short-Sleeve T-Shirt",
     'description': "XXX"}
    





]
@app.route('/', methods=['GET'])
def home():
    return "<h1>RunOrShineAPI</h1><p>Prototype</p>"

# A route to return running gear.

@app.route('/api/v1/resources/items/all', methods=['GET'])
def api_all():
    return jsonify(items)

app.run()
