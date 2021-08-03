#!/bin/bash
echo working with selenium jenkins and docker
#pip install -r requirements.txt
source venv_framework/bin/activate
cd test
pytest -s -q --alluredir=$WORKSPACE/Report
#allure generate --clean $WORKSPACE/Report -o $WORKSPACE/Report/allure-report
#cd ..
#python3 testreporting.py
#command for aws upload
