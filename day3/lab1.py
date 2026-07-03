import csv
import pandas as pd

f1= open("lab1.csv", "w")
f1.write('''num1,num2
         10,20
         30,40
         50,60
         70,80
         80,90
         ''')
f1.close()

df= pd.read_csv("lab1.csv")
print(df)
df.insert(2, "sum", df["num1"]+df["num2"])
print(df)
df.to_csv("lab1.csv", index= False)