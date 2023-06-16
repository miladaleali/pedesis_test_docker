#!/bin/bash

set -e

echo "Creating database backup before stopping the stack..."
docker compose up db -d

docker compose exec db /backup_restore/restore.sh

echo "Stopping the stack..."
docker compose down --remove-orphans

echo "Restore complete."
