import numbers
import numpy as np
import operator
import random
import pickle
import math
import pandas as pd

def BNL(ls, N):
    #input parameters
    #ls: a list with the objects,
    #N: the number of dimensions

    #output
    #window: a list containing the ids of the skyline objects

    #window for comparing
    window = []

    #place the first id in the window
    window.append(0)

    for idx in range(1, len(ls)):
        dom = False
        #compare each object with the window
        for witem in window:
            if comp_k(ls[witem], ls[idx], N, N):
                # object is dominated by the window
                dom = True

        if dom == False:
            #append object to window
            window.append(idx)

            #delete all the objects in the window dominated by element
            window = [x for x in window if not comp_k(ls[idx], ls[x], N, N)]

    return window

def comp_k(a, b, K, N):
#returns True if a k-dominates b
#returns False otherwise
    counter = 0
    res=[]
    for aitem, bitem in zip(a[1:], b[1:]):
        if (counter == 0):
            aitem = -aitem
            bitem = -bitem
        counter = counter+1
        res.append(compare(aitem,bitem))
    dict = count(res)

    if dict['EQ']==N:
        return False
    c = dict['GR']+dict['EQ']
    if c==N:
        return True
    return False

def compare(a,b):
    #compares a and b and returns 'GR','LS','EQ'
        if a>b:
            return 'GR'
        elif a<b:
            return 'LS'
        else:
            return 'EQ'

def count(ls):
    #takes a list of 'LS', 'GR', 'EQ'
    #and returns a dictionary with the values
    ctEQ = ctGR = ctLS = 0
    for item in ls:
        if item == 'LS':
            ctLS = ctLS+1
        elif item == 'GR':
            ctGR = ctGR+1
        elif item == 'EQ':
            ctEQ = ctEQ+1
    dict = {'LS':ctLS, 'GR':ctGR, 'EQ':ctEQ}
    return dict