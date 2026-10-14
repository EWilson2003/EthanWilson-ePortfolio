"""
Dashboard-facing service layer. UI code can call this module without constructing
raw MongoDB queries in callbacks.
"""

from typing import Any, Dict, List
from animal_shelter import AnimalShelter
from query_builder import build_rescue_query


class AnimalDashboardService:
    def __init__(self, repository: AnimalShelter):
        self.repository = repository

    def filter_animals(
        self, rescue_type: str = "Reset", breed_text: str = "", limit: int = 1000
    ) -> List[Dict[str, Any]]:
        query = build_rescue_query(rescue_type, breed_text)
        return self.repository.read(
            query=query,
            projection={"_id": 0},
            limit=limit,
            sort_field="animal_id",
        )

    def add_animal(self, record: Dict[str, Any]) -> bool:
        return self.repository.create(record)

    def edit_animal(self, animal_id: str, changes: Dict[str, Any]) -> int:
        if not animal_id or not animal_id.strip():
            raise ValueError("animal_id is required")
        return self.repository.update({"animal_id": animal_id.strip()}, changes)

    def remove_animal(self, animal_id: str) -> int:
        if not animal_id or not animal_id.strip():
            raise ValueError("animal_id is required")
        return self.repository.delete({"animal_id": animal_id.strip()})
