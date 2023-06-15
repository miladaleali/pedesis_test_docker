#!/bin/bash

set -e

BACKUP_FILE=/backup/db_backup.sql

if [ -f "$BACKUP_FILE" ]; then
    echo "Restoring database from backup..."
    psql -U postgres < $BACKUP_FILE
    echo "Restore complete."
else
    echo "No backup file found. Skipping restore."
fi
