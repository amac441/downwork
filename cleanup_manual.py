import pandas as pd
import numpy as np
import sys

# rs=pd.read_csv(r"C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\manual_people\2017_4_24_andy.csv",encoding = "ISO-8859-1", delimiter=";",error_bad_lines=False)
file=sys.argv[2]
rs=pd.read_csv(file,encoding = "ISO-8859-1", delimiter=";",error_bad_lines=False)

if sys.argv[1]='cleanup':

    df2=rs.drop_duplicates()
    print(shape.rs)
    print(shape.df2)

    df2.head()
    renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
    df2=df2.rename(columns=renamecolumns)
    df2['profileID']=df2['id'].str.split('~').str[1]
    df2.to_csv('manual_$s.csv' % date)

if sys.argv[1]=='clean_and_used':

    used_list=['Batch_1_159.csv','pilot04062017.csv','2017_4_6_manual_details.csv']

    cols =['id','alreadyUsed']
    dfused=pd.DataFrame(columns=cols)
    for u in used_list:
        df=pd.read_csv(u)
        df['alreadyUsed']='T'
        df2=df[cols]
        dfused=dfused.append(df2)

    final=newdf.merge(dfused,on=['id'],how="left")
    final.to_csv("manual_people_4_24.csv")