import os
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import pandas as pd 
from datetime import datetime
from pandas import Series,DataFrame


import xlrd
from xlrd import xldate_as_tuple
data = xlrd.open_workbook(r'same_sexmarried.xlsx')
table = data.sheets()[0]

def import_excel(excel):
    tables = []
    for rown in range(excel.nrows):
        add = True
        array = {'tweets':'', 'target':'','score':''}
        #if(table.cell_value(rown, 0) !='' and table.cell_value(rown, 1) != '' and table.cell_value(rown, 2) != '' and table.cell_value(rown, 2) != 0 ):
        if(table.cell_value(rown, 0) !='' and table.cell_value(rown, 1) != '' and table.cell_value(rown, 2) != ''):

            array['tweets'] = table.cell_value(rown, 0)
            array['target'] = table.cell_value(rown, 1)
            array['score'] = table.cell_value(rown, 2)
            tables.append(array)
    return tables
tables = import_excel(table)
count = 0
for i in tables:
        print(i['tweets'])
        print(i['target'])
        print(i['score'])
        count = count +1
print(count)

