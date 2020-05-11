import couchdb
import csv
from objects import CovidCase
from neo4j_core import add_covid_data
import asyncio
import json
import os

couch = couchdb.Server('http://admin:password@localhost:5984/')

db = couch['covid']

def add_initial_data():
    with open(r"data\us-counties.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            print ("added record from " + line[2])
            obj = CovidCase(line[0], line[1], line[2], line[3], int(line[4]), int(line[5]))
            db.save(obj.__dict__)
            print ("adding to neo4j")
            asyncio.run(add_covid_data(str(line[2]), str(line[1]),str(line[0]), int(line[4]), int(line[5])))

def insert(obj: CovidCase):
    db.save(obj.__dict__)

def get_death_count():
    item = db.view('cases_info/deaths')
    return item

add_initial_data()