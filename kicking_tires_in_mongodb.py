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

    cities_df = pd.read_csv('cities.csv', low_memory = False)
    cities_dict = cities_df.to_dict()
    # Reducing dict size for performance purposes
    cities_dict = dict(list(cities_dict.items())[:10])
    # Making sure all keys and values are strings to avoid InvalidDocument error
    cities_dict = {str(k): str(v) for k,v in cities_dict.items()}
    return cities_dict

def add_cities_to_db(db: Database, cities_data: dict):
    """
    A function to insert city data into db
    Arguments: db -> collection object, cities_data -> dictionary
    """

    try:
        db.cities.insert_one(cities_data)
        print('Inserted data into database successfully :)')
    
    except(errors.ServerSelectionTimeoutError):
        print("Oops! insert took too long due to a ServerSelectionTimeoutError")
    
def fetch_first_record(db: Database):
    """
    A function to fetch the first record in our data to test that data is inserted correctly
    Arguments: db -> collection object
    """

    try:
        return db.cities.find_one()

    except(errors.ServerSelectionTimeoutError):
        print("Oops! looks like your query took too long due to a ServerSelectionTimeoutError")

def get_db():
    """
    A function to create the database on a MongoDB cluster
    """
    
    try:
        client = MongoClient("mongodb+srv://Ashmawy:{}@cluster0.ta7o8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(atlas_creds['value'][1]))
        db = client.cities

        print('DB created on the cluster successfully :)')

    except(errors.ServerSelectionTimeoutError):
        print("Oops! connection timed out")

    return db

if __name__ == "__main__":
    db = get_db()
    add_cities_to_db(db, get_clean_city_data())
    print(fetch_first_record(db))
