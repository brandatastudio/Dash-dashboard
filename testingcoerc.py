#!/usr/bin/env python


import pandas as pd
import numpy as np

datapath = 'information regarding the project/googleplaystore.csv'


df =  pd.read_csv(datapath,sep = ',')

cols = ["Installs" , "Price" , "Size" ]
df[cols] = df[cols].apply(pd.to_numeric)

print(df.dtypes)
print(df[cols])
