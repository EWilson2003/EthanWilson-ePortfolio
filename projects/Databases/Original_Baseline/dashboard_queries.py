"""
Simplified baseline representation of the CS 340 dashboard database filtering.
"""

from animal_shelter import AnimalShelter

shelter = AnimalShelter("aacuser", "password")


def get_rescue_animals(rescue_type):
    if rescue_type == "Water Rescue":
        query = {
            "animal_type": "Dog",
            "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever"]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
        }
    elif rescue_type == "Mountain or Wilderness Rescue":
        query = {
            "animal_type": "Dog",
            "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog",
                              "Siberian Husky", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
        }
    elif rescue_type == "Disaster or Individual Tracking":
        query = {
            "animal_type": "Dog",
            "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever",
                              "Bloodhound", "Rottweiler"]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300},
        }
    else:
        query = {}
    return shelter.read(query)
