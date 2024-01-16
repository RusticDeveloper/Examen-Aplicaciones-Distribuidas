# importaciones
from flask import Flask,jsonify,abort
import requests
# instancia api
app=Flask(__name__)
# obtencion de personajes
resp_personajes = requests.get('https://rickandmortyapi.com/api/character').json()

# print(resp_personajes['results'])



@app.route('/')
def get_character():
    return "<h1>Examen Aplicaciones distribuidas -creacion api</h1>"

@app.route('/<persona>')
def get_pizza_by_name(persona):
    try:
        personaje=[character for character in resp_personajes['results'] if persona in character['name'] ]
        return jsonify(personaje)
    except IndexError:    
        abort(404)


if __name__ =='__main__':
    app.run(debug=True)