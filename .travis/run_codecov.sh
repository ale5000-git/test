#!/bin/bash

echo Installing codecov...
pip install codecov

if [[ $TRAVIS_PYTHON_VERSION == '3.2_' ]]; then
  echo Testing...
  python setup.py test
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo Running...
  python "$1"
else 
  echo Coverage testing...
  coverage run setup.py test
fi
echo Done.
