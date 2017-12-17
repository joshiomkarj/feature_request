#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request
from models import Base, Client, Product_Area, Feature, engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

app = Flask(__name__)


def get_dict(row):
    record_dict = dict()
    for column in row.__table__.columns:
        record_dict[column.name] = str(getattr(row, column.name))
    return record_dict


@app.route('/')
def index():
    return "This is the endpoint to feature db"

@app.route('/features', methods=['GET'])
def get_features():
    records = session.query(Feature).all()
    response = [get_dict(record) for record in records]
    return jsonify(response)

@app.route('/features', methods=['POST'])
def create_feature():
    if not request.json:
        abort(400)
    feature = Feature(title=request.json['title'],
                      description=request.json['description'],
                      client_id=request.json['client_id'],
                      client_priority=request.json['client_priority'],
                      target_date=request.json['target_date'],
                      product_area_id=request.json['product_area_id'])

    session.add(feature)
    session.commit()
    return jsonify({'message': 'Added feature'}), 201


if __name__ == '__main__':
    app.run(debug=True)