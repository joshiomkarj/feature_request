#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import configparser

config = configparser.ConfigParser()
config.read("../product.ini")
engine = config['DATABASE']['engine']

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'
    client_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    client_name = sqlalchemy.Column(sqlalchemy.String(1000))


class Product_Area(Base):
    __tablename__ = 'product_areas'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    product_area_name = sqlalchemy.Column(sqlalchemy.String(1000))


class Feature(Base):
    __tablename__ = 'features'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.Text)
    description = sqlalchemy.Column(sqlalchemy.Text)
    client_id = sqlalchemy.Column(sqlalchemy.Integer)
    client_priority = sqlalchemy.Column(sqlalchemy.Integer)
    target_date = sqlalchemy.Column(sqlalchemy.Date)
    product_area_id = sqlalchemy.Column(sqlalchemy.Integer)

engine = sqlalchemy.create_engine(engine)

Base.metadata.create_all(engine)
