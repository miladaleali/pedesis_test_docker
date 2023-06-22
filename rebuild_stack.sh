#!/bin/bash

set -e

echo "Build stack without cache..."
docker compose --profile logs build --no-cache

echo "Stack up..."
docker compose --profile logs up