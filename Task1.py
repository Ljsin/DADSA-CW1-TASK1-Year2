#FILE: Task1.py 
#DATE LAST MODIFIED: 08/02/2021
#------------------------------------------

#STUDENT NAME: Lloyd Wood
#STUDENT NUMBER: 19000148
#------------------------------------------

import csv
#STOCK AND SHOPPING LIST AS TWO SEPARATE ARRAYS
store_stock_list = [] 
house_shop_list = []

#STORES HOUSE ORDERES AND HOUSES IN BOTH WEEKS INTO A LIST
house_orders = []
houses_W1 = ['1A','1B','1C','1D','1E','2C','3E']
houses_W2 = ['1A','1B','1C','1D','1E','2C','3E']

item_price = []
item_quantity = []

#LIST ARRAYS CREATED FOR EACH WEEK 
WEEK1 = [] 
WEEK2 = [] 

#LIST ARRAYS CREATED FOR EACH SHOP
SHOP_A = [] 
SHOP_B = [] 
SHOP_C = [] 

#LIST OF STORE COMBINATION 
AB_COMBO = []
AC_COMBO = []
BC_COMBO = []

#LIST OF STORES COMBINED 
SHOP_AB = []
SHOP_AC = []
SHOP_BC = []

#STORES DAYS OF THE WEEK INTO A LIST 
days = ['MONDAY', 
'TUESDAY', 
'WEDNESDAY', 
'THRUSDASY', 
'FRIDAY', 
'SATURDAY', 
'SUNDAY']

#############################################################################
#print(input("Press [ENTER] to view STOCK IN EACH STORE & WEEK LISTS..."))
#############################################################################

#FUNCTION: Week_stock
#PARAM: NONE
#DESC: Splits stock list into three individual lists from each store A, B and C 
#RETURNS: list - Week_stock
def Week_stock():
    
    with open("CW1/DADSA CWK SHOPPING DATA WEEK 1 File A.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        #DEFINED AS A GLOBAL TO BE USED INSIDE AND OUTSIDE THIS FUNCTION 
        global store_stock_list 
        #LIST HOLDS READER FOR CSV FILE 
        store_stock_list = list(csv_reader)
        
        for column in range(1, 28):
            if store_stock_list[column][3] == "Y":
                SHOP_A.append(store_stock_list[column][0] + store_stock_list[column][1])
            if store_stock_list[column][4] == "Y":
                SHOP_B.append(store_stock_list[column][0] + store_stock_list[column][1]) 
            if store_stock_list[column][5] == "Y":
                SHOP_C.append(store_stock_list[column][0] + store_stock_list[column][1])
            # APPENDING EACH SHOP WITH THE STOCK LIST BY COLUMN AND INDEX OF 1 
        
    with open("CW1/DATA CWK SHOPPING DATA WEEK 1 FILE B.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        house_shop_list = list(csv_reader)
    return house_shop_list
    # RETURNING THE SHOPPING LIST FROM FILE B
house_shop_list = Week_stock()
# CALLING THE FUNCTION FROM THE SHOPPING LIST


#FUNCTION: Week_list
#PARAM: NONE
#DESC: contains both a list of week 1 and week 2's items 
#RETURNS: list - Week_list
def Week_list():
    for i in range(2, 29):
        # CREATING A LIST TO STORE INDEX VALUES FOR SHOPPING LIST WITHIN WEEK 2
        list1 = str(house_shop_list[i][0]) + str(house_shop_list[i][8:])
        WEEK1.append(house_shop_list[i][0:8])
        # APPENDING EACH WEEK 1 LIST WITH THE SHOPPING LIST
        # & WEEK 2 LIST WITH CREATED LIST VARIABLE
        WEEK2.append(list1)   
# CALLING FUNCTION 
Week_list()

# PRINTS ALL STORE ITEMS AND ITEMS WITHIN BOTH WEEKS
print("[SHOP A LIST]")
print(*SHOP_A, sep='\n')
print('\n')
print("[SHOP B LIST]")
print(*SHOP_B, sep='\n')
print('\n')
print("[SHOP C LIST]")
print(*SHOP_C, sep='\n')
print('\n')
print("[WEEK 1 LIST]")
print(*WEEK1, sep='\n')
print('\n')
print("[WEEK 2 LIST]")
print(*WEEK2, sep='\n')
print('\n')

"""print("[SHOP A LIST]")
for store_stock_list in SHOP_A:
    print(store_stock_list)
print('\n')
print("[SHOP B LIST]")
for store_stock_list in SHOP_B:
    print(store_stock_list)
print('\n')
print("[SHOP C LIST]")
for store_stock_list in SHOP_C:
    print(store_stock_list)
print('\n')
print("[WEEK 1 LIST]")
for house_shop_list in WEEK1:
    print(house_shop_list)
print('\n')
print("[WEEK 2 LIST]")
for house_shop_list in WEEK2:
    print(house_shop_list)
print('\n')"""


#############################################################################
#print(input("Press [ENTER] to view HOUSE SHOPPING SCHEDULE FOR WEEK 1 AND 2..."))
#############################################################################

#FUNCTION: houses_in_weeks
#PARAM: NONE
#DESC: Reads house data printing each household number and items for sp
#RETURNS: list of houses and items 
def read_house_data():
    # LOOPS THROUGH HOUSES IN WEEK 1 LIST
    for i in range(1, 8):
        print("HOUSE", house_shop_list[0][i] + ":")
        # FOR LOOP FOR ITEM/ITEMS IN LIST
        for j in range(1, 29):
            if house_shop_list[j][i] >= '1':
                print(store_stock_list[j-1][1] + store_stock_list[j-1][2])
        print("")
 
    # LOOPS THROUGH HOUSES IN WEEK 2 LIST
    for x in range(8, 15):
        print("HOUSE", house_shop_list[0][x] + ":")
        # FOR LOOP FOR ITEM/ITEMS IN LIST
        for k in range(1, 29):
            if house_shop_list[k][x] >= '1':
                print(store_stock_list[k-1][1] + store_stock_list[k-1][2])
        print("")


#FUNCTION: available_itemsW1
#PARAM: list - shop 
#DESC: shows items that are available in week 1 for each household
#RETURNS: list of items for each household within 
# week 1 and the total of number items 
def available_itemsW1(shop):
    # FOR LOOP FOR HOUSES IN WEEK 1
    for i in range(1, 8):
        count = 0
        print("HOUSE", house_shop_list[0][i] + ":")
        # FOR LOOP FOR ITEM/ITEMS IN LIST
        for j in range(1, 29):
            if house_shop_list[j][i] >= '1':
                for item in shop:
                    if item == house_shop_list[j][0]:
                        print(house_shop_list[j-0][1] + (" x ") + store_stock_list[j-1][1]
                         + (": ") + store_stock_list[j-1][2])
                        count += 1        
        print("Total number of required items: " + str(count))
        print("")

#FUNCTION: available_itemsW2
#PARAM: list - shop
#DESC: shows items that are available in week 2 for each household
#RETURNS: list of items for each household within 
# week 2 and the total of number items 
def available_itemsW2(shop):
    # FOR LOOP FOR HOUSES IN WEEK 1
    for x in range(8, 15):
        count = 0
        print("HOUSE", house_shop_list[0][x] + ":")
        # FOR LOOP FOR ITEM/ITEMS IN LIST
        for k in range(1, 29):
            if house_shop_list[k][x] >= '1':
                for item in shop:
                    if item == house_shop_list[k][0]:
                        print(house_shop_list[k-0][1] + (" x ") + store_stock_list[k-1][1] 
                        + (": ") + store_stock_list[k-1][2])
                        count += 1
        print("Total number of required items: " + str(count))
        print("")


#FUNCTION: remove_duplicates 
#PARAM: list - org_stores, list - new_stores 
#DESC: Removes any duplicate lists and stores elements into a new list 
#RETURNS: Lists without any duplicated items in each store combination 
def remove_dup_items(org_stores, new_stores):
    for duplicate_items in org_stores:
        if duplicate_items != new_stores:
            new_stores.append(duplicate_items)
            #APPENDS NEW STORES WITH DUP ITEMS WHEN STORED INTO A NEW LIST 

#REMOVES DUPLICATED ITEMS WITH STORE COMBINATIONS 
remove_dup_items(AB_COMBO, SHOP_AB)
remove_dup_items(AC_COMBO, SHOP_AC)
remove_dup_items(BC_COMBO, SHOP_BC)


#PRINTS A SHOPPING LIST FOR ITEMS REQUIRED BY EACH HOUSEHOLD 
# FROM SHOP A, B AND C WITHIN BOTH WEEKS 
print("_"*20, "SHOPPING SCHEDULE - WEEK 1 - SHOP A", "_"*20)
print('\n')
available_itemsW1(SHOP_A)
print("_"*20, "SHOPPING SCHEDULE - SHOP B", "_"*20)
print('\n')
available_itemsW1(SHOP_B)
print("_"*20, "SHOPPING SCHEDULE - SHOP C", "_"*20)
print('\n')
available_itemsW1(SHOP_C)
 
print("_"*20, "SHOPPING SCHEDULE - WEEK 2 - SHOP A", "_"*20)
print('\n')
available_itemsW2(SHOP_A)
print("_"*20, "SHOPPING SCHEDULE - SHOP B", "_"*20)
print('\n')
available_itemsW2(SHOP_B)
print("_"*20, "SHOPPING SCHEDULE - SHOP C", "_"*20)
print('\n')
available_itemsW2(SHOP_C)

#############################################################################
#print(input("Press [ENTER] to view DELIVERY SCHEDULE FOR WEEK 1..."))
#PRINTS DELIVERY SCHEDULE FOR WEEK 1
print("_"*20, "DELIVERY SCHEDULE FOR HOUSES -  WEEK 1", "_"*20)
#############################################################################

#FUNCTION: delivery_scheduleW1()
#PARAM: NONE
#DESC: Creates a delivery schedule for households for the first week
#RETURNS: Displays delivery days for each household that contains the SHOP products are being delivered from 
def delivery_scheduleW1():
    MAX_FROM_SHOP_A = 0
    MAX_FROM_SHOP_B = 0
    MAX_FROM_SHOP_C = 0

    for columns in house_orders:
        if(houses_W1 and columns != 'Products'):
               MAX_FROM_SHOP_A = MAX_FROM_SHOP_A + house_shop_list[columns][0]
               MAX_FROM_SHOP_B = MAX_FROM_SHOP_B + house_shop_list[columns][1]
               MAX_FROM_SHOP_C = MAX_FROM_SHOP_C + house_shop_list[columns][2]
    for columns in houses_W1:
        SHOP_A = house_shop_list[0]
        SHOP_B = house_shop_list[1]
        SHOP_C = house_shop_list[2]
        if(SHOP_A > SHOP_B and SHOP_A > SHOP_C):
            print(f"DELIVERY DAY FOR HOUSE {columns[0:]}: "  f"{days[0]} : [SHOP A PRODUCTS]")
            if(SHOP_B > SHOP_C):
                if(SHOP_C == 0):
                    print(days[1] + "[SHOP B PRODUCTS]")
                else: print(days[1] + "[SHOP B PRODUCTS]")
        if(SHOP_B > SHOP_A and SHOP_B > SHOP_C):
            print(f" DELIVERY DAY FOR HOUSE {columns[0:]}: " f"{days[0]} : [SHOP B PRODUCTS]")
            if(SHOP_A > SHOP_C):
                if(SHOP_C == 0):
                    print(f"{days[1]}: [SHOP A PRODUCTS]")
                else: print(f"{days[1]}: [SHOP A PRODUCTS]")
        if(SHOP_C > SHOP_A and SHOP_C > SHOP_B):
            print(f"DELIVERY DAY FOR HOUSE {columns[0:]}: " f"{days[0]} : [SHOP A PRODUCTS]")
            if(SHOP_A > SHOP_B):
                if(SHOP_B == 0):
                    print(f"{days[1]}: [SHOP A PRODUCTS]")
                else: print(f"{days[1]}: [SHOP A PRODUCTS]")
            if(SHOP_B > SHOP_A):
                if(SHOP_A == 0):
                    print(f"{days[1]}: [SHOP B PRODUCTS]")
                else: print(f"{days[1]}:   [SHOP B PRODUCTS]  , " +  f"{days[2]}: [NO DELIVERY TODAY!]"), 
                print(f"{days[3]}: [NO DELIVERY TODAY!] ,  " +  f"{days[4]}: [NO DELIVERY TODAY!]"), 
                print(f"{days[5]}:  [REST DAY!]          ,  " + f"{days[6]}: [REST DAY!]")
        print("")
delivery_scheduleW1()

print('\n')

#############################################################################
#print(input("Press [ENTER] to view DELIVERY SCHEDULE FOR WEEK 2..."))
#PRINTS DELIVERY SCHEDULE FOR WEEK 2
print("_"*20, "DELIVERY SCHEDULE FOR HOUSES - WEEK 2", "_"*20)
#############################################################################

#FUNCTION: delivery_scheduleW1()
#PARAM: NONE
#DESC: Creates a delivery schedule for households for the second week
#RETURNS: Returns exactly the same as week one's function only difference is the SHOP selection
def delivery_scheduleW2():
    MAX_FROM_SHOP_A = 0
    MAX_FROM_SHOP_B = 0
    MAX_FROM_SHOP_C = 0
    for columns in house_orders:
        if(houses_W2 and columns != 'Products'):
               MAX_FROM_SHOP_A = MAX_FROM_SHOP_A + house_shop_list[columns][0]
               MAX_FROM_SHOP_B = MAX_FROM_SHOP_B + house_shop_list[columns][1]
               MAX_FROM_SHOP_C = MAX_FROM_SHOP_C + house_shop_list[columns][2]
    for columns in houses_W2:
        SHOP_A = house_shop_list[0]
        SHOP_B = house_shop_list[1]
        SHOP_C = house_shop_list[2]
        if(SHOP_A > SHOP_B and SHOP_A > SHOP_C):
            print(f"DELIVERY DAY FOR HOUSE {columns[0:]}: " f"{days[0]} : [SHOP A PRODUCTS]")
            if(SHOP_B > SHOP_C):
                if(SHOP_C == 0):
                    print(days[1] + ": [SHOP B PRODUCTS]")
                else: print(days[1] + ": [SHOP C PRODUCTS]")
        if(SHOP_B > SHOP_A and SHOP_B > SHOP_C):
            print(f"DELIVERY DAY FOR HOUSE {columns[0:]}: " f"{days[0]} : [SHOP B PRODUCTS]")
            if(SHOP_A > SHOP_C):
                if(SHOP_C == 0):
                    print(days[1] + ": [SHOP A PRODUCTS]")
                else: print(days[1] + ": [SHOP C PRODUCTS]")
        if(SHOP_B > SHOP_A or SHOP_A > SHOP_B):
            print(f"DELIVERY DAY FOR HOUSE {columns[0:]}: " f"{days[0]} : [SHOP B PRODUCTS]")
            if(SHOP_A > SHOP_B):
                if(SHOP_B == 0):
                    print(f"{days[1]}: [SHOP A PRODUCTS]")
                else: print(f"{days[1]}: [SHOP B PRODUCTS]")
            if(SHOP_B > SHOP_A):
                if(SHOP_A == 0):
                    print(f"{days[1]}:   [SHOP B PRODUCTS]")
                else: print(f"{days[1]}:   [SHOP A PRODUCTS]  , " + f"{days[2]}: [NO DELIVERY TODAY!]"), 
                print(f"{days[3]}: [NO DELIVERY TODAY!] ,  " + f"{days[4]}: [NO DELIVERY TODAY!]"), 
                print(f"{days[5]}:  [REST DAY!]          ,  " + f"{days[6]}: [REST DAY!]")

        print("")
delivery_scheduleW2()
