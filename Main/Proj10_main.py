# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:03:51 2021

@author: jun
"""

import Proj10_module as module
bigdata= []

loop= True

while loop:
    module.dispMenu()
    sel= input('Please select A, B, C, D or Q: ')
    print()
    
    if sel == 'A' or sel =='a':
        module.dispYear2014()
        module.empty()
    
    elif sel== 'B' or sel == 'b':
        module.mmmCategory()
        module.empty()
    
    elif sel== 'C' or sel == 'c':   
        module.meanTwenty()
        module.empty()
        
    elif sel== 'D' or sel == 'd':
        module.GraphandBarchart()
        module.empty()
    
    elif sel == 'Q' or sel == 'q':
        module.cuteCat()
        loop=False
    
    else:
        print('Sorry invalid selection, Please Try again!')
