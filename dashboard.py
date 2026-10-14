import os
from animal_shelter import AnimalShelter
shelter=AnimalShelter(os.environ.get("MONGO_URI","mongodb://localhost:27017"))
def rescue_filter(kind):
    if kind=="Water":
        return {"breed":{"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever"]},"sex_upon_outcome":"Intact Female"}
    return {}
def load_rows(kind="All"):
    return shelter.read(rescue_filter(kind))
