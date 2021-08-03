import os
import shutil
from datetime import datetime
import allure
import selenium
class TestReports:
    def testreport(self):
        directory = datetime.now()
        dt_string = directory.strftime("%d-%B-%Y --- %H-%M-%S")
        # print(dt_string)
        # parentdir = os.path.abspath(os.curdir)
        # print(parentdir)
        reportdir = os.path.join(os.path.abspath(os.curdir),"Report")
        # print(reportdir)
        mydir = os.path.join(reportdir, dt_string.strip())
        files = os.path.join(reportdir, "html")
        # print(mydir)
        # print(files)
        try:
            if files != None:
                os.makedirs(mydir)
                shutil.move(files, mydir)
        except Exception as e:
            print(e)

t = TestReports()
t.testreport()



