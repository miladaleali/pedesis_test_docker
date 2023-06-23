#!/bin/bash

set -e
echo "Down Docker..."
docker compose down --remove-orphans

echo "Remove Volumes..."
docker volume rm pedesis_redis-data

echo "Remove Celery worker id..."
sudo rm -r celery_files/
