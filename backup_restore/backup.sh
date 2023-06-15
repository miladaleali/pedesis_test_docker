#!/bin/bash

set -e

BACKUP_FILE=/backup/db_backup.sql

echo "Backing up database..."

pg_dumpall -U postgres > $BACKUP_FILE

echo "Backup complete."
