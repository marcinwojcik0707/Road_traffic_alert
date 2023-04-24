import pandas as pd
from datetime import date
df = pd.read_excel('Grafik_2023.xlsx')
df = df.drop(index=[0], columns='Unnamed: 0')
df3 = df.rename(columns={'GRAFIK':'Date','Unnamed: 2':'Day_of_the_week'})
df3['Date']=pd.to_datetime(df3['Date']).dt.date
df3['Date']=pd.to_datetime(df3['Date']).dt.normalize()
df2=df3[(df3['Date']) == str(date.today())]
df2=df2['MWó']
print(df2.iloc[0])