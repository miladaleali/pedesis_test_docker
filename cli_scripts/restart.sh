#!/bin/bash

set -e

echo "restarting all things after debuging position..."
./safe_down.sh

echo "deleting db data"
sudo rm -r ../data

echo "restore db"
./restore_db.sh

echo "rebuild stack"
./rebuild_stack.sh


