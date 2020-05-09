import couchdb
import pandas as pd
import csv

couch = couchdb.Server('http://admin:admin@localhost:5984/')
db = couch['covid']

with open("../data/us-counties.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        db.save({'date': line[0], 'county': line[1], 'state': line[2], 'cases': line[4], 'deaths': line[5]})