#!/bin/bash

echo Installing codecov and its dependencies...

if [[ $TRAVIS_PYTHON_VERSION == '3.2' ]]; then
  pip install requests==2.12.0 || exit 1 # 2.17.3
  pip install coverage==4.0a5 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  pip install requests==2.7.9 || exit 1 # ?????????????? miss for codecov install
  pip install coverage==3.7.1 || exit 1
fi
pip install codecov || exit 1

echo Coverage testing...

if [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  coverage run "$1" || exit 1
else
  coverage run setup.py test || exit 1
fi

echo Done.
