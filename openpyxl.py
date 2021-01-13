#data - https://opendata.vancouver.ca/explore/dataset/census-local-area-profiles-2016/information/


import openpyxl

path='D:\Github repos\pythonStatistics\CensusLocalAreaProfiles2016.xlsx'

demographics_sheet=openpyxl.load_workbook(path,read_only=False,keep_vba=False,data_only=True,keep_links=True)

ws = demographics_sheet.active

print(ws['D6'].value)