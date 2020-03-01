import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True



def dict_factory(cursor, row):
    d = {}
    for indx, colum in enumerate(cursor.description):
        d[colum[0]] = row[indx]
    return d



@app.route('/', methods=['GET'])
def home():
    return "<h1>RunOrShineAPI</h1><p>Prototype</p>"

# A route to return running gear.

@app.route('/api/v1/resources/items/all', methods=['GET'])

def api_all():
    conect = sqlite3.connect('items.db')
    conect.row_factory = dict_factory
    curs = conect.cursor()
    all_items = curs.execute('SELECT * FROM items;').fetchall()

    con = sqlite3.connect('weatherIcons.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    all_icons = cur.execute('SELECT * FROM weatherIcons;').fetchall()

    everything = all_items + all_icons

    return jsonify(everything)


@app.errorhandler(404)
def page_not_found(er):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


#Adds ability to filter items by id

@app.route('/api/v1/resources/items', methods=['GET'])
def api_filter():
    query_params = request.args

    id = query_params.get('id')

    query = "SELECT * FROM items WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if not (id):
        return page_not_found(404)

    query = query[:-4] + ';'

    conect = sqlite3.connect('items.db')
    conect.row_factory = dict_factory
    curs = conect.cursor()

    results = curs.execute(query, to_filter).fetchall()

    return jsonify(results)

#Adds ability to filter weather icons by id
@app.route('/api/v1/resources/weatherIcons', methods=['GET'])
def icon_filter():
    query_params = request.args

    id = query_params.get('id')

    query = "SELECT * FROM weatherIcons WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if not (id):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('weatherIcons.db')
    conn.row_factory = dict_factory
    curso = conn.cursor()

    results = curso.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
