# from datetime import datetime
# import time
# import requests
# url = 'http://10.100.230.95:8161/api/message/MESMSG'
# ts = time.time()
# st = datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S.000')
# st2 = datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S.005')


# Tool=input("What is the Tool ID?:").upper()
# while True:
#     Tank=input("What tank needs to be updated?").upper()

#     if Tank == "T1": 
#         SV = "11"
#     else: 
#         if Tank == "T2": SV = "12"
#         else: 
#             if Tank == "T3": SV = "13"
#             else: 
#                 if Tank == "T4": SV = "14"
#                 else: print("Incorrect Tank Name Format.  Use T1,T2,T3 or T4")
#     Count=input("What is the correct count?")

#     msg = "PARAMDATA HDR=(DCP,DCP,"+Tool+") TIMESTAMP="+st+" EQPID="+Tool+" GROUPID=1 PARAM_VALUES={"+SV+"00=PLAYGROUND_RESET^"+Tank+"_Counter_Value="+Count+"}"
#     print(msg)
#     requests.post(url, data={'type':'topic','body':msg})

#     # deb206 t1


from datetime import datetime
import time
import requests
url = 'http://10.100.230.95:8161/api/message/MESMSG'
ts = time.time()
st = datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S.000')
st2 = datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S.005')


Tool=input("What is the Tool ID?:").upper()
while True:
    Tank=input("What tank needs to be updated?").upper()

    if Tank == "T1": 
        SV = "11"
    else: 
        if Tank == "T2": SV = "12"
        else: 
            if Tank == "T3": SV = "13"
            else: 
                if Tank == "T4": SV = "14"
                else: print("Incorrect Tank Name Format.  Use T1,T2,T3 or T4")
    Count=input("What is the correct count?")

    msg = "PARAMDATA HDR=(DCP,DCP,"+Tool+") TIMESTAMP="+st+" EQPID="+Tool+" GROUPID=1 PARAM_VALUES={"+SV+"00=RESET^"+Tank+"_Counter_Value="+Count+"}"
    print(msg)
    requests.post(url, data={'type':'topic','body':msg})

    # deb206 t1
