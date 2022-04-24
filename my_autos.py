from gridfs import Database
from matplotlib.collections import Collection
from pymongo import MongoClient
from pymongo import errors
import pandas as pd
import pprint

atlas_creds = pd.read_csv('mongo_atlas_creds.csv')

def get_clean_autos_data():
    """
    A function to clean autos data :)
    Returns a clean dictionary of city data.
    """

    # Reducing dataframe size for performance purposes
    autos_df = pd.read_csv('autos.csv', low_memory = False)
    autos_dict = autos_df.to_dict(orient = 'series')

    """ Note:
        Series orientation when dealing with MongoDB uses least memory,
        and setting low_memory = False reduces memory further """

    autos_dict = {str(k): str(v) for k,v in autos_dict.items()}
    autos_dict = dict(list(autos_dict.items()))
    return autos_dict

def add_autos_to_db(db: Database, autos_data: dict):
    """
    A function to insert city data into db
    Arguments: db -> collection object, cities_data -> dictionary
    """

    try:
        db.autos.insert_one(autos_data)
        print('Inserted data into database successfully :)')
    
    except(errors.ServerSelectionTimeoutError):
        print("Oops! insert took too long due to a ServerSelectionTimeoutError")
    
def fetch_key(db: Database, key_to_be_fetched: str):
    """
    A function to fetch the first record in our data to test that data is inserted correctly
    Arguments: db -> collection object
    """

    try:
        return db.autos.find_one({}, {key_to_be_fetched: 1})

    except(errors.ServerSelectionTimeoutError):
        print("Oops! looks like your query took too long due to a ServerSelectionTimeoutError")

def get_db():
    """
    A function to create the database on a MongoDB cluster
    """
    
    try:
        client = MongoClient("mongodb+srv://Ashmawy:{}@cluster0.ta7o8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(atlas_creds['value'][1]))
        db = client.playing_with_pymongo

        print('DB server accessed with no problems :)')

    except(errors.ServerSelectionTimeoutError):
        print("Oops! connection timed out")

    return db

if __name__ == "__main__":
    db = get_db()
    
    # Only call this function once
    add_autos_to_db(db, get_clean_autos_data())

    pprint.pprint(fetch_key(db, 'rdf-schema#label'))
