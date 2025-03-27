import pandas as pd

import os

filename = "250114 Beta catenin and myc target genes 4th replicate_Copy_Copy_20250114_130802_Standard Curve Result_20250114 153522.xlsx"  # ← change this to match your actual file name!
df = pd.read_excel(filename, skiprows=21, nrows=54 )
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

df["Sample"].isin([20, 40])
df[df["Sample"].isin([20, 40])]

df.loc[df["Sample"].isin([20, 40]),"normalized"]=df.loc[df["Sample"].isin([20, 40]), "average"]/df.loc[df["Sample"].isin([20,40]), "Target"].map(NT_average)

print(df[df["normalized"].notna()][["Sample", "Target", "average", "normalized"]])

df.to_excel("python_qpcr_finally.xlsx", index=False)
