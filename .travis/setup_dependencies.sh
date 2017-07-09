#!/bin/bash

echo '*** Installing dependencies...'

if [[ $TRAVIS_PYTHON_VERSION == '3.2' ]]; then
  pip install coverage==4.0a5 || exit 1
  pip install requests==2.10.0 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' || $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  pip install coverage==3.7.1 || exit 1
  #pip install requests==2.7.9 || exit 1 # ?????????????? miss for codecov install
else
  :  # Coverage and requests are automatically installed by codecov.
fi

if [[ $TRAVIS_PYTHON_VERSION == '3.1' ]]; then
  pip install unittest2==0.8 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.5' || $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  pip install unittest2==0.5.1 || exit 1
else
  pip install unittest2 || exit 1
  pip install codecov || exit 1
fi

echo '*** Done.'
