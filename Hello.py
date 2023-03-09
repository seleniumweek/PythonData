import array as ar
import module as md
import pandas as pd
from lxml.html import fromstring
import lxml.html as PARSER

'''data = open('example.html').read()
root = PARSER.fromstring(data)

for ele in root.getiterator():
    if ele.tag == "td":
          print('hi')

alldata = md.readHTMLDocument("C:\\Users\\admin\\Desktop\\Htmlfile1.html","C:\\Users\\admin\\Desktop\\Htmlfile2.html")
md.ConvertDocToHtml("C:\\Users\\admin\\Desktop\\Wordfile2.docx","C:\\Users\\admin\\Desktop\\Htmlfile2.html")'''

sheet1 = pd.read_excel('C:\\Users\\admin\\Desktop\\Book1.xlsx')
sheet2 = pd.read_excel('C:\\Users\\admin\\Desktop\\Book2.xlsx')

'''sheet1 = pd.read_excel(r'Book1.xlsx')
sheet2 = pd.read_excel(r'Book2.xlsx')'''
  
# Iterating the Columns Names of both Sheets
for i,j in zip(sheet1,sheet2):
     
    # Creating empty lists to append the columns values    
    a,b =[],[]
  
    # Iterating the columns values
    for m, n in zip(sheet1[i],sheet2[j]):
  
        # Appending values in lists
        a.append(m)
        b.append(n)
  
    # Iterating the list's values and comparing them
    for m, n in zip(range(len(a)), range(len(b))):
        if a[m] != b[n]:
            print('Column name : \'{}\' and Row Number : {}'.format(i,m))
    rowcount = sheet1.shape[0]
    for i in sheet2.itertuples():
        print(list(i[1:]))



