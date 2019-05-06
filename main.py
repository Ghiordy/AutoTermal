# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 06:36:27 2019

@author: Ghiordy F. Contreras
"""

import RPi.GPIO as GPIO
import time
import numpy as np

class Main:
    """ This class emlate a main Mealy FSM module. """
    def __init__(self,currentState):
        """ Initialize states by default parameters """
        self._currentState = currentState
        
    @property
    def currentState(self):
        """ Gets or sets states of the main"""
        return self._currentSate
    
    @states.setter
    def states(self,state):
        if state in states:
            self._currentState()
        else:
            print('Not valid state')
            
    
        
        
        