#!/bin/sh
sleep 30

python initdb.py
exec $@
