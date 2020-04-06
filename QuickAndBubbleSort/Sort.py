# -*- coding: utf-8 -*-

import time
import random
import numpy as np

def Bubble(vec):
    
    swaped = True
    ret_vec = vec.copy()
    vec_size = len(vec)
    
    while(swaped):
        swaped = False
        i = 0
        j = 1
        while(vec_size>j):
            temp = 0
            
            if(ret_vec[i] > ret_vec[j]):
                temp = ret_vec[j]
                ret_vec[j] = ret_vec[i]
                ret_vec[i] = temp
                swaped = True
            
            i= i + 1
            j= j + 1
            
    
def QuickSort(vec, i, j, rand):
#    [4,3,6,2,1]
    if(i < j):
        par = QuickDivide(vec, i, j, rand)
        QuickSort(vec, i, par-1, rand)
        QuickSort(vec, par+1, j, rand)
        
        
def QuickDivide(vec, i, j, rand):
    t_i = i + 1
    t_j = j
    
    pivo = vec[random.randint(i,j)] if rand else vec[i]
    
    
    while(t_i<=t_j):
        
        if (vec[t_i] <= pivo) : 
            t_i = t_i+1 
        elif (vec[t_j] > pivo) :
            t_j = t_j-1
        elif (t_i <= t_j):
            aux = vec[t_i]
            vec[t_i] = vec[t_j]
            vec[t_j] = aux
            t_i = t_i + 1
            t_j = t_j - 1    
    
#    for p in range(i, j):
#        if vec[p] <= vec[pivo]:
#            t_i = t_i + 1
#            
#            aux = vec[t_i]
#            vec[t_i] = vec[p]
#            vec[p] = aux

    a = vec[i]
    vec[i] = vec[t_j]
    vec[t_j] = a
    
    return t_j
        


    

class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        self.stop_time = time.time()
        return self.stop_time

    def get_elapsed_time(self):
        return self.stop_time - self.start_time

        
def testAlgorithms(n):
    print("N;Algorithm;Seconds")
    wa = StopWatch()
        
    
    for i in n:
        vec = np.random.randint(999999, size=i)
        time = 0
        for _ in range(500):
            wa.start()
            Bubble(vec)
            wa.stop()
            time = time + wa.get_elapsed_time()
            
        print(i,';BubbleSort;',time)   
        
        time = 0
        for _ in range(500):
            wa.start()
            QuickSort(vec, 0, len(vec) - 1, rand = False)
            wa.stop()
            time = time + wa.get_elapsed_time()
            
        print(i,';QuickSortDefault;',time) 
        
        time = 0
        for _ in range(500):
            wa.start()
            QuickSort(vec, 0, len(vec) - 1, rand = True)
            wa.stop()
            time = time + wa.get_elapsed_time()
            
        print(i,';QuickSortRandom;',time) 
        
        
        
        