import pandas as pd
import datetime
import json
from flask import *
app=Flask(__name__)
@app.route('/',methods=['Get'])
def birthday():
    df= pd.read_csv("data.csv",encoding="latin")
    ls=list()
    st=''
    x = datetime.datetime.now()
    month=x.strftime("%b")
    day=x.strftime("%d")
    var = day+"-"+month
    for i in range(len(df['Celebrity'])):
        if(df['Birthday'][i]==var):
            if(st==''):
                st=st+df['Celebrity'][i]
            else:
                st=st+','+df['Celebrity'][i]         
    if(st==''):
        st="You are Unique"
    ls.append(st)
    jsonString = json.dumps(ls)
    return jsonString
if(__name__=='__main__'):
    app.run(port=7777)




