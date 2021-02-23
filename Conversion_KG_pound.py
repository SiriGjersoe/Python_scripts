#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:15:22 2021

@author: Siri Gjersøe
"""

# a script with a promt which converts values from KG to pounds and other way around
# Formula: m(lb) = m(kg) / 0.45359237
# Formula: m(kg) = m(lb) × 0.45359237

def convKG_to_pound():
    x = input("Enter weight unit (pound or kg) to convert FROM: ")
    y = float(input("Enter value: "))
    if type(y) is int:
        print("derp")
    if x == 'kg':
        amountKg = y / 0.45359237
        print(y, 'kg', 'equals', format(amountKg, '.2f'), 'pounds')
    elif x == 'pound':
        amountP = y * 0.45359237
        print(y, 'pounds', 'equals', format(amountP, '.2f'), 'kg')
    else:
        print('Please choose either kg or pound')
        restart = input('Do you want to try again?')
        if restart == 'yes':
        # go to the top
            convKG_to_pound()
            return 0
        elif restart == 'y':
            # go to the top
            convKG_to_pound()
            return 0
        else:
            print('Fine then, bye!')
            return
            
convKG_to_pound()    
            
