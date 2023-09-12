#!/bin/bash

set -e

echo "What command do you want run?"
read command_

if [ "$command_" = "fetchone" ]; then
    # Ask which position
    echo "Give Position id:"
    read position_id

    docker compose exec backend python ./debug/position_status.py fetchone $position_id

else
    docker compose exec backend python ./debug/position_status.py fetchall

fi


