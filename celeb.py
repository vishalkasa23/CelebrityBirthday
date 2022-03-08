import pandas as pd
import datetime
import json
from flask import *
app=Flask(__name__)
@app.route('/',methods=['Get'])
def birthday():
    df= pd.read_csv("data.csv",encoding="latin")
    ls=list()
    x = datetime.datetime.now()
    month=x.strftime("%b")
    day=x.strftime("%d")
    var = day+"-"+month
    for i in range(len(df['Celebrity'])):
        if(df['Birthday'][i]==var):
            ls.append(df['Celebrity'][i])
    jsonString = json.dumps(ls)
    return jsonString
if(__name__=='__main__'):
    app.run(port=7777)




