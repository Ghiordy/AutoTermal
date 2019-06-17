# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:36:27 2019

@author: Ghiordy F. Contreras
"""


state = ['set','run']
currentState = state[0]

def transient():
    print('Starting AutoTermal...')
    checker = False
    attempts = 1000
    while(not(checker)):
        checker = startMQTT()
        attempts = attempts - 1
        if attempts == 1:
            print('Number of attempts covered')
            break
    return checker

def steady():
    #Ghiordy Contreras
    pass

def machine():
    checker = transient()
    if checker:
        currentState = state[1]
    else:
        currentState = state[0]
    return currentState

def central():
    currentState = machine()
    

