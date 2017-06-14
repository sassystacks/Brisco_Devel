from Connect_Brisco_DB import Connect_DB
from extractCSV import ExtractCSV
from datetime import datetime, date, time
A = Connect_DB('postgres','postgres','localhost','Boom_boom1')
B = ExtractCSV(A,'test.csv',11,2016)
B.TestPrint()
A.crsr().close()
A.cnct().close
# month = 3
# date1 = date(2016,month,1)
#
# print(date1)
# print(type(date1))
