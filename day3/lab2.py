import csv
import pandas as pd

f1=open("lab2.csv", "w")
f1.write("10 20 30 40\n")
f1.write("50 60 70 80\n")
f1.write("25 35 45 55\n")
f1.write("44 54 64 74\n")
f1.write("22 32 42 52\n")
f1.write("46 56 66 76\n")
f1.close()

df= pd.read_csv("lab2.csv")
print(df)