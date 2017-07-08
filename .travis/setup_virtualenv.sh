#!/bin/bash

echo '*** Python Virtualenv setup in progress...'
virtualenv "~/virtualenv/python$1" || exit 1
rm -f "~/virtualenv/python$1/bin/python" || exit 1
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1" || exit 1
source "~/virtualenv/python$1/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '2.5' || $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Installing Python Setuptools (part 1)...'
  easy_install 'http://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.3.tar.gz' || exit 1
  rm -rf "~/virtualenv/python$1/lib/python$1/site-packages/distribute-"* || exit 1

  echo '*** Installing Python Pip...'
  if [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then pip install pip==1.3.1 || exit 1; else pip install pip==1.1 || exit 1; fi

  #pip install setuptools==0.7.3 > /dev/null 2>&1 || exit 1

  echo '*** Installing Python Setuptools (part 2)...'
  #pip install setuptools==1.4.2 || exit 1
  easy_install setuptools==1.4.2
  echo '-------------------------------'
  easy_install --version
fi

echo '*** Done.'
