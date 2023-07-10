#!/bin/bash

set -e

echo "Debug Send Signal"
docker compose exec backend python ./debug/send_signal.py
