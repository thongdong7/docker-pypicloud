#!/usr/bin/env bash

set -e
#docker build -t pypi .
#
#docker run -ti --rm --entrypoint bash pypi
#docker-compose build
docker-compose pull
docker-compose rm -f
docker-compose up

