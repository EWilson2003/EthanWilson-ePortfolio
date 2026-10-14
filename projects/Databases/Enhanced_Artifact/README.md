# CS 499 Enhancement Three: Databases

This enhancement implements the Module One plan for the CS 340 Animal Shelter Dashboard.

## Improvements
- Centralized MongoDB access in a reusable repository class.
- Removed hard-coded credentials from the enhanced code; credentials can be supplied at runtime or by environment variables.
- Added validation and explicit protection against unfiltered update/delete operations.
- Added reusable rescue-filter query construction and optional breed filtering.
- Added MongoDB indexes for common dashboard lookups.
- Added projection, result limits, sorting, exception handling, and connection cleanup.
- Added a service layer so dashboard callbacks do not need to construct raw database operations.
- Added unit tests for the query builder.

## Suggested environment
Python 3.10+ and PyMongo. A running MongoDB AAC database is required for live CRUD operations.
The query-builder unit tests do not require MongoDB.
