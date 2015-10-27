# -*- coding: utf-8 -*-

'''

examlpes of data input()
[
{"date":"20150929","histogram":[4176,924,254,269,213,249,296,209,91,29,21,12,6,5,0,0,0,0,0,0]},
{"date":"20150930","histogram":[4690,951,250,233,197,185,250,236,97,44,33,14,8,2,2,0,0,0,0,0]},
{"date":"20151001","histogram":[59,250,192,146,157,319,748,996,1080,741,352,176,109,76,10,2,0,0,0,0]},
]

'[{"date":"20150929","histogram":[4176,924,254,269,213,249,296,209,91,29,21,12,6,5,0,0,0,0,0,0]},{"date":"20150930","histogram":[4690,951,250,233,197,185,250,236,97,44,33,14,8,2,2,0,0,0,0,0]},{"date":"20151001","histogram":[59,250,192,146,157,319,748,996,1080,741,352,176,109,76,10,2,0,0,0,0]}]'
[{"date":"20150929","histogram":[4176,924,254,269,213,249,296,209,91,29,21,12,6,5,0,0,0,0,0,0]},{"date":"20150930","histogram":[4690,951,250,233,197,185,250,236,97,44,33,14,8,2,2,0,0,0,0,0]},{"date":"20151001","histogram":[59,250,192,146,157,319,748,996,1080,741,352,176,109,76,10,2,0,0,0,0]}]
resp = json.loads('[{"date":"20150929","histogram":[4176,924,254,269,213,249,296,209,91,29,21,12,6,5,0,0,0,0,0,0]},{"date":"20150930","histogram":[4690,951,250,233,197,185,250,236,97,44,33,14,8,2,2,0,0,0,0,0]},{"date":"20151001","histogram":[59,250,192,146,157,319,748,996,1080,741,352,176,109,76,10,2,0,0,0,0]}]')

'''

import json

def sum_array():
     
     #precisa sair =>
     #20151001
     #the code start here==>
     inputs = raw_input()
     json_data = json.loads(inputs)
     regression0, regression1, regression2 = ((sum(json_data[0]['histogram'])) / 2), ((sum(json_data[1]['histogram'])) / 2), ((sum(json_data[2]['histogram'])) / 2)

     if ( (regression0 > regression1) or (regression0 > regression2) ):
         regress = 0
     elif ( (regression1 > regression0) or (regression1 > regression2) ):
         regress = 1       
     elif ( (regression2 > regression1 ) or ( regression2 > regression0) ):       
         regress = 2
     print(json_data[regress]['date'])

sum_array()







    
