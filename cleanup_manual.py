import pandas as pd
import numpy as np
import sys

# rs=pd.read_csv(r"C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\manual_people\2017_4_24_andy.csv",encoding = "ISO-8859-1", delimiter=";",error_bad_lines=False)

def cleanup(rs):

    df2=rs.drop_duplicates()
    print(shape.rs)
    print(shape.df2)

    df2.head()
    try:
        renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
        df2=df2.rename(columns=renamecolumns)
        df2['profileID']=df2['id'].str.split('~').str[1]
    except:
        print "Column headers werent as expected"

    # df2.to_csv('manual_$s.csv' % date)
    #
    return df2

def markused(rd):

    used_list=os.listdir('used_people')

    cols =['id','alreadyUsed']
    dfused=pd.DataFrame(columns=cols)
    for u in used_list:
        df=pd.read_csv('used_people/'+u)
        df['alreadyUsed']='T'
        df2=df[cols]
        dfused=dfused.append(df2)

    final=rd.merge(dfused,on=['id'],how="left")
    final.to_csv("manual_people_4_24.csv")

file=sys.argv[2]
rs=pd.read_csv(file,encoding = "ISO-8859-1", delimiter=";",error_bad_lines=False)

if sys.argv[1]=='cleanup':

    rd=cleanup(rs)

if sys.argv[1]=='used':

    rs=cleanup(rs)
    rd=markused(rs)

final2=rd.drop_duplicates(subset='id')
final2.to_csv("clean_"+file)
