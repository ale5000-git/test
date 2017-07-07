#!/bin/bash

virtualenv "~/virtualenv/python$1"
rm -f "~/virtualenv/python$1/bin/python"
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1"
source "~/virtualenv/python$1/bin/activate"
export TRAVIS_PYTHON_VERSION="$1"

easy_install --version

#if [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  #pip install distribute==0.6.49 || exit 1
#fi

easy_install --version

pip install pip==1.1 || exit 1

easy_install pip==1.1 || exit 1

easy_install --version

# ==1.4.2

######### python-setuptools (but you can install python-setuptools-deadsnakes)
