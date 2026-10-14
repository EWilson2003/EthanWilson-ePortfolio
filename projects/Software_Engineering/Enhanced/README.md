# Inventory Tracker - CS 499 Enhanced Version
Enhancements:
- Separates model, repository/data-access, service/application logic, and UI responsibilities.
- Validates usernames, passwords, item names, quantities, and low-stock thresholds.
- Adds inventory search and low-stock filtering.
- Stores password hashes rather than plaintext passwords.
- Uses parameterized SQLite queries.
- Adds a service layer so activities do not directly contain database rules.
- Adds clear result handling and maintainable domain objects.

The source is organized as an Android-ready Java design. Android SDK compilation must be performed
in Android Studio on a machine with the required SDK installed.
