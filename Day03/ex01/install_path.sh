#!/bin/bash
rm -rf -p local_lib my_folder
rm -f -p local_lib.log
/Users/${USER}/.brew/opt/python@3.9/bin/python3.9 -m pip3 install --upgrade pip3
pip3 --version
pip3 install --upgrade --target=./local_lib git+https://github.com/jaraco/path.git > local_lib.log
python3 make_my_dir.py