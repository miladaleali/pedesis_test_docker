#!/bin/bash

set -e

echo "Create NEW USER..."
docker compose exec backend python -m pedesis create usertest milad aleali miladaleali miladaleali1392@gmail.com 09921374939 123456

echo "Create NEW USER BROKER..."
docker compose exec backend python -m pedesis create userbrokertest miladaleali 123456 okx $DEBUG_BROKER_API_KEY $DEBUG_BROKER_SECRET_KEY $DEBUG_BROKER_PASSPHRASE

echo "Create NEW CONTRACT..."
docker compose exec backend python -m pedesis create contracttest --add-to-station miladaleali okx 32000 50 360 123456
