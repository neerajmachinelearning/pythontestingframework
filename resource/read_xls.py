from resource import constants
from resource.xls_reader import XLS_Reader

def getcelldata(testname, filepath):
    datalist = []
    xls = XLS_Reader(filepath)
    sheetname = constants.DATASHEETNAME
    teststartrowindex = 0
    while not(xls.get_cell_value(sheetname, teststartrowindex, 0) == testname):
        teststartrowindex = teststartrowindex + 1
    columnstartrowindex = teststartrowindex + 1
    datastartrownindex = columnstartrowindex + 1

    maxrow = 0
    try:
        while not(xls.check_empty_cell(sheetname,datastartrownindex+maxrow, 0)==True):
            maxrow = maxrow + 1
    except Exception:
        pass

    maxcol = 0
    try:
        while not(xls.check_empty_cell(sheetname, columnstartrowindex, maxcol) == True):
            maxcol = maxcol + 1
    except Exception:
        pass

    # print(f"teststartrowindex: {teststartrowindex}, columnstartrowindex: {columnstartrowindex}, datastartrownindex: {datastartrownindex}, maxcol: {maxcol}, maxrow: {maxrow}")

    for rNum in range(datastartrownindex, datastartrownindex+maxrow):
        datadictionary = {}
        for cNum in range(0, maxcol):
            datakey = xls.get_cell_value(sheetname, columnstartrowindex, cNum)
            datavalue = xls.get_cell_value(sheetname, rNum, cNum)
            # print(f"{datakey} >> {datavalue}")
            datadictionary[datakey] = datavalue
        datalist.append(datadictionary)
    return datalist

def isRunnable(testcasename, path):
    xls = XLS_Reader(path)
    rows = xls.get_row_count(constants.TESTCASEDATASHEET)
    for rNum in range(0, rows):
        testname = xls.get_cell_data_by_col_name(constants.TESTCASEDATASHEET, rNum, constants.TCID)
        if testname == testcasename:
            runmode = xls.get_cell_data_by_col_name(constants.TESTCASEDATASHEET, rNum, constants.RUNMODE)
            if runmode.lower() == 'y':
                return True
            else:
                return False


# xls = XLS_Reader("/Users/neerajsharma/PycharmProjects/Framework_Web/resource/testdata.xlsx")
# value = xls.get_cell_data_by_col_name("testcases", "loginTest", 1, "TCID")
# columncount = xls.get_col_count("testcases")
# print(value)
# print(columncount)
#
# value1 = xls.get_cell_data_by_col_name("testdata", 2, "loginTest", "Password")
# print(value1)
