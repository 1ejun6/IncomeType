# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:32:11 2021

@author: jun
"""

import csv 
from tabulate import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

with open('Proj10_data.csv', newline='' ) as Proj10_data:
    projdata= csv.reader(Proj10_data)
    
    bigdata= [row for row in projdata] #bigdata= entire data
    category= bigdata.pop(0) #category= Row: Year, Dividends, Interest, Other Types, Rent, Royalties, Trade Income
    maindata= [list(map(int, row)) for row in bigdata]#maindata= integer main value by (12 row) Year
    years= [row.pop(0) for row in maindata]#years= 2007- 2018
    rowdata= [list(dt) for dt in zip(*maindata)]#rowdata= rows into columns by (6 row) Dividends, Interest, Other Types, Rent, Royalties, Trade Income 

def dispMenu():
#tuple() can be called as list [] 
#tabulate call list so it would print the whole str, if called with () it would print each word with the sentence
    c1=('Please choose option')
    c2=('\tA - Display all Singapore Companies Income type for 2014.') 
    c3=('\tB - Category selected would display its Mean value from 2011-2017 And display Maximum and Minimum values along with the Years it ocurred on.')
    c4=('\tC - Category selected would display its Mean value along With the values that fall within 20% of the Mean and the Years in which they occurred.') 
    c5=('\tD - A graph of Trade Income,Total Income + Total Income VS Years And A bar graph Dividends + Interest VS Years') 
    c6=('\tQ - Exit the program.') 
    print(tb([[c1],[c2],[c3],[c4],[c5],[c6]], tablefmt='grid' ))

#extra functions
def miniMenu():
    cat1=[1,2,3,4,5,6]
    print(tb([category[1:7]], headers=cat1 , tablefmt='grid' ))

def empty():
    print('\n')
    
def cuteCat():
    print('''
              ∧＿∧
              （｡･ω･｡)つ━☆・*。
             ⊂　　 ノ 　　　・゜
              しーＪ　　　°。+ * 。
                         .・゜
                       ゜｡ﾟﾟ･｡･ﾟﾟ。 ･ﾟ  ･ﾟ  ･ﾟ  ･ﾟ  ･ﾟ  
                     。　  ｡ﾟ  ﾟ  Thank you!!　･ﾟ   ｡ﾟ 
                            ･ﾟ  ･ﾟ  ･ﾟ  ･ﾟ  ･ﾟ  ･ﾟ  
                                    ･ﾟ  
              
              
              ''')

def dispYear2014():
    print('☆ Singapore Companies Income type for 2014 are ☆')
    print(tb([bigdata[7]], headers=category, tablefmt='grid' ))


def mmmCategory():
    choice= 0
    guess= True
    mainval=typ=maxval=minval=ix=maxindex=minindex=p1=p2=0 
    while guess:
        miniMenu()
        choice=int(input('☆ Please select option 1-6: '))
    
        if choice== 1:
            mainval= rowdata[0][4:]
            typ=category[1]  
            selyear= years[4:]
            guess= False
            
        elif choice== 2:
            mainval= rowdata[1][4:]
            typ=category[2]
            selyear= years[4:]
            guess= False
            
        elif choice== 3:
            mainval= rowdata[2][4:]
            typ=category[3]
            selyear= years[4:]
            guess= False
            
        elif choice== 4:
            mainval= rowdata[3][4:]
            typ=category[4]
            selyear= years[4:]
            guess= False
            
        elif choice== 5:
            mainval= rowdata[4][4:]
            typ=category[5]
            selyear= years[4:]
            guess= False
            
        elif choice== 6:
            mainval= rowdata[5][4:]
            typ=category[6]
            selyear= years[4:]
            guess= False
            
        else: 
           
            print('☆ Invalid selection. Please select options 1-6 again! ☆')
            empty()
            continue
            
        maxval=max(mainval)
        minval=min(mainval)
        total=sum(mainval)
        avg=total/len(mainval)
  
        for ix in range(len(mainval)):#for loop iterates through the row number by ix
            if mainval[ix]== maxval:#if loop equilate mainval with the row number == maxval
                maxindex=selyear[ix]#maxindex= selyear[ix] index with the row number 
            elif mainval[ix]== minval:
                 minindex=selyear[ix]#minindex= selyear[ix] index with the row number 
            
        p1=(f'☆ The {typ} Mean value for 2011-2017 is {avg:.2f} ☆')
        p2=(f'☆ The 2011-2017 {typ} Max value is {maxval} on {maxindex} & Min value is {minval} on {minindex} ☆')
        print(tb([[p1],[p2]], tablefmt='grid' ))
        
        
def meanTwenty():
    choice= 0
    guess= True
    mainval=typ=total=0
    while guess:
        miniMenu()
        choice=int(input('☆ Please select option 1-6: '))
        print()
        
        if choice== 1:
            mainval= rowdata[0]
            typ=category[1]  
            guess= False
            
        elif choice== 2:
            mainval= rowdata[1]
            typ=category[2]
            guess= False
            
        elif choice== 3:
            mainval= rowdata[2]
            typ=category[3]
            guess= False
            
        elif choice== 4:
            mainval= rowdata[3]
            typ=category[4]
            guess= False
            
        elif choice== 5:
            mainval= rowdata[4]
            typ=category[5]
            guess= False
            
        elif choice== 6:
            mainval= rowdata[5]
            typ=category[6]
            guess= False
            
        else: 
            print('☆ Invalid selection. Please select options 1-6 again!☆')
            continue
        
        total= sum(mainval)
        avg= total/len(mainval)  
        matt= []
        yearmatt= []
            
        for a in range(len(mainval)):#a= entire list 
            percentage= (mainval[a]/avg)*100 
            if 120> percentage > 80:
                matt.append(mainval[a])#append value of (mainval[a]) to the new list= matt
                yearmatt.append(years[a])#append value of (years[a]) to the new list= yearmatt
                
        print(f'☆ The {typ} Mean value for 2007-2018 is {avg:.2f} ☆')
        print('-'*52)
        print('These are the values that fall within 20% range of the Mean:')
        print(tb([yearmatt, matt], tablefmt='grid' ))
        
def GraphandBarchart():
    totaldata= []
    fatdata= (rowdata[5])
    for i in range(len(maindata)):
        total= sum(maindata[i])
        totaldata.append(total)
 
    figure(figsize=(8, 6), dpi=80)
    plt.plot(years, fatdata, label='Trade Income')
    plt.plot(years, totaldata, label='Total Income')
    plt.xlabel('years')
    plt.ylabel('Trade Income & Total Income')
    plt.grid(True)
    plt.title('Total Income + Total Income VS Years')  
    #define x frequency, y frequency
    plt.xticks(years)
    plt.yticks(totaldata+fatdata) 
    plt.legend() 
    plt.show()
    
    #bar graph
    #assign x axis as array of my length of year, create a list from 0-11 with no ,
    xpos= np.arange(len(years))
    #array-like option 
    #list of xsticks locations passing an empty list removes all xsticks
    plt.xticks(xpos, years)
    #xsticks defines the spacing along the x-axis
    plt.title('Dividends + Interest VS Years') 
    plt.xlabel('years')
    plt.ylabel('Dividends + Interest')
    plt.yticks(rowdata[0]+ rowdata[1])
    plt.grid(True)
    #spacing is 0.2, width depends base of my xpos spacing 
    plt.bar(xpos-0.2,rowdata[0], width=0.4, label="Dividends")
    plt.bar(xpos+0.2,rowdata[1], width=0.4,label="Interest")
    plt.legend()    
    plt.show()