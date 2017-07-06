#!/bin/ash

if [[ $TRAVIS_PYTHON_VERSION == '3.2' ]]; then
  echo Run testing...
  python setup.py test
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo Run script...
  python "$1"
else 
  echo Run testing and Coverage testing...
  coverage run setup.py test
fi
echo Done.
