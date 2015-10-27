# -*- coding: utf-8 -*-
#n = int(raw_input())
#for i in range(0, n):
#    a, b = raw_input().split()
#    print(int(a) + int(b))

'''
https://www.hackerrank.com/tests/sample
5
1
2
3
4
5
result => 15

values_data = [4.0,1.0,2.0,3.0,4.0,5.0]
resultado =>19
media => 19 / 6

'''

def sum_array():
  
#n = int(raw_input())
#for i in range(0, n):
#    a, b = raw_input().split()
#    print(int(a) + int(b))  
  
     values_data = [4.0,1.0,2.0,3.0,4.0,5.0]
     #precisa sair =>
     #3.17 /  3.5
     #the code start here==>
     inputs = raw_input()
     inputs = inputs.replace("[","")
     inputs = inputs.replace("]","")
     inputs = map(float, inputs.split(","))
     len_input = len(inputs)
     mean_value = float(round((sum(inputs) / len(inputs)),2))
     mean_index1 = (len(inputs) / 2)
     mean_index2 = mean_index1 + 1
     median = float((inputs[mean_index1] + inputs[mean_index2]) / 2)
     print(mean_value,median)
     #mean=>
     #median=>
     
     
     #for i in range(0, inputs):
     #     print(i)       
     
     #print(float(raw_input()))
     
'''     
     for x in values_data:
         #import ipdb;ipdb.set_trace();
         mean = values_data[x]
         #count+= count
         print("result print=>");print(mean);
'''         
sum_array()







    
