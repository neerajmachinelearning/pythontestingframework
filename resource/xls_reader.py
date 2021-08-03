import xlrd3 as xlrd

class XLS_Reader:

    def __init__(self, path):
        self.path = path
        self.readxls = xlrd.open_workbook(path)

    def get_cell_value(self, sheetname, rindex, cindex):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.cell_value(rindex, cindex)

    def get_cell_data_by_col_name(self, sheetname, rindex, colname):
        sheet = self.readxls.sheet_by_name(sheetname)
        for cnum in range(0, self.get_col_count(sheetname)):
            extractcolumnname = sheet.cell_value(0, cnum)
            if extractcolumnname == colname:
                celldata = sheet.cell_value(rindex, cnum)
                if celldata != "":
                    return celldata
                else:
                    return "cell data value is empty for given rnindex and column name"

    def get_col_count(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.ncols

    def get_row_count(self, sheetname):
        sheet = self.readxls.sheet_by_name(sheetname)
        return sheet.nrows

    def get_test_row_number(self, sheetname, testname):
        test_start_row_index = 0
        sheet = self.readxls.sheet_by_name(sheetname)
        while not (sheet.cell_value(test_start_row_index, 0))== testname:
            test_start_row_index = test_start_row_index + 1
        return test_start_row_index

    def check_empty_cell(self, sheetname, rindex, cindex):
        sheet = self.readxls.sheet_by_name(sheetname)
        cellvalue = sheet.cell_value(rindex, cindex)
        if cellvalue == "":
            return True
        else:
            return False




