import pandas as pd
import numpy as np
import sys, os

# rs=pd.read_csv(r"C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\manual_people\2017_4_24_andy.csv",encoding = "ISO-8859-1", delimiter=";",error_bad_lines=False)

def cleanup(rs):

    print ("File Size"+str(rs.shape))

    df2=rs.drop_duplicates()
    # print(shape.rs)
    # print(shape.df2)

    print(df2.iloc[0])
    # renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
    # df2=df2.rename(columns=renamecolumns)
    # df2['profileID']=df2['id'].str.split('~').str[1]
    try:
        renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
        df2=df2.rename(columns=renamecolumns)
        df2['profileID']=df2['id'].str.split('~').str[1]
    except:
        print "Column headers werent as expected"

    # df2.to_csv('manual_$s.csv' % date)
    #

    print ("Renamed Columns")
    return df2

def markused(rd):

    print ("Marking Used from files in /used_people folder")
    used_list=os.listdir('used_people')

    cols =['id','alreadyUsed']
    dfused=pd.DataFrame(columns=cols)
    for u in used_list:
        df=pd.read_csv('used_people/'+u)
        df['alreadyUsed']='T'
        df2=df[cols]
        dfused=dfused.append(df2)

    final=rd.merge(dfused,on=['id'],how="left")
    # final.to_csv("manual_people_4_24.csv")
    return final

file=sys.argv[2]

if sys.argv[1]=='cleanup':
    rs=pd.read_csv(file,encoding = "ISO-8859-1",error_bad_lines=False)
    rd=cleanup(rs)

if sys.argv[1]=='used':

    rs=pd.read_csv(file,encoding = "ISO-8859-1",error_bad_lines=False)
    rs=cleanup(rs)
    rd=markused(rs)

print ("File Size" + str(rd.shape))
print ("Dropping Dupliates")
final2=rd.drop_duplicates(subset='id')
print ("File Size" + str(final2.shape))
final2.to_csv("cleaned_"+file)