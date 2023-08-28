#! /usr/bin/env bash

# Let the DB start
python /app/app/backend_pre_start.py

# Run migrations
alembic upgrade b7b29fde792b

# Create initial data in DB
# python /app/app/initial_data.py
python initial_brokers.py

# Run station
python manage.py run station