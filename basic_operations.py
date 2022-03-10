from cgi import test
import datetime   # This will be needed later
import os
from pymongo import MongoClient
# Load config from a .env file:


def client():
    MONGODB_URI = "mongodb+srv://stock-adm:c6133452-a4cd-4e0e-99c4-4a20607fb430@cluster0.z7scl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # Connect to your MongoDB cluster:

    return MongoClient(MONGODB_URI)
