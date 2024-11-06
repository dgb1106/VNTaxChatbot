from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import EnvironmentVariables

class DBConnection:
    def __init__(self) -> None:
        client = MongoClient(EnvironmentVariables.mongodbURI, server_api=ServerApi('1'))
        self.db = client["TaxDocuments"]
        self.collection = self.db["Definitions"]
        
    def getResult(self, key):
        query = {"name": {"$regex": key, "$options": "i"}}
        result = self.collection.find_one(query, {"definition": 1, "_id": 0})
        return result;
        

# documents = collection.find()
# for doc in documents:
#     print(doc)

# query = {"name": "Hoạt động thương mại điện tử"}

def main():
    key = input()
    dbConnection = DBConnection()
    result = dbConnection.getResult(key)
    print(result["definition"])
        
if __name__ == "__main__":
    main()

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)