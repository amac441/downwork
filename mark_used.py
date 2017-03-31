import pandas as pd
from MutiprocessDataframe import callfunction
import numpy as np

basefolder=r'C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\masterData'
print ("Calling MultiProcess")
resourceslist = callfunction(basefolder)
resourceslist.shape

#merge in used accounts
used_list=['2_24_sampele_75.csv','pretest_09-2.csv']

cols =['id','alreadyUsed']
dfused=pd.DataFrame(columns=cols)
for u in used_list:
    df=pd.read_csv(u)
    df['alreadyUsed']='T'
    df2=df[cols]
    dfused=dfused.append(df2)

df5=resourceslist.merge(url3,on=['id'],how="left")
