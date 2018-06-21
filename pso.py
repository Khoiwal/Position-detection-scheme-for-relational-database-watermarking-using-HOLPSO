# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:44:02 2017

@author: Jagpreet Singh
"""
import numpy as num
import random as rand
import matplotlib.pyplot as plt

#c1 = c2 = 2
#y = sphere function

def find_gbest(pbest):
    array = pbest**2
    x = num.sum(array,axis = 1)
    #print(x)
    #y = num.amin(x)
    #print(y)
    index = num.argmin(x)
    return index
    
def find_value(array):
    array = array**2
    x = num.sum(array,axis = 1)
    #y = num.min(x)
    #print(x)
    return x

def find_pbest(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest):
    array1 = num.copy(position_vector**2)
    array2 = num.copy(pbest**2)
    x1 = num.sum(array1,axis=1)
    x2 = num.sum(array2,axis=1)
    for i in range(0,number_of_particles):
        if x2[i]>x1[i]:
            pbest[i,:] = num.copy(position_vector[i,:])
    #print(x1,x2,pbest)
    return pbest


    
def vel_update(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest,w,gbest_arr):
    velocity_vector = num.round((w*velocity_vector + num.round(2*rand.random(),2)*(pbest-2*position_vector+gbest_arr)),2)
    return velocity_vector

def find_gen(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest,w):
    #print(position_vector)
    #print(value_pbest,index_pbest)
    pbest = find_pbest(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest)
    gbest = find_gbest(pbest)
    #print(pbest)
    #print(gbest)
    gbest_arr = num.zeros(shape = (number_of_particles,number_of_variables))
    for i in range(0,number_of_particles):
        gbest_arr[i,:] = num.copy(pbest[gbest,:])
        
    #print(gbest_arr[0,:])
    
    velocity_vector = vel_update(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest,w,gbest_arr) 
    position_vector = num.round((position_vector + velocity_vector),2)
    #plt.plot(find_value(position_vector),'r-',label='Last Gen')
    return position_vector,velocity_vector,pbest


nop = input("Please mention the number of particles \n")
noi = input("Please mention the number of iterations \n")


number_of_particles = int(nop)
number_of_variables = 3
number_of_iterations = int(noi)

position_vector = (num.random.rand(number_of_particles,number_of_variables)-0.5)*10.24
velocity_vector = (num.random.rand(number_of_particles,number_of_variables)-0.5)*10.24
position_vector = num.round(position_vector,2)
velocity_vector = num.round(velocity_vector,2)
pbest = num.copy(position_vector)
        
#print(position_vector)    
#print()    
#print(find_value(position_vector))
#print()
#print(gbest)
#print()
#print(gbest_arr)

plt.plot(find_value(position_vector),'r-',label='1st Gen')
#print(position_vector)
#print(pbest)
for i in range(0,number_of_iterations):
    #print(i)
    w = 0.2
    position_vector,velocity_vector,pbest = find_gen(position_vector,velocity_vector,number_of_particles,number_of_variables,pbest,w)
plt.plot(find_value(position_vector),'b-',label='Last Gen')
plt.plot([-0.01])
plt.legend()
plt.show