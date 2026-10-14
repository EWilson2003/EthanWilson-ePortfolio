"""
CS 499 Enhancement Three - Databases
Improved MongoDB data-access layer for the CS 340 Animal Shelter Dashboard.
"""

from __future__ import annotations
import os
from typing import Any, Dict, List, Mapping, Optional

from pymongo import ASCENDING, MongoClient
from pymongo.errors import PyMongoError

Document = Dict[str, Any]


class AnimalShelter:
    """Validated, reusable MongoDB repository for Austin Animal Center records."""

    ALLOWED_UPDATE_FIELDS = {
        "name", "animal_type", "breed", "color", "date_of_birth",
        "datetime", "monthyear", "outcome_type", "outcome_subtype",
        "sex_upon_outcome", "age_upon_outcome_in_weeks", "location_lat",
        "location_long",
    }

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        host: str = "localhost",
        port: int = 27017,
        database: str = "AAC",
        collection: str = "animals",
    ) -> None:
        username = username or os.getenv("AAC_MONGO_USER")
        password = password or os.getenv("AAC_MONGO_PASSWORD")
        if not username or not password:
            raise ValueError(
                "MongoDB credentials are required. Use constructor arguments or "
                "AAC_MONGO_USER/AAC_MONGO_PASSWORD environment variables."
            )

        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={database}"
        self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def ensure_indexes(self) -> None:
        """Create indexes used by the dashboard's most common filters."""
        self.collection.create_index([("animal_id", ASCENDING)], unique=True, sparse=True)
        self.collection.create_index(
            [("animal_type", ASCENDING), ("breed", ASCENDING),
             ("sex_upon_outcome", ASCENDING), ("age_upon_outcome_in_weeks", ASCENDING)],
            name="rescue_filter_idx",
        )
        self.collection.create_index([("outcome_type", ASCENDING)], name="outcome_type_idx")

    @staticmethod
    def _clean_query(query: Optional[Mapping[str, Any]]) -> Document:
        if query is None:
            return {}
        if not isinstance(query, Mapping):
            raise TypeError("query must be a mapping/dictionary")
        return dict(query)

    @staticmethod
    def _validate_document(data: Mapping[str, Any]) -> Document:
        if not isinstance(data, Mapping) or not data:
            raise ValueError("data must be a non-empty dictionary")
        cleaned = dict(data)
        if "age_upon_outcome_in_weeks" in cleaned:
            age = cleaned["age_upon_outcome_in_weeks"]
            if not isinstance(age, (int, float)) or age < 0:
                raise ValueError("age_upon_outcome_in_weeks must be a non-negative number")
        return cleaned

    def create(self, data: Mapping[str, Any]) -> bool:
        try:
            document = self._validate_document(data)
            return self.collection.insert_one(document).acknowledged
        except PyMongoError as exc:
            raise RuntimeError(f"MongoDB create failed: {exc}") from exc

    def read(
        self,
        query: Optional[Mapping[str, Any]] = None,
        projection: Optional[Mapping[str, int]] = None,
        limit: int = 0,
        sort_field: Optional[str] = None,
        ascending: bool = True,
    ) -> List[Document]:
        if limit < 0 or limit > 10000:
            raise ValueError("limit must be between 0 and 10000")
        try:
            cursor = self.collection.find(self._clean_query(query), projection)
            if sort_field:
                cursor = cursor.sort(sort_field, ASCENDING if ascending else -1)
            if limit:
                cursor = cursor.limit(limit)
            return list(cursor)
        except PyMongoError as exc:
            raise RuntimeError(f"MongoDB read failed: {exc}") from exc

    def update(self, query: Mapping[str, Any], changes: Mapping[str, Any]) -> int:
        clean_query = self._clean_query(query)
        if not clean_query:
            raise ValueError("Refusing an unfiltered update.")
        clean_changes = self._validate_document(changes)
        disallowed = set(clean_changes) - self.ALLOWED_UPDATE_FIELDS
        if disallowed:
            raise ValueError(f"Update contains disallowed fields: {sorted(disallowed)}")
        try:
            return self.collection.update_many(clean_query, {"$set": clean_changes}).modified_count
        except PyMongoError as exc:
            raise RuntimeError(f"MongoDB update failed: {exc}") from exc

    def delete(self, query: Mapping[str, Any]) -> int:
        clean_query = self._clean_query(query)
        if not clean_query:
            raise ValueError("Refusing an unfiltered delete.")
        try:
            return self.collection.delete_many(clean_query).deleted_count
        except PyMongoError as exc:
            raise RuntimeError(f"MongoDB delete failed: {exc}") from exc

    def close(self) -> None:
        self.client.close()
