#!/bin/sh

echo Coverage testing...

if [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  coverage run "$1" || exit 1
else
  coverage run setup.py test || exit 1
fi

echo Done.
