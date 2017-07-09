#!/bin/bash

if [[ $1 == '2.5' ]]; then
  echo '------------------------------------------'
  ls /usr/lib/python2.5/dist-packages
  echo '------------------------------------------'
  ls /usr/lib/python2.5/site-packages
  echo '------------------------------------------'
  ls /usr/bin/python2.5
  echo '------------------------------------------'
  ls /usr/python2.5
  echo '------------------------------------------'
  ls /usr/python2.5/lib/python2.5
  echo '------------------------------------------'
  ls /usr/python2.5/lib/python2.5/site-packages
  echo '------------------------------------------'
  ls /usr/python2.5/lib/python2.5/dist-packages
  echo '------------------------------------------'
  ls python2.5/lib/python2.5/site-packages
  echo '------------------------------------------'
  ls python2.5/lib/python2.5/dist-packages
  echo '------------------------------------------'
  #mkdir '~/python'
  #cp -p python$1 '~/python/python'
  #export PATH="~/python/python:$PATH"
  echo '*** Python - Updating Virtualenv...'
  "/usr/lib/python$1/dist-packages/easy_install" --user virtualenv==1.9.1 || exit 1
else
  exit 1
fi
virtualenv --version


echo '*** Python - Virtualenv setup in progress...'
virtualenv -p "python$1" --setuptools "~/virtualenv/python$1" || exit 1
source "~/virtualenv/python$1/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$1"

if [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  echo '*** Python - Updating Virtualenv...'
  #easy_install virtualenv==1.9.1 || exit 1
  #pip install virtualenv==1.9.1 || exit 1
fi

virtualenv --version

if [[ $TRAVIS_PYTHON_VERSION == '3.1' ]]; then
  echo '*** Python - Updating Setuptools...'
  pip install -U setuptools || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.5' || $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Python - Updating Setuptools...'
  pip install setuptools==1.4.2 || exit 1

  echo '*** Python - Updating Pip...'
  pip install pip==1.1 || exit 1
fi

echo '*** Done.'
