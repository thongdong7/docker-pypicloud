#!/usr/bin/env bash

set -e

export ENV=prod
export STORAGE=s3
export AWS_ACCESS_KEY_ID=abc
export AWS_SECRET_ACCESS_KEY=def
export ADMIN_USERNAME=admin
export ADMIN_PASSWORD=admin
export S3_BUCKET=my_s3_bucket
export READ_USER=guest
export READ_USER_PASSWORD=guest

./venv/bin/python override/code/make_config.py
