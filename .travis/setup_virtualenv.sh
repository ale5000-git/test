#!/bin/bash

virtualenv "~/virtualenv/python$1"
rm -f "~/virtualenv/python$1/bin/python"
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1"
source "~/virtualenv/python$1/bin/activate"
export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  pip install setuptools==1.4.2
fi
