import pandas as pd
import sys
import os

path="yearly/"
files=os.listdir(path)

df_list=[]

for f in files:
    data=pd.read_csv(path+f)
    data["Year"]=f[:4]
    df_list.append(data)  
  
appended_data=pd.concat(df_list)

appended_data.drop(['Unnamed: 0'],axis=1,inplace=True)

appended_data=appended_data.query("Pos != '0'")

appended_data.to_csv("Appended_FFL_data.csv",index=False)
print("Your Master CSV file has been created!")