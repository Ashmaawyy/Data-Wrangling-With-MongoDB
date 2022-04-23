from pymongo import MongoClient
import sys
import pandas as pd
atlas_creds = pd.read_csv('mongo_atlas_creds.csv')

def add_city(db):
    # Changes to this function will be reflected in the output. 
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    try:
        db.cities.insert_one({"name" : "Chicago",
                              "long" : "41.8781 N",
                              "lat" : "87.6298 W"})

    except(TimeoutError):
        print("Oops! insert took too long")
    
def get_city(db):
    try:
        return db.cities.find_one()

    except(TimeoutError):
        print("Oops! looks like your query took too long")

def get_db():
    try:
        client = MongoClient("mongodb+srv://Ashmawy:{}@cluster0.ta7o8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(atlas_creds['value'][1]))
        db = client.cities

        print('Connected Ok :)')
    # 'examples' here is the database name. It will be created if it does not exist.
    except(TimeoutError):
        print("Oops! connection timed out")

    return db

if __name__ == "__main__":
    db = get_db()
    add_city(db)
    print(get_city(db))
