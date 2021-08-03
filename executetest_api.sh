#!/bin/bash
echo working with selenium jenkins and docker
cd /Users/neerajsharma/AutomationProjects/IndependentAutomation/framework_webtesting/Report
mkdir xmlfiles
cp environment.properties executor.json launch.json xmlfiles
cd /Users/neerajsharma/AutomationProjects/IndependentAutomation/framework_webtesting/test_api
pytest -s -q --alluredir=/Users/neerajsharma/AutomationProjects/IndependentAutomation/framework_webtesting/Report/xmlfiles
allure generate --clean /Users/neerajsharma/AutomationProjects/IndependentAutomation/framework_webtesting/Report/xmlfiles -o /Users/neerajsharma/AutomationProjects/IndependentAutomation/framework_webtesting/Report/html
cd ..
python3 testreporting.py
rm -r Report/xmlfiles
#command for aws upload

