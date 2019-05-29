#!/usr/bin/env python


import pandas as pd
import numpy as np

datapath = 'information regarding the project/googleplaystore.csv'


dataset =  pd.read_csv(datapath,sep = ',')

columnamesopt = []
for i in dataset.columns.values:
    columnamesopt.append({'label' : str(i) , 'value' : str(i) })

print(dataset.dtypes)
print(dataset)
