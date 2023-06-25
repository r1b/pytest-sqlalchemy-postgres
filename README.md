# pytest-sqlalchemy-postgres

Pytest plugin for testing Postgres with a SQLAlchemy session. Uses savepoints to isolate tests.

## Installation

`pip install pytest-sqlalchemy-postgres`

## Usage

See sample usage in `tests/example/`

## Rationale

This realizes a common pattern for testing an application against a live database for local development / CI:

1. Start the test runner
2. Drop all tables in the test database
3. Create all tables in the test database
4. For each test
   1. Create a transaction
   2. For each database interaction
      1. Create a savepoint
      2. Do stuff
      3. Release the savepoint
   3. Rollback the transaction

## Limitations

- Cannot test code that explicitly creates transactions

In other words, `session.add`, `session.flush` and `session.commit` are all OK. `session.begin` is not. This is sufficient for most use cases.