from gridfs import Database
from matplotlib.collections import Collection
from pymongo import MongoClient
from pymongo import errors
import sys
import pandas as pd

atlas_creds = pd.read_csv('mongo_atlas_creds.csv')

def get_clean_city_data():
    """
    A function to clean city data :)
    Returns a clean dictionary of city data.
    """

    cities_df = pd.read_csv('cities.csv')
    cities_dict = cities_df.to_dict()
    return cities_dict

def add_cities_to_db(db: Database, cities_data: dict):
    """
    A function to insert city data into db
    Arguments: db -> collection object, cities_data -> dictionary
    """

    try:
        db.cities.insert_many(cities_data)
        print('Inserted data into database successfully :)')
    
    except(errors.ServerSelectionTimeoutError):
        print("Oops! insert took too long")
    
def fetch_first_row(db: Database):
    """
    A function to print the first row in our data to test that data is correct
    Arguments: db -> collection object
    """

    try:
        return db.cities.find_one()

    except(errors.ServerSelectionTimeoutError):
        print("Oops! looks like your query took too long")

def get_db():
    """
    A function to create the database on a MongoDB cluster
    """
    
    try:
        client = MongoClient("mongodb+srv://Ashmawy:{}@cluster0.ta7o8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(atlas_creds['value'][1]))
        db = client.cities

        print('Connected Ok :)')

    except(errors.ServerSelectionTimeoutError):
        print("Oops! connection timed out")

    return db

if __name__ == "__main__":
    db = get_db()
    add_cities_to_db(db, get_clean_city_data())
    fetch_first_row(db)
