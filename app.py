import pandas as pd
import numpy as np
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydb"
)
excel_file = 'reportListaMovimentiXls.xls'



report = pd.read_excel(excel_file)
balanceDate=report.iloc[1]['A']
balanceTotal=report.iloc[1]['C']
rowIBAN=report.iloc[0]['A']
print('IBAN: '+ rowIBAN)
print('balanceDate: '+ balanceDate)
print('balanceTotal: '+ str(balanceTotal))

'''
for index,row in report.iterrows():
    print(row['A'])
'''
'''
for index,row in report.iterrows():
    print(row['A'])
'''
report=report.rename(columns={'A':'DATA CONTABILE','B':'DATA VALUTA','C':'IMPORTO','D':'DESCRIZIONE'})

jsoned = report.to_json(orient='records')
jsonedJSON = json.loads(jsoned)
'''
jsonedJSON.append({'IBAN':rowIBAN, 'balanceTotal': balanceTotal, 'balanceDate':balanceDate})
'''
print(jsonedJSON)

with open('data.json','w+') as outfile:
    outfile.write(json.dumps(jsonedJSON))

val = []
for obj in jsonedJSON:
    val.append((obj['IMPORTO'],obj['DESCRIZIONE']))

mycursor = mydb.cursor()
sql = "INSERT INTO movements (importo, descrizione) VALUES (%s, %s)"

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")