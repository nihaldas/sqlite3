import sqlite3 as sql
from sqlite3 import Error
import numpy as np 
import pandas as pd 
import sklearn 

con = sql.connect('mydatabase.db')
cursorObj = con.cursor()

result = cursorObj.execute('SELECT * FROM employees;')

columns = ['Id','Name','Salary','Department','Position','Date']

df1 = pd.DataFrame(columns=columns)


for r in result:
	arr = [] 
	for q in r: 
		arr.append(q)
	df1 = df1.append(dict(zip(df1.columns, arr)), ignore_index=True)
	
print(df1)
