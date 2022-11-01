#!/bin/bash
# Usage: restore.sh /path/to/docker-compose.yml

docker-compose -f "$1" down -v
docker-compose up -d --build
