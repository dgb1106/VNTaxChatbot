from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://heyiamdgb:Gb11062005@vntaxchatbot.qqw1j.mongodb.net/?retryWrites=true&w=majority&appName=VNTaxChatbot"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["TaxDocuments"]
collection = db["Definitions"]

# documents = collection.find()
# for doc in documents:
#     print(doc)

# query = {"name": "Hoạt động thương mại điện tử"}
query = {"name": {"$regex": "Hoạt động", "$options": "i"}}
result = collection.find(query)

for res in result:
    print(res)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)