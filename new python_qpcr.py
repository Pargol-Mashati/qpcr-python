#clean and improved code
import pandas as pd

import os

filename = "250324   myc target new genes_20250326_104144_Results_20250326 130821.csv"
df = pd.read_csv(filename, skiprows=21, nrows=54 )
print(df.head())
print(df.columns)
df= df[["Sample", "Target", "Cq"]]
print(df)

import numpy as np 
df["Cq"]= df["Cq"].replace("Undetermined", np.nan)
print(df)
df= df.dropna()
print(df)


ref_cq=df[df["Target"]== "GAPDH"].groupby("Sample")["Cq"].mean()
print(ref_cq)

df["dCT"]= df["Cq"]- df["Sample"].map(ref_cq)
print(df["dCT"])

df["expression"]=2 ** (-df["dCT"])
print(df["expression"])


df["average"]= df.groupby(["Sample", "Target"])["expression"].transform("mean")

print(df["average"])


NT_average= df[df["Sample"]== "NT"].groupby("Target")["average"].mean()


df.loc[df["Sample"].isin(["20", "40"]),"normalized"]=df.loc[df["Sample"].isin(["20", "40"]), "average"]/df.loc[df["Sample"].isin(["20","40"]), "Target"].map(NT_average)
print(df["Sample"].unique()) #make sure the Sample items are strings or integers otherwise you might get empty index

print(df[df["normalized"].notna()][["Sample", "Target", "average", "normalized"]])

df.to_excel("250326_python_qpcr_results.xlsx", index=False)
