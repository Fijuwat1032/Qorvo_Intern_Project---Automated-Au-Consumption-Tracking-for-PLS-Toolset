import time
from datetime import datetime
import requests
url = 'http://10.100.230.95:8161/api/message/MESMSG'
ts = time.time()
st = datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S.000')
 
 
Tool=input("What is the Tool ID?:").upper()
Cell=input("What cell needs to be updated?").upper()
if Cell == "A": 
    SV = "1104"
else: 
    if Cell == "B": SV = "1304"
    else: print("Incorrect Cell Name Format.  Use A or B")
Count=input("What is the correct count?")
 
msg = "PARAMDATA HDR=(DCP,DCP,"+Tool+") TIMESTAMP="+st+" EQPID="+Tool+" GROUPID=1 PARAM_VALUES={"+SV+"="+Cell+"Playground_Reset^"+Cell+"_Counter_Value="+Count+"}"
print(msg)
requests.post(url, data={'type':'topic','body':msg})


#test case pls203, a, random numbers 
