# -*- coding:utf-8 -*-
'''
Created on 2013年9月5日

@author: wangzining
'''
import xlrd

path=r"f://test//test.xls"
book=xlrd.open_workbook(path)

sheetname=book.sheet_names()[0]
print sheetname

sheet=book.sheet_by_name(sheetname)
nrows=sheet.nrows
ncols=sheet.ncols
print nrows,ncols

row_data=sheet.row_values(0)
col_data=sheet.col_values(0)
print row_data,col_data

cell_value=sheet.cell_value(0,1)
print cell_value