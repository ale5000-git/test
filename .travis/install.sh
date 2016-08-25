#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    # Install some custom requirements on OS X
    brew install pyenv-virtualenv
fi
