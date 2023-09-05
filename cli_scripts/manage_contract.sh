#!/bin/bash

set -e

echo "What command do you want run?"
read command_

if [ "$command_" = "init" ]; then
    # Ask contract length
    echo "Give Contract Len:"
    read contract_len

    docker compose exec backend python ./debug/manage_contract.py init $contract_len

else
    docker compose exec backend python ./debug/manage_contract.py delete

fi


