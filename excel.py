import pandas as pd
import numpy as np
from xlsxwriter.utility import xl_rowcol_to_cell

template = pd.read_excel("C:\\Users\\admin\\Desktop\\Book1.xlsx",na_values=np.nan,header=None)
testSheet = pd.read_excel("C:\\Users\\admin\\Desktop\\Book2.xlsx",na_values=np.nan,header=None)

rt,ct = template.shape
rtest,ctest = testSheet.shape

df = pd.DataFrame(columns=['Cell_Location','BaseTemplate_Value','CurrentFile_Value'])

for rowNo in range(max(rt,rtest)):
  for colNo in range(max(ct,ctest)):
    # Fetching the template value at a cell
    try:
        template_val = template.iloc[rowNo,colNo]
    except:
        template_val = np.nan

    # Fetching the testsheet value at a cell
    try:
        testSheet_val = testSheet.iloc[rowNo,colNo]
    except:
        testSheet_val = np.nan

    # Comparing the values
    if (str(template_val)!=str(testSheet_val)):
        cell = xl_rowcol_to_cell(rowNo, colNo)
        dfTemp = pd.DataFrame([[cell,template_val,testSheet_val]],
                              columns=['Cell_Location','BaseTemplate_Value','CurrentFile_Value'])
        df = df.append(dfTemp)
        print(df)