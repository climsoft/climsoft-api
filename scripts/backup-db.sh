#!/bin/bash

# USAGE: ./backup-db.sh DB_HOST DB_PORT DB_USER DB_PASS
# This script generates a backup file named ALL_DB_BACKUP_DOW.sql
# Where DOW could be replaced by SUN, MON, TUE, WED, THU, FRI, SAT
# You could schedule this at midnight and you will have backup of
# all databases on a host with all data, for last seven days.

if (($# < 4)) || (($# > 4))
then
  echo "4 arguments required."
  echo "Usage: ./backup-db.sh DB_HOST DB_PORT DB_USER DB_PASS"
  echo "Example: ./backup-db.sh localhost 3306 root password"
  exit 1
fi

DOW=$(date +%a)

DB_HOST=$1
DB_PORT=$2
DB_USER=$3
DB_PASS=$4

BACKUP_FILENAME="ALL_DB_BACKUP_${DOW^^}.sql"

export MYSQL_PWD=$DB_PASS

mysqldump --column-statistics=0 --host "$DB_HOST" --port "$DB_PORT" --protocol=tcp --user "$DB_USER" --flush-privileges --all-databases >| "$BACKUP_FILENAME"
