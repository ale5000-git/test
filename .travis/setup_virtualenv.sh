#!/bin/bash

echo '------------------'
echo "PATH: $PATH"
echo '------------------'
easy_install --version
echo '------------------'
pip --version
echo '------------------'

if [[ -n "$1" ]]; then VER="$1"; else VER="$Python"; fi

if [[ $VER == '3.1' ]]; then
  VENV_VER='13.1.2'
elif [[ $VER == '2.5' ]]; then
  VENV_VER='1.9.1'
elif [[ $VER == '2.4' ]]; then
  VENV_VER='1.7.2'
elif [[ $VER == '2.3' ]]; then
  VENV_VER='1.3.1'
  ############### 1.3.2
fi

if [[ $VER == '3.1' ]]; then
  mkdir -p "$HOME/.local/lib/python$VER/site-packages"
  echo '*** Python - Installing Setuptools...'
  wget -q "https://pypi.python.org/packages/source/s/setuptools/setuptools-18.2.tar.gz" || exit 1
  tar -xz -f "setuptools-18.2.tar.gz" || exit 1
  cd "setuptools-18.2/" || exit 1
  "python$VER" setup.py install --prefix="$HOME/.local" || exit 1
  cd .. || exit 1

  #echo '*** Python - Installing Pip...'
  #wget -q "https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz" || exit 1
  #tar -xz -f "pip-1.5.6.tar.gz" || exit 1
  #cd "pip-1.5.6/" || exit 1
  #"python$VER" setup.py install --prefix="$HOME/.local" || exit 1
  #cd .. || exit 1

  echo '*** Python - Installing Pip...'
  "easy_install-$VER" --prefix="$HOME/.local" pip==1.5.6 || exit 1
fi

if [[ -n "$VENV_VER" ]]; then
  echo '*** Python - Installing Virtualenv...'
  wget -q "https://pypi.python.org/packages/source/v/virtualenv/virtualenv-${VENV_VER}.tar.gz" || exit 1
  tar -xz -f "virtualenv-${VENV_VER}.tar.gz" || exit 1
  cd "virtualenv-${VENV_VER}/" || exit 1
  if [[ $VER == '3.1' ]]; then
    #rm -rf virtualenv_support/setuptools-*.whl || exit 1
    rm -rf virtualenv_support/pip-*.whl || exit 1
  fi
  "python$VER" setup.py install --prefix="$HOME/.local" || exit 1
  cd .. || exit 1
fi

if [[ $VER == '2.3' ]]; then
  echo '.' #echo '*** Python - Updating Setuptools...'
  #easy_install setuptools==1.4.2 #|| exit 1 #################
  cp -pf "$TRAVIS_BUILD_DIR/.travis/lib/subprocess.py" "$HOME/.local/lib/python$VER/site-packages" || exit 1
fi

echo '*** Python - Virtualenv setup in progress...'
if [[ $VER == '3.1' ]]; then
  "virtualenv-$VER" -p "python$VER" "$HOME/virtualenv/python$VER" || exit 1
elif [[ $VER == '2.3' ]]; then
  "python$VER" "$HOME/.local/lib/python$VER/site-packages/virtualenv.py" -p "python$VER" "$HOME/virtualenv/python$VER" ###|| exit 1
   echo '...'
else
  "virtualenv-$VER" -p "python$VER" "$HOME/virtualenv/python$VER" || exit 1
fi
source "$HOME/virtualenv/python$VER/bin/activate" || exit 1

export TRAVIS_PYTHON_VERSION="$VER"

#if [[ $VER == '2.3' ]]; then
  #easy_install setuptools==1.4.2 || exit 1 #################
#fi

if [[ $TRAVIS_PYTHON_VERSION == '2.3' ]]; then
  echo '*** Python - Updating Setuptools...'
  easy_install setuptools==1.4.2 #|| exit 1 #################
fi

echo '------------------'
pip --version
echo '------------------'

if [[ $TRAVIS_PYTHON_VERSION == '3.1' ]]; then
  echo '*** Python - Downgrading Pip...'
  pip install pip==1.5.6 || exit 1
  #"easy_install-$VER" pip==1.5.6 || exit 1
elif [[ $TRAVIS_PYTHON_VERSION == '2.5' ]]; then
  echo '*** Python - Downgrading Pip (Workaround for missing SSL in Python 2.5)...'
  easy_install pip==1.2.1 || exit 1
fi

echo '------------------'
easy_install --version
echo '------------------'
pip --version
echo '------------------'

echo '*** Done.'
