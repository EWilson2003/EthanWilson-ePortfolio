import os
MONGO_URI=os.getenv("MONGO_URI","mongodb://localhost:27017")
DB_NAME=os.getenv("MONGO_DB","AAC")
COLLECTION_NAME=os.getenv("MONGO_COLLECTION","animals")
