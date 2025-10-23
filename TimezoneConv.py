#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:37:19 2021

@author: Siri Gjersoe
"""

#My very first python script used to calculate time zones


#==============================================================================
#   To do: 
#    1. Add conditionals to outrule:
#       - decimals such as .69
#       - strings instead of numbers
#
#  elif time == (time, str):
#         print('Please use 24 h format')
#         restart = input('One more time? (yes/no)').lower()
#         if restart == "yes":
#             conv()
#             return 0
#==============================================================================
# ...existing code...
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a script with a promt which converts values from KG to pounds and other way around
# Formula: m(lb) = m(kg) / 0.45359237
# Formula: m(kg) = m(lb) × 0.45359237

# ...existing code...
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:37:19 2021

@author: Siri Gjersoe
"""

#My very first python script used to calculate time zones

#==============================================================================
#   To do: 
#    1. Add conditionals to outrule:
#       - decimals such as .69
#       - strings instead of numbers
#
#  elif time == (time, str):
#         print('Please use 24 h format')
#         restart = input('One more time? (yes/no)').lower()
#         if restart == "yes":
#             conv()
#             return 0
#==============================================================================
            
# Basic conversions of time zones in Europe and a few in USA: CET = standard time 
def conv():
    print('Convert time zone from CET.\n Please use 24 h format (e.g. 13.00)')
    try:
        time = float(input("Time: "))
    except ValueError:
        print("Invalid time format. Please enter a number like 13.00")
        return
# make sure the input is not greater than 24    
    if time > float(24):
        print('Please use 24 h format')
        restart = input('One more time? (yes/no)').lower()
        if restart == "yes":
            conv()
            return 0
        elif restart == "y":
            conv()
            return 0
        elif restart == "ok":
            conv()
            return 0
        else:
            print("Bye!")
            return
    else:
        zone = input("Zone (Available options: GET, CAT, EAT, CST, and EST): ").upper()
        if zone == 'CET':
            CET = time
            print("The time in e.g. Berlin is:", format(CET, '.2f'),"(CET time:", time,")")
        elif zone == ('GET'):
            GET = time - 1.0
            print("The time in e.g. London is:", format(GET, '.2f'),"(CET time:", time,")")
        elif zone == 'CAT':
            CAT = time + 1.0
            print('The time e.g. Johannesburg is:', format(CAT, '.2f'),"(CET time:", time,")")
        elif zone == 'EAT':
            EAT = time + 2.0
            print('The time e.g. Moscow is:', format(EAT, '.2f'),"(CET time:", time,")")
        elif zone == 'CST':
            CST = time - 7.0
            print('The time in e.g. Urbana Illinois is:', format(CST, '.2f'),"(CET time:", time,")")
        elif zone == 'EST':
            EST = time - 6.0
            print('The time in e.g. New York is:', format(EST, '.2f'),"(CET time:", time,")")
        else:       
            print('Sorry, time zone not available')
            restart = input("Do you want to retry?").lower()
            if restart == "yes":
                conv()
                return 0
            elif restart == "y":
                conv()
                return 0
            elif restart == "ok":
                conv()
                return 0
            else:
                 print("Bye!")
                 return
            
# call the function        
conv()

# pause so console doesn't close immediately when double-clicked
input('Press Enter to exit...')

# The format function '.2f' lets you specify how many decimals you want to show (2 in this case)     
#format(EST, '.2f')
# ...existing code...