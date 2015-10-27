# -*- coding: utf-8 -*-
'''
====>
Singapore
Bangkok
Singapore
Bangkok
Singapore

'''

def sum_array():
  search = []
  valid = False
  counter_search = 0
  
  while not valid:
    
    inputs = raw_input()
    search.append(inputs)
    counter_search += 1
    max_search = 0
    max_searched = 0
    
    if counter_search > 5:
        valid = True
      
        for i in search:
	    if search.count(i) > max_search:
	        max_search = search.count(i)
	        max_searched = i 
    print(max_searched)          
        
      
#  len_search = len(search.count)

  
#search[search.count(i)]
sum_array()
