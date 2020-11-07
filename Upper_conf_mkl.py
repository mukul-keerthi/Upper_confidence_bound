# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:31:38 2020
Upper confidence bound (UCB) algorithm
@author: Mukul
"""

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing UCB
N = 10000 #Number of users
d = 10 #Number of ads
ads_selected = []
numbers_of_selection = [0] * d #Empty list containing 10 zeros Ni(n) 
sum_of_rewards = [0] * d #Contains sum of rewards of each ad initialized to zero
total_rewards = 0 #Initialized to zero
#Iterative loop to loop through number of users
for n in range(0, N):
    #Initialize the variables
    ad = 0 
    max_upper_bound = 0
for i in range (0, d):   
    if (numbers_of_selection[i] > 0): #Implementing step 1
        average_reward = sum_of_rewards[i] / numbers_of_selection[i] #Average reward
        delta_i = math.sqrt(3/2 * math.log(n+1)/ numbers_of_selection[i]) #Step 2 - n+1 because n starts at 0
    #Step 3 - Select ad i which has the maximum UCB
        upper_bound = average_reward + delta_i
    else:
  #Set the denominator to a very high value
        numbers_of_selection[i] = 1e400 #Close to infinity value
        if (upper_bound > max_upper_bound):
            max_upper_bound = upper_bound #Update the max upper bound
        #To select the ad with the max upper bound select index 'i'
            ad = i
    #Append to the ad selected list
    ads_selected.append(ad)
    numbers_of_selection += 1
    reward = dataset.values[n, i] #The corresponding row and coloumn index
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward #Add the corresponding row and coloumn index   
    total_rewards = total_rewards + reward
#Visualizing the result     
    plt.hist(ads_selected)
    plt.title ('Ad selection Histogram')
    plt.xlabel('Ads')
    plt.ylabel('Number of times each ad was selected')
    plt.show()
     


