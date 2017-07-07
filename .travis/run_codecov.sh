#!/bin/bash

#echo Installing codecov...
#pip install codecov || exit 1

if [[ $TRAVIS_PYTHON_VERSION == '3.2_' ]]; then
  pip install coverage==4.3.1 || exit 1
  echo Testing...
  python setup.py test || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo Running...
  python "$1" || exit 1
else
  pip install codecov || exit 1
  echo Coverage testing...
  coverage run setup.py test || exit 1
fi
echo Done.
