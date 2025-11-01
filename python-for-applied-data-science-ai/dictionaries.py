#python-for-applied-data-science-ai


#Dictionaries: Start #####################
#####################################
# dictionaries consist of keys and values. 
# Keys can only be strings, numbers, or tuples, but values can be any data type.
#Each key is separated from its value by a colon ":".
# Commas separate the items, and the whole dictionary is enclosed in curly braces.

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 
# Retreave the keys and values?:
soundtrack_dic.keys()
soundtrack_dic.values()
#Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the value
album_sales_dict = {"Back in black":50,"The bodyguard":50, "Thriller":65}
album_sales_dict["Thriller"]

# Task-1 Create an empty dictionary
inventory = {}
# Task-2 Store the first product details in variable
inventory["Mobile_phone"] = {"Mobile_phone_Quantity":5, "Mobile_phone_price":20000, "Mobile_phone_Release_Year":2020}
# Task-3 Add the details in inventory
inventory
# Task-4 Store the second product details in a variable.
inventory["Laptop"] = {"Laptop_Quantity": 10, "Laptop_price": 50000, "Laptop_Release_Year": 2023}

# Task-4 Store the second product details in a variable
inventory.keys()
# Task-7 Check if ProductNo1_releaseYear and ProductNo2_releaseYear is in the inventory
inventory["Mobile_phone"]["Mobile_phone_Release_Year"]
inventory["Laptop"]["Laptop_Release_Year"]
print("Mobile_phone_Release_Year" in inventory["Mobile_phone"])
# Task-8 Delete release year of both the products from the inventory
del(inventory["Mobile_phone"]["Mobile_phone_Release_Year"])
inventory
del(inventory["Laptop"]["Laptop_Release_Year"])
