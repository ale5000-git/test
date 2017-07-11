#!/bin/bash

if [[ -n "$1" ]]; then VER="$1"; else VER="$Python"; fi

echo '*** Python - Installing Virtualenv...'
if [[ $VER == '3.1' ]]; then
  VENV_VER='13.1.2'
elif [[ $VER == '2.5' ]]; then
  VENV_VER='1.9.1'
elif [[ $VER == '2.4' ]]; then
  VENV_VER='1.7.2'
elif [[ $VER == '2.3' ]]; then
  VENV_VER='1.3.2'
  ###############
else
  #easy_install -U virtualenv || exit 1
  VENV_VER='x.x' #################################
fi
wget -q "https://pypi.python.org/packages/source/v/virtualenv/virtualenv-${VENV_VER}.tar.gz" || exit 1
tar -xz -f "virtualenv-${VENV_VER}.tar.gz" || exit 1
cd "virtualenv-${VENV_VER}/"
"python$VER" setup.py install --prefix="~/.local" || exit 1
cd ..

echo '*** Python - Virtualenv setup in progress...'
if [[ $VER == '2.4' ]]; then
  exit 0
  virtualenv -p "python$VER" "~/virtualenv/python$VER" || exit 1
elif [[ $VER == '2.3' ]]; then
  ls "$TRAVIS_BUILD_DIR/.travis"
  cp -pf $TRAVIS_BUILD_DIR/.travis/lib/subprocess.py ~/.local/lib/python$VER/site-packages #|| exit 1
  "python$VER" virtualenv.py -p "python$VER" --setuptools "~/virtualenv/python$VER" #|| exit 1
else
  exit 0
  virtualenv -p "python$VER" --setuptools "~/virtualenv/python$VER" || exit 1
fi
source "~/virtualenv/python$VER/bin/activate" #|| exit 1

export TRAVIS_PYTHON_VERSION="$VER"

if [[ $TRAVIS_PYTHON_VERSION == '3.1' ]]; then
  echo '*** Python - Updating Setuptools...'
  easy_install 'https://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.3.tar.gz' > /dev/null 2>&1 || exit 1
  rm -rf "~/virtualenv/python$VER/lib/python$VER/site-packages/distribute-"* || exit 1
  pip install setuptools==19.4 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  echo '*** Python - Updating Setuptools...'
  easy_install setuptools==1.4.2 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Python - Updating Setuptools...'
  pip install setuptools==1.4.2 || exit 1
fi

if [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  echo '*** Python - Updating Pip...'
  easy_install pip==1.2.1 || exit 1  # Workaround for missing SSL
  #easy_install ssl || exit 1  # Needed by pip 1.3.1
  #pip install pip==1.3.1 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.4' ]]; then
  echo '*** Python - Updating Pip...'
  pip install pip==1.1 || exit 1
fi

echo '*** Done.'
