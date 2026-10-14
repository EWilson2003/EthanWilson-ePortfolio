"""
Centralized, validated query builder for dashboard rescue filters.
"""

from typing import Any, Dict

RESCUE_PROFILES = {
    "Water Rescue": {
        "breeds": ["Labrador Retriever Mix", "Chesapeake Bay Retriever",
                   "Newfoundland", "Labrador Retriever"],
        "sex": "Intact Female",
        "min_age": 26,
        "max_age": 156,
    },
    "Mountain or Wilderness Rescue": {
        "breeds": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog",
                   "Siberian Husky", "Rottweiler"],
        "sex": "Intact Male",
        "min_age": 26,
        "max_age": 156,
    },
    "Disaster or Individual Tracking": {
        "breeds": ["Doberman Pinscher", "German Shepherd", "Golden Retriever",
                   "Bloodhound", "Rottweiler"],
        "sex": "Intact Male",
        "min_age": 20,
        "max_age": 300,
    },
}


def build_rescue_query(rescue_type: str, breed_text: str = "") -> Dict[str, Any]:
    """Build one safe MongoDB query from approved dashboard filters."""
    if rescue_type in ("Reset", "All", "", None):
        query: Dict[str, Any] = {}
    elif rescue_type not in RESCUE_PROFILES:
        raise ValueError("Unknown rescue filter")
    else:
        profile = RESCUE_PROFILES[rescue_type]
        query = {
            "animal_type": "Dog",
            "breed": {"$in": profile["breeds"]},
            "sex_upon_outcome": profile["sex"],
            "age_upon_outcome_in_weeks": {
                "$gte": profile["min_age"],
                "$lte": profile["max_age"],
            },
        }

    breed_text = (breed_text or "").strip()
    if breed_text:
        if len(breed_text) > 80:
            raise ValueError("Breed filter is too long")
        # Escape regex metacharacters so user text is treated literally.
        import re
        query["breed"] = {"$regex": re.escape(breed_text), "$options": "i"}
    return query
