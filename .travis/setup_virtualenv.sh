#!/bin/ash

virtualenv "~/virtualenv/python$1"
virtualenv -p "/usr/bin/python$1" "~/virtualenv/python$1"
cp -pf "~/virtualenv/python$1/bin/python$1" "~/virtualenv/python$1/bin/python"
source "~/virtualenv/python$1/bin/activate"
export TRAVIS_PYTHON_VERSION="$1"
