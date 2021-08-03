import os

PROJECTPATH = os.path.abspath(os.pardir)
RESOURCEPATH = PROJECTPATH + "/resource"
print(RESOURCEPATH)
# RESOURCEPATH = "/Users/neerajsharma/PycharmProjects/Framework_Web/resource/"
PROPERTYPATH = RESOURCEPATH+"/property.properties"
DATASHEETPATH = RESOURCEPATH+"/testdata.xlsx"
DATASHEETNAME = 'testdata'
print(DATASHEETPATH)
TESTCASEDATASHEET = 'testcases'
TCID = 'TCID'
RUNMODE = 'Runmode'
GRIDRUN_Y = 'Y'
ENVIRONMENTPATH = RESOURCEPATH+'Report/environment.properties'

# API Environment
# TALECH_HOST = 'https://web-dev-11.talech.com'
# WAPI_BE_HOST = 'https://wapi-dev-11.talech.com'
TALECH_HOST = 'https://web-aqa-05.talech.com'
WAPI_BE_HOST = 'https://wapi-aqa-05.talech.com'
# TALECH_HOST = 'https://web-dev-16.talech.com'
# WAPI_BE_HOST = 'https://wapi-dev-16.talech.com'
# CODE = 'hgtr123463hgtr123463hgtr1234634'
