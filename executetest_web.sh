#!/bin/bash
echo Running testing framework
#pip install -r requirements.txt
source venv_framework/bin/activate
cd Report
mkdir xmlfiles
cp environment.properties executor.json launch.json xmlfiles
cd ../test_web
pytest -s -q -m webtest --alluredir=../Report/xmlfiles
allure generate --clean ../Report/xmlfiles -o ../Report/html
cd ..
python3 testreporting.py
rm -r Report/xmlfiles
# Test Ends
