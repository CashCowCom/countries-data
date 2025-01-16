#!/usr/bin/env bash


ARGS=$@
rm -rf dist
poetry build $ARGS
