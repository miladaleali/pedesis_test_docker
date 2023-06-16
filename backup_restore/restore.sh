#!/bin/bash

set -e

BACKUP_FILE=/backup/db_backup.sql

until pg_isready; do
    echo "Waiting for postgresql to start.."
    sleep 1
done

if [ -f "$BACKUP_FILE" ]; then
    echo "Restoring database from backup..."
    psql -U postgres < $BACKUP_FILE
    echo "Restore complete."
else
    echo "No backup file found. Skipping restore."
fi
