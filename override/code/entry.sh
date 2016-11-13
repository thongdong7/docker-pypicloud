#!/usr/bin/env bash

echo Make config file...
./venv/bin/python make_config.py

echo Start nginx
service nginx start

echo Start..
./venv/bin/uwsgi --ini-paste-logged server.ini

echo Bye!
