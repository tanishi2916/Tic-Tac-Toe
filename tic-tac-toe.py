# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:17:04 2020

@author: Tanishi
"""


x={'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
arr=[]
for i in x:
    arr.append(i)
    
def printb(x):
    print(x['1']+'|'+x['2']+'|'+x['3'])
    print("-+-+-")
    print(x['4']+'|'+x['5']+'|'+x['6'])
    print("-+-+-")
    print(x['7']+'|'+x['8']+'|'+x['9'])
n=0

def check(x):
    if ((x['1']==x['2']==x['3'])and(x['1']!=' ')and(x['2']!=' ')and(x['3']!=' ')):
        return 1
    elif ((x['4']==x['5']==x['6'])and(x['4']!=' ')and(x['5']!=' ')and(x['6']!=' ')):
        return 1
    elif ((x['7']==x['8']==x['9'])and(x['9']!=' ')and(x['8']!=' ')and(x['7']!=' ')):
        return 1
    elif((x['1']==x['4']==x['7'])and(x['1']!=' ')and(x['4']!=' ')and(x['7']!=' ')):
        return 1
    elif ((x['2']==x['5']==x['8'])and(x['2']!=' ')and(x['5']!=' ')and(x['8']!=' ')):
        return 1
    elif ((x['3']==x['6']==x['9'])and(x['3']!=' ')and(x['6']!=' ')and(x['9']!=' ')):
        return 1
    elif ((x['5']==x['7']==x['3'])and(x['5']!=' ')and(x['7']!=' ')and(x['3']!=' ')):
        return 1
    elif ((x['1']==x['5']==x['9'])and(x['1']!=' ')and(x['5']!=' ')and(x['9']!=' ')):
        return 1
    
print(x['1']+'|'+x['2']+'|'+x['3'])
print("-+-+-")
print(x['4']+'|'+x['5']+'|'+x['6'])
print("-+-+-")
print(x['7']+'|'+x['8']+'|'+x['9'])  
s1=input("enter player1 name")
s2=input("enter player2 name") 
for i in range(9):
    
    n=1-n
    
    if(n):
        pos=input(s1+" p1 enter the position")
        if (x[pos] == ' '):
            x[pos]='o'
            c=check(x)
            if c==1:
                print(s1+" player1 wins")
                break
        else:
            n=0
            print("ENTER THE CORRECT PLACE")
            print()
    else:
        pos=input(s2+" p2 enter the position")
        if (x[pos] == ' '):
            x[pos]='x'
            c2=check(x)
            if c2==1:
                print(s2+" player2 wins")
                break
        else:
            n=1
            print("ENTER THE CORRECT PLACE")
            print()
            
            
    printb(x)
    if i == 8:
        print("nobody wins")
print("**GAME OVER**")

    
    
    
        
            