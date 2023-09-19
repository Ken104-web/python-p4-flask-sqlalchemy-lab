#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if animal:
        body = f'''
            <ul>ID: {animal.id}</ul>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>
            <ul>Zookeeper: {animal.zookeeper.name}</ul>
            <ul>Enclosure: {animal.enclosure.environment}</ul>
        '''
    else:
        body = '<h1>404 animal not found</h1>'
    responce = make_response(body)
    return responce

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper= Zookeeper.query.filter(Zookeeper.id == id).first()
    if zookeeper:
        body = f'''
        <ul>ID: {zookeeper.id}</ul>
        <ul>Name: {zookeeper.name}</ul>
        <ul>Birthday: {zookeeper.birthday}</ul>'''
    for animal in zookeeper.animals:
            body += f'<ul>Animal: {animal.name}</ul>'
        
            body += '</ul></ul>'
    else:
        body = '<h1>404 zookeeper not found</h1>'
    
    responce = make_response(body)
    return responce

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
