#!/usr/bin/env bash

SERVICE_ROOT=$(realpath $(dirname $0)/../)
TESTS_FOLDER=$SERVICE_ROOT/tests
ARGS=$@

poetry run pytest --cov=$SERVICE_ROOT --cov-report term-missing -rav $TESTS_FOLDER $ARGS
