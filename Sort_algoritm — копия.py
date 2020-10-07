# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:31:59 2019

@author: Y
"""
def bubble_sort(arg):
    """original bubble sorting algoritm 
    \n\r arg:lists,arrays 
    \n\r returns sorted object"""
    if type(arg) != list:
        print("wrong type")
    else:
        i = 1
        while(i<=len(arg)-1):
            k = 0
            while(k<=len(arg)-i-1):
                if arg[k]>arg[k+1]:
                    arg[k],arg[k+1] = arg[k+1],arg[k]
                k = k+1
            i =i + 1
        return arg

def bubble_sort_plus(arg):
    """modificated bubble sorting algoritm
    \n\r this realisation checks is objects sorted and can 
    \n\r return answer earlier than original algoritm
    \n\r arg:lists,arrays 
    \n\r returns sorted object"""
    if type(arg) != list:
        print("wrong type")
    else:
        i = 1

        while(i<=len(arg)-1):
            k = 0
            f=0
            while(k<=len(arg)-i-1):
                if arg[k]>arg[k+1]:
                    arg[k],arg[k+1] = arg[k+1],arg[k]
                    f=1
                k = k+1
            if f==0:
                return arg
            else:
                i =i + 1
        return arg
        
def cocktail_sort(arg):
    
    left=0
    right=len(arg)-1
    while left<=right:
        for i in range(left,right,+1):
            if arg[i]>arg[i+1]:
                arg[i],arg[i+1] = arg[i+1],arg[i]
        right-=1
        for i in range(right,left,-1):
            if arg[i-1]>arg[i]:
                arg[i-1],arg[i] = arg[i],arg[i-1]
        left+=1
    return arg


def quicksort(arg):
    if len(arg)<=1:
        return arg
    else:
        #choice support element
        support=arg[len(arg)-1]
        #import random
        #support=random.choice(arg)
        low=[]
        medium=[]
        hight=[]
        for n in arg:
            if n<support:
                low.append(n)
            elif n==support:
                medium.append(n)
            else:
                hight.append(n)
        return quicksort(low)+medium+quicksort(hight)

def insert_sort(arg):
    for j in range(1,len(arg)):
        aim= arg[j]
        i=j-1
        while (i>=0 and arg[i]>aim):
            arg[i+1]=arg[i]
            i=i-1
        arg[i+1]=aim
    return arg
    
def gnome_sort(arg):
    i=1
    j=2
    while i < len(arg):
        if arg[i]>arg[i-1]:
            i=j
            j+=1
        else:
            arg[i-1],arg[i]=arg[i],arg[i-1]
            i-=1
            if i==0:
                i=j
                j+=1
    return arg
     
a=[3,1,5,8,1,0,4,6,6,7]
b=gnome_sort(a)
print(b)
    