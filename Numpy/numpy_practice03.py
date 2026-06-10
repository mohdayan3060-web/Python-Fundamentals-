import pandas as pd
import numpy as np
#this is ways to work with csv file and using numpy and pandas 

olympics_data=pd.read_csv(r'C:\Users\hp\Python fundamentals\Numpy\olympics_cleaned_v4.csv') 
ID=olympics_data['ID'].to_numpy()
Name=olympics_data['Name'].to_numpy()
Sex=olympics_data['Sex'].to_numpy()
Age=olympics_data['Age'].to_numpy()
Height=olympics_data['Height'].to_numpy()
Weight=olympics_data['Weight'].to_numpy()



print(type(ID))
