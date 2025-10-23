# ...existing code...
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:15:22 2021
Modifoed on 23.10.25
@author: Siri Gjersøe
"""

# a script with a promt which converts values from KG to pounds and other way around
# Formula: m(lb) = m(kg) / 0.45359237
# Formula: m(kg) = m(lb) × 0.45359237

def convKG_to_pound():
    x = input("Enter weight unit (pound or kg) to convert FROM: ").strip().lower()
    try:
        y = float(input("Enter value: "))
    except ValueError:
        print("Invalid number!")
        return

    if isinstance(y, int):
        print("derp")
    if x == 'kg':
        amountKg = y / 0.45359237
        print(y, 'kg', 'equals', format(amountKg, '.2f'), 'pounds')
    elif x in ('pound', 'lb', 'lbs'):
        amountP = y * 0.45359237
        print(y, 'pounds', 'equals', format(amountP, '.2f'), 'kg')
    else:
        print('Please choose either kg or pound')

    restart = input('Do you want to try again? (y/n): ').strip().lower()
    if restart in ('yes', 'y'):
        convKG_to_pound()
        return 0
    else:
        print('Fine then, bye!')
        input('Press Enter to exit...')
        return

convKG_to_pound()
# ...existing code...