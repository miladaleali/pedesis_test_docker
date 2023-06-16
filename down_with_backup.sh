#!/bin/bash

set -e

echo "Creating database backup before stopping the stack..."
docker-compose exec db /backup_restore/backup.sh

echo "Stopping the stack..."
docker-compose down

echo "Backup and stop complete."
