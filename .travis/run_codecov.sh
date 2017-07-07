#!/bin/bash

echo Installing codecov...
if [[ $TRAVIS_PYTHON_VERSION == '3.2' ]]; then
  pip install coverage==4.0a5 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  pip install coverage==3.7.1 || exit 1
fi
pip install codecov || exit 1

echo Coverage testing...
coverage run setup.py test || exit 1
echo Done.
