# -*- coding: utf-8 -*-
"""
DADSA Assignment one TASK 1
Created on Wed Dec 30 18:41:50 2020 NEW VERSION

Version 3 of task one
Update: Dictionarys replaced with Storage classes and algorithms improved and shortened

@author: benjamin Ell-Jones 
"""


"""

TO DO:
1. delivery algorithm
2. Scheduling algorithm

"""
import csv

#Class to store Shop data
class Item:
    def __init__(self, itemName, itemPrice,itemStores):
        self.itemNumber = 0
        self.itemName = itemName
        self.itemPrice = itemPrice 
        self.itemStores = itemStores
        
    def getItemNumber(self):
        return self.itemNumber
    def getItemName(self):
        return self.itemName
    def getItemPrice(self):
        return self.itemPrice
    def getItemStores(self):
        return self.itemStores
    
    def setItemStores(self, storeLetter):
        self.stores.append(storeLetter)
    def setItemNumber(self, itemNumber):
        self.itemNumber = itemNumber
#Class to store shopping list data
class ShoppingLists:
    def __init__(self,houseName,week, itemList):   
        self.houseName = houseName
        self.itemList = itemList
        self.minimalCombinations = []
        self.week = week
        
        self.needToBuyShopA = []
        self.needToBuyShopAQuantities = []
        self.needToBuyShopB = []
        self.needToBuyShopBQuantities = []
        self.needToBuyShopC = []
        self.needToBuyShopCQuantities = []
        
        self.needToBuyShopD = []
        self.needToBuyShopDQuantities = []
        
    def getHouseName(self):
        return self.houseName
    def getItemList(self):
        return self.itemList
    def getWeek(self):
        return self.week
    def getMinimalCombinations(self):
        return self.minimalCombinations
    
    def getNeedToBuyShopAQuantities(self):
        return self.needToBuyShopAQuantities
    def getNeedToBuyShopBQuantities(self):
        return self.needToBuyShopBQuantities
    def getNeedToBuyShopCQuantities(self):
        return self.needToBuyShopCQuantities
    def getNeedToBuyShopDQuantities(self):
        return self.needToBuyShopCQuantities
    
    def getNeedToBuyShopA(self):
        return self.needToBuyShopA
    def getNeedToBuyShopB(self):
        return self.needToBuyShopB
    def getNeedToBuyShopC(self):
        return self.needToBuyShopC 
    def getNeedToBuyShopD(self):
        return self.needToBuyShopD 
    
    def setItemList(self, itemList):
        self.itemList.append(itemList)
    def setStoreCombinations(self, storeCombinations):
        self.minimalCombinations = storeCombinations
    
    def setNeedToBuyShopA(self, needToBuyShopA):
        self.needToBuyShopA.append(needToBuyShopA)
    def setNeedToBuyShopB(self, needToBuyShopB):
        self.needToBuyShopB.append(needToBuyShopB)
    def setNeedToBuyShopC(self, needToBuyShopC):
        self.needToBuyShopC.append(needToBuyShopC)
    def setNeedToBuyShopD(self, needToBuyShopD):
        self.needToBuyShopD.append(needToBuyShopD)
        
    def replaceNeedToBuyShopA(self, needToBuyShopA):
        self.needToBuyShopA = needToBuyShopA
    def replaceNeedToBuyShopB(self, needToBuyShopB):
        self.needToBuyShopB = needToBuyShopB
    def replaceNeedToBuyShopC(self, needToBuyShopC):
        self.needToBuyShopC = needToBuyShopC
    def replaceNeedToBuyShopD(self, needToBuyShopD):
        self.needToBuyShopD = needToBuyShopD
        
    def setNeedToBuyShopAQuantities(self, needToBuyShopAQuantities):
        self.needToBuyShopAQuantities.append(needToBuyShopAQuantities)
    def setNeedToBuyShopBQuantities(self, needToBuyShopBQuantities):
        self.needToBuyShopBQuantities.append(needToBuyShopBQuantities)
    def setNeedToBuyShopCQuantities(self, needToBuyShopCQuantities):
        self.needToBuyShopCQuantities.append(needToBuyShopCQuantities)
    def setNeedToBuyShopDQuantities(self, needToBuyShopDQuantities):
        self.needToBuyShopDQuantities.append(needToBuyShopDQuantities)
    
    def replaceNeedToBuyShopAQuantities(self, needToBuyShopAQuantities):
        self.needToBuyShopAQuantities = needToBuyShopAQuantities
    def replaceNeedToBuyShopBQuantities(self, needToBuyShopBQuantities):
        self.needToBuyShopBQuantities = needToBuyShopBQuantities
    def replaceNeedToBuyShopCQuantities(self, needToBuyShopCQuantities):
        self.needToBuyShopCQuantities = needToBuyShopCQuantities
    def replaceNeedToBuyShopDQuantities(self, needToBuyShopDQuantities):
        self.needToBuyShopDQuantities = needToBuyShopDQuantities
        
class Catagories: 
    def __init__(self,catagoryName ,itemList):   
        self.catagoryName = catagoryName
        self.itemList = itemList
    
    def getCatagoryName(self):
        return self.catagoryName
    def getItemList(self):
        return self.itemList
    
    def setCatagoryName(self, catagoryName):
        self.catagoryName = catagoryName        
    def setItemList(self, itemList):
        self.itemList = itemList

class Delivery():
    def __init__(self, day, week):   
        self.day = day 
        self.week = week
        self.deliverySchedule = []
        
    def getDayDelivery(self):
        return self.day
    def getWeekDelivery(self):
        return self.week
    def getdeliverySchedule(self):
        return self.deliverySchedule
        
    def setDayDelivery(self, day):
        self.day = day  
    
    def setDeliverySchedule(self, deliverySchedule):
        self.deliverySchedule.append(deliverySchedule)
            
class ShoppingSchedule():
    def __init__(self,day,week):   
        self.day = day  
        self.week = week
        self.ShopToBuyFrom = ""
        self.ShoppingToBuy = []
        self.ShoppingQuantities = []
        
    def getDayShoppingSchedule(self):
        return self.day
    def getWeekShoppingSchedule(self):
        return self.week
    def getShopToBuyFrom(self):
        return self.ShopToBuyFrom
    def getShopingToBuy(self):
        return self.ShoppingToBuy
    
    def getShoppingQuantities(self):
        return self.ShoppingQuantities
    
    def setDayShoppingSchedule(self, day):
        self.day = day    
    
    def setShopToBuyFrom(self, ShopToBuyFrom):
        self.ShopToBuyFrom = ShopToBuyFrom 
    def setShopingToBuy(self, ShoppingToBuy):
        self.ShoppingToBuy.append(ShoppingToBuy) 
    def setShoppingQuantities(self, ShoppingQuantities):
        self.ShoppingQuantities.append(ShoppingQuantities) 
        
shopObjects = [] # Stores a list of shop objects 
houseObjects = [] # stores a list of shopping list objects
catagoryObjects = [] # stores a list of catagory objects

shoppingScheduleObjects = []
deliveryObjects = []

countHouseNamesWeeks = [] # Stores a list of house names obtained by running inputCSVHouseNames() the result of that function is stored in here

#gets all shops and item data
def inputCSVShopList():
    with open('DATA CWK SHOPPING DATA WEEK 4 FILE A.csv', 'r') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        next(csv_reader1)
        for row1 in csv_reader1:       
            itemNumber = 0
            shopList = []
        
            itemNumber = itemNumber + 1
        
            tempShopStorageA = row1[3] 
            tempShopStorageB = row1[4]
            tempShopStorageC = row1[5]
            tempShopStorageD = row1[6]
            if(tempShopStorageA == 'Y'):
                shopList.append(tempShopStorageA)
            elif(tempShopStorageA == ''):
                shopList.append('N')
            else:
                print("Error StoreA Input")
            if(tempShopStorageB == 'Y'):
                shopList.append(tempShopStorageB)
            elif(tempShopStorageB == ''):
                shopList.append('N')
            else:
                print("Error StoreB Input")
            
            if(tempShopStorageC == 'Y'):
                shopList.append(tempShopStorageC)
            elif(tempShopStorageC == ''):
                shopList.append('N')
            else:
                print("Error StoreC Input") 
                
            if(tempShopStorageD == 'Y'):
                shopList.append(tempShopStorageD)
            elif(tempShopStorageD == ''):
                shopList.append('N')  
            else:
                print("Error StoreD Input")
            
            shopObjects.append(Item(row1[1],row1[2],shopList))
       
# Gets each house holds name          
def inputCSVHouseNames():
    with open('DATA CWK SHOPPING DATA WEEK 4 FILE B.csv', 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)   
        gotFirstLine = False # if set true python has obtained the first line from the csv file
        output = [] # Stores the output of this func to be returned
        
        for line2 in csv_reader2:
        
            if (gotFirstLine == False): # if the first line of the csv file has not been obtained do:
                countColumn = []  
                countInrange = 0
            
                for i in range(0,31): # for each column 
                    countInrange = countInrange + 1 
                    countColumn.append(line2[countInrange]) # Add obtained data from field in csv file to a tempary storage array
                
                    
                    output = countColumn # store contence in output
                gotFirstLine = True # One the first line from csv has been obtained set to true
    return output         

# Gets each house holds shopping list       
def inputCSVShoppingList(countHouseNamesWeeks):
    count = 1     
    weekCounter = 1
    
    for i in range(0,31): # for each house name in countHouseNamesWeeks
        count = count + 1
        
        tempStorageItemQuantity = []
        if (count > 15): # day counter is smaller than 7 days
            weekCounter = 2 # add week
    
        with open('DATA CWK SHOPPING DATA WEEK 4 FILE B.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
        
            next(csv_reader) # dont include row one of csv
            next(csv_reader) # dont include row two of csv
            
            if(count == 32):
                break
            else:
                for line in csv_reader: 
                    tempStorageItemQuantity.append(line[count])# append column to tempStorageItemQuantity
                houseObjects.append(ShoppingLists(countHouseNamesWeeks[i],weekCounter, tempStorageItemQuantity)) # create object and add data
            
#this function splits an items name into a selection of key words, those key words are analised and then the item is catagorised and stored in a list(category)
def categorySort():
    print("Category Sort")
    itemNumber = -1
    splitElementCount = -1
    splitItemName = []
    
    itemCategoryBread = []
    itemCategoryMilk = []
    itemCategoryRice = []
    itemCategoryButter = []
    itemCategoryApples = []
    itemCategoryOnions = []
    
    for i in shopObjects: # for each item
        itemNumber = itemNumber + 1
        itemName = shopObjects[itemNumber].getItemName() # Gets an items name
        splitItemName = itemName.split(' ') #Splits the item name into keywords
        for x in splitItemName: #For each keyword 
            splitElementCount = splitElementCount + 1 
            # This next section of code tries to match one of those key words to a catagory.
            #for example if an item has bread as a keyword it's item number will be added to the bread category
            if (splitItemName[splitElementCount] == "Bread" or splitItemName[splitElementCount] == "bread"):
                itemCategoryBread.append(itemNumber)                               
            
                #this next line is for testing
                #itemCategoryBread.append(shopObjects[itemNumber].getItemName())
                
            elif (splitItemName[splitElementCount] == "Milk" or splitItemName[splitElementCount] == "milk"):
                itemCategoryMilk.append(itemNumber) 
                
                #this next line is for testing
                #itemCategoryMilk.append(shopObjects[itemNumber].getItemName())
                
            elif (splitItemName[splitElementCount] == "Rice" or splitItemName[splitElementCount] == "rice"):
                itemCategoryRice.append(itemNumber) 
                
                #this next line is for testing
                #itemCategoryRice.append(shopObjects[itemNumber].getItemName())
                
            elif (splitItemName[splitElementCount] == "Butter" or splitItemName[splitElementCount] == "butter"):
                itemCategoryButter.append(itemNumber)
                
                #this next line is for testing
                #itemCategoryButter.append(shopObjects[itemNumber].getItemName())
                
            elif (splitItemName[splitElementCount] == "Apples" or splitItemName[splitElementCount] == "apples"):
                itemCategoryApples.append(itemNumber) 
                
                #this next line is for testing
                #itemCategoryApples.append(shopObjects[itemNumber].getItemName())
                
            elif (splitItemName[splitElementCount] == "Onions" or splitItemName[splitElementCount] == "onions"):
                itemCategoryOnions.append(itemNumber)
                
                #this next line is for testing
                #itemCategoryOnions.append(shopObjects[itemNumber].getItemName())
        splitElementCount = -1 
        
    catagoryObjects.append(Catagories("Bread", itemCategoryBread))
    catagoryObjects.append(Catagories("Milk", itemCategoryMilk))
    catagoryObjects.append(Catagories("Rice", itemCategoryRice))
    catagoryObjects.append(Catagories("Butter", itemCategoryButter))
    catagoryObjects.append(Catagories("Apples", itemCategoryApples))
    catagoryObjects.append(Catagories("Onions", itemCategoryOnions))
     
#Gives all items in the shopObjects = [] array Item Numbers
def giveItemNumber():
    itemNumber = -1
    for i in shopObjects:
        itemNumber = itemNumber + 1
        shopObjects[itemNumber].setItemNumber(itemNumber)
                      
#removes blank spaces in lists and replaces them with 0
# This function does scale       
def RemoveBlank(aList):
   
    count = -1
    for x in aList: #for each element in array
        count = count + 1
        if (aList[count] == ''): # if element equals nothing
            aList[count] = 0 # replace with 0
    return aList  

# Implements the RemoveBlank Method 
#Personal Note: ellipsis caused here
def replace():
    countHouseObjects = -1
    tempHouseList = []
    for i in houseObjects: # for each object in houseObjects
        countHouseObjects = countHouseObjects + 1
        tempHouseList = RemoveBlank(houseObjects[countHouseObjects].getItemList()) # remove the blank spots in a list in itemStores(array) in houseObjects and store in temp variable
        houseObjects[countHouseObjects].setItemList(tempHouseList)  # update list in itemStores(array) in houseObjects using data from tempHouseList variable
        tempHouseList = [] # clear the list for the next set of data

# Checks to see what stores a spesific item is in.
def inStore(item):
    inShops = ""
    tempStoreShopList = shopObjects[item].getItemStores()
    if (tempStoreShopList[0] == 'Y'):
        inShops = "A"
    elif (tempStoreShopList[1] == 'Y'):
        inShops = "B"
    elif (tempStoreShopList[2] == 'Y'):
        inShops = "C"
    elif (tempStoreShopList[3] == 'Y'):
        inShops = "D"
    return inShops  

# Will combine output of inStore so, for house A1 you may have A,B,A,A,B,A,B,B,A and this function will reduce it to A,B
def minimumStores(StoreShopChoice): # This function finds out what shops each house hold will need to visit
    StoreStoreAmmountA = 0
    StoreStoreAmmountB = 0
    StoreStoreAmmountC = 0
    StoreStoreAmmountD = 0
    count = 0
    
    logicalChoice = []
    for i in StoreShopChoice:
        if(StoreShopChoice[count] == 'A'):
            StoreStoreAmmountA = StoreStoreAmmountA + 1
           
        elif(StoreShopChoice[count] == 'B'):
            StoreStoreAmmountB = StoreStoreAmmountB + 1
           
        elif(StoreShopChoice[count] == 'C'):
            StoreStoreAmmountC = StoreStoreAmmountC + 1  
            
        elif(StoreShopChoice[count] == 'D'):
            StoreStoreAmmountD = StoreStoreAmmountD + 1      
        count = count + 1
    
    if(StoreStoreAmmountA >= 1):
        logicalChoice.append('A')
    if(StoreStoreAmmountB >= 1):
        logicalChoice.append('B')
    if(StoreStoreAmmountC >= 1):
        logicalChoice.append('C')
    if(StoreStoreAmmountD >= 1):
        logicalChoice.append('D')
    return logicalChoice

#Main Data proccessing function, uses minimumStores and inStore functionss 
def proccess():
    print("DADSA Assignment one TASK 1") #Prints project title
    print(" ")
    
    mainCounter = -1
    itemListCounter = -1
    
    tempProccessed = []
    combination = []
    
    for i in houseObjects:
        mainCounter = mainCounter + 1
        tempItemListStorage = houseObjects[mainCounter].getItemList()
        tempItemListStorage.pop()# Pops the strange ellipsis thing
        for i in tempItemListStorage:
            itemListCounter = itemListCounter + 1
            
            if (int(tempItemListStorage[itemListCounter]) > 0):
               canBeFoundInStore = inStore(itemListCounter)
               tempProccessed.append(canBeFoundInStore)
               
               itemName = shopObjects[itemListCounter].getItemName()
               
               if (canBeFoundInStore == "A"):                   
                   houseObjects[mainCounter].setNeedToBuyShopA(itemName) 
                   houseObjects[mainCounter].setNeedToBuyShopAQuantities(tempItemListStorage[itemListCounter])
               elif(canBeFoundInStore == "B"):
                   houseObjects[mainCounter].setNeedToBuyShopB(itemName) 
                   houseObjects[mainCounter].setNeedToBuyShopBQuantities(tempItemListStorage[itemListCounter])
                   
               elif(canBeFoundInStore == "C"):
                   houseObjects[mainCounter].setNeedToBuyShopC(itemName)
                   houseObjects[mainCounter].setNeedToBuyShopCQuantities(tempItemListStorage[itemListCounter])
                   
               elif(canBeFoundInStore == "D"):
                   houseObjects[mainCounter].setNeedToBuyShopD(itemName)    
                   houseObjects[mainCounter].setNeedToBuyShopDQuantities(tempItemListStorage[itemListCounter])
        combination = minimumStores(tempProccessed)
        houseObjects[mainCounter].setStoreCombinations(combination)
        tempProccessed = []
        itemListCounter = -1
    combination = []
    

#Handles Substitutions
def substitutions():
   
    houseCount = -1
     
   
    for i in houseObjects:
        houseCount = houseCount + 1
       
        houseObjectRequiredShops = houseObjects[houseCount].getMinimalCombinations()
        
        itemsRequiredA = houseObjects[houseCount].getNeedToBuyShopA()
        itemsRequiredB = houseObjects[houseCount].getNeedToBuyShopB()
        itemsRequiredC = houseObjects[houseCount].getNeedToBuyShopC()
        
        itemsRequiredAQuantities = houseObjects[houseCount].getNeedToBuyShopAQuantities()
        itemsRequiredBQuantities = houseObjects[houseCount].getNeedToBuyShopBQuantities()
        itemsRequiredCQuantities = houseObjects[houseCount].getNeedToBuyShopCQuantities()
        
        shopCount = -1 
        for x in houseObjectRequiredShops:
            shopCount = shopCount + 1
            if (houseObjectRequiredShops[shopCount] == 'A'):
                if(len(itemsRequiredA) < len(itemsRequiredB) and len(itemsRequiredA) < len(itemsRequiredC) or len(itemsRequiredA) < 2):
                    houseCombosToEdit = houseObjects[houseCount].getMinimalCombinations()
                    houseCombosToEdit.remove("A")
                    itemNumberA = -1 
                    itemsRequiredAAmmount = -1
                    for i in shopObjects:
                        itemNumberA = itemNumberA + 1
                        itemsRequiredAAmmount = -1
                        for i in itemsRequiredA:
                            itemsRequiredAAmmount = itemsRequiredAAmmount + 1
                            if (shopObjects[itemNumberA].getItemName() == itemsRequiredA[itemNumberA]):
                              
                              
                              # next section of code finds alternative item
                              catagoryCountA = -1
                              itemListA = []
                              for i in catagoryObjects:
                                   catagoryCountA = catagoryCountA + 1
                                   itemListA = catagoryObjects[catagoryCountA].getItemList()
                                    
                                   itemNumInCatagoryListA = -1
                                   for i in itemListA: # for each item in catagory 
                                       itemNumInCatagoryListA = itemNumInCatagoryListA + 1
                                        
                                       if (itemListA[itemNumInCatagoryListA] == itemNumberA): #if item is found in catagory
                                           WhatItemA = -1
                                           for i in itemListA: # for each item in catagory 
                                               WhatItemA = WhatItemA + 1
                                               if (itemListA[WhatItemA] != itemNumberA): # if you find an item that isnt the item we want to replace                                                   
                                                   
                                                   if (shopObjects[WhatItemA].getItemStores()[1] == "Y"): # and it can be bought in shop B
                                                      
                                                       
                                                       
                                                       houseObjects[houseCount].setStoreCombinations(houseCombosToEdit) 
                                                       itemsRequiredA.pop(itemsRequiredAAmmount)
                                                       houseObjects[houseCount].replaceNeedToBuyShopA(itemsRequiredA)
                                                       houseObjects[houseCount].setNeedToBuyShopB(shopObjects[itemListA[WhatItemA]].getItemName())
                                                       
                                                       save1 = itemsRequiredAQuantities.pop(itemsRequiredAAmmount)
                                                       houseObjects[houseCount].replaceNeedToBuyShopAQuantities(itemsRequiredAQuantities)
                                                       houseObjects[houseCount].setNeedToBuyShopBQuantities(save1)
                                                       
                                                       
                                                   elif(shopObjects[WhatItemA].getItemStores()[2] == "Y"):# and it can be bought in shop C
                                                         
                                                        houseObjects[houseCount].setStoreCombinations(houseCombosToEdit)
                                                        itemsRequiredA.pop(itemsRequiredAAmmount)
                                                        houseObjects[houseCount].replaceNeedToBuyShopA(itemsRequiredA)
                                                        houseObjects[houseCount].setNeedToBuyShopC(shopObjects[itemListA[WhatItemA]].getItemName())
                                                        
                                                        save2 = itemsRequiredAQuantities.pop(itemsRequiredAAmmount)
                                                        houseObjects[houseCount].replaceNeedToBuyShopAQuantities(itemsRequiredA)
                                                        houseObjects[houseCount].setNeedToBuyShopCQuantities(save2)
                                                     
                        itemsRequiredAAmmount = -1
                
                  
            elif (houseObjectRequiredShops[shopCount] == 'B'):
                if(len(itemsRequiredB) < len(itemsRequiredA) and len(itemsRequiredB) < len(itemsRequiredC) or len(itemsRequiredB) < 2):
                    houseCombosToEdit = houseObjects[houseCount].getMinimalCombinations()
                    houseCombosToEdit.remove("B")
                    itemNumberB = -1
                    for i in shopObjects: # for each item
                        itemNumberB = itemNumberB + 1
                        itemsRequiredBAmmount = -1
                        for i in itemsRequiredB: # for each item required from shop B
                            itemsRequiredBAmmount = itemsRequiredBAmmount  + 1
                          
                            if (shopObjects[itemNumberB].getItemName() == itemsRequiredB[itemsRequiredBAmmount]): # if the item we need to buy is in shop list then
                               
                                # next section of code finds alternative item
                                catagoryCountB = -1
                                itemListB = []
                                for i in catagoryObjects:
                                    catagoryCountB = catagoryCountB + 1
                                    itemListB = catagoryObjects[catagoryCountB].getItemList()
                                    
                                    itemNumInCatagoryListB = -1
                                    for i in itemListB: # for each item in catagory 
                                        itemNumInCatagoryListB = itemNumInCatagoryListB + 1
                                        
                                        if (itemListB[itemNumInCatagoryListB] == itemNumberB): #if item is found in catagory
                                            WhatItemB = -1
                                            for i in itemListB: # for each item in catagory 
                                                WhatItemB = WhatItemB + 1
                                                if (itemListB[WhatItemB] != itemNumberB): # if you find an item that isnt the item we want to replace                                                   
                                                    
                                                    if (shopObjects[WhatItemB].getItemStores()[0] == "Y"): # and it can be bought in shop A
                                                                                    
                                                        houseObjects[houseCount].setStoreCombinations(houseCombosToEdit) 
                                                       
                                                        itemsRequiredB.pop(itemsRequiredBAmmount)#remove item
                                                        houseObjects[houseCount].replaceNeedToBuyShopB(itemsRequiredB)# Update item list
                                                        houseObjects[houseCount].setNeedToBuyShopA(shopObjects[itemListB[WhatItemB]].getItemName())# add replacement to list
                                                        
                                                        save3 = itemsRequiredBQuantities.pop(itemsRequiredBAmmount)
                                                        houseObjects[houseCount].replaceNeedToBuyShopAQuantities(itemsRequiredBQuantities)
                                                        houseObjects[houseCount].setNeedToBuyShopAQuantities(save3)
                                                        break
                                                    elif(shopObjects[WhatItemB].getItemStores()[2] == "Y"):# and it can be bought in shop C
                                                                                                                                                                           
                                                         houseObjects[houseCount].setStoreCombinations(houseCombosToEdit)
                                                         itemsRequiredB.pop(itemsRequiredBAmmount)#remove item
                                                         houseObjects[houseCount].replaceNeedToBuyShopB(itemsRequiredB)# Update item list
                                                         houseObjects[houseCount].setNeedToBuyShopC(shopObjects[itemListB[WhatItemB]].getItemName())
                                                         
                                                         save4 = itemsRequiredBQuantities.pop(itemsRequiredBAmmount)
                                                         houseObjects[houseCount].replaceNeedToBuyShopBQuantities(itemsRequiredBQuantities)
                                                         houseObjects[houseCount].setNeedToBuyShopCQuantities(save4)
                                                         break
    
                            itemsRequiredBAmmount = -1
                                                        
            elif (houseObjectRequiredShops[shopCount] == 'C'):
                if(len(itemsRequiredC) < len(itemsRequiredB) and len(itemsRequiredC) < len(itemsRequiredA) or len(itemsRequiredC) < 2):
                    houseCombosToEdit = houseObjects[houseCount].getMinimalCombinations()
                    houseCombosToEdit.remove("C")
                    itemNumberC = -1
                    for i in shopObjects:
                        itemNumberC = itemNumberC + 1
                        itemsRequiredCAmmount = -1
                        for x in itemsRequiredC:
                            itemsRequiredCAmmount = itemsRequiredCAmmount + 1
                            
                            if (shopObjects[itemNumberC].getItemName() == itemsRequiredC[itemsRequiredCAmmount]):
                                
                                # next section of code finds alternative item
                                catagoryCount = -1
                                itemList = []
                                for i in catagoryObjects:
                                    catagoryCount = catagoryCount + 1
                                    itemList = catagoryObjects[catagoryCount].getItemList()
                                    
                                    itemNumInCatagoryList = -1
                                    for i in itemList:
                                        itemNumInCatagoryList = itemNumInCatagoryList + 1
                                        if (itemList[itemNumInCatagoryList] == itemNumberC): #if item is found in that list
                                            WhatItem = -1
                                            for i in itemList:
                                                WhatItem = WhatItem + 1
                                                if (itemList[WhatItem] != itemNumberC ):                                                    
                                                    if (shopObjects[WhatItem].getItemStores()[0] == "Y"):
                                                                                                            
                                                        houseObjects[houseCount].setStoreCombinations(houseCombosToEdit) 
                                                        itemsRequiredC.pop(itemsRequiredCAmmount)#remove item
                                                        houseObjects[houseCount].replaceNeedToBuyShopC(itemsRequiredC)
                                                        houseObjects[houseCount].setNeedToBuyShopA(shopObjects[itemList[WhatItem]].getItemName())
                                                        
                                                        save5 = itemsRequiredCQuantities.pop(itemsRequiredCAmmount)
                                                        houseObjects[houseCount].replaceNeedToBuyShopCQuantities(itemsRequiredCQuantities)
                                                        houseObjects[houseCount].setNeedToBuyShopAQuantities(save5)
                                                      
                                                        break
                                                    elif(shopObjects[WhatItem].getItemStores()[1] == "Y"):                                                                                                                                                            
                                                        
                                                        itemsRequiredC.pop(itemsRequiredCAmmount)#remove item
                                                        houseObjects[houseCount].replaceNeedToBuyShopC(itemsRequiredC)
                                                        houseObjects[houseCount].setNeedToBuyShopB(shopObjects[itemList[WhatItem]].getItemName())
                                                        
                                                        save6 = itemsRequiredCQuantities.pop(itemsRequiredCAmmount)
                                                        houseObjects[houseCount].replaceNeedToBuyShopCQuantities(itemsRequiredCQuantities)
                                                        houseObjects[houseCount].setNeedToBuyShopBQuantities(save6)
                                                        break
                        itemsRequiredCAmmount = -1

#Adds days to scedule/Generates raw schedule with no deliverys or shopping trips
def addDays():
    dayCount = 0
    weekCount = 1
    for i in range(0,14):
        dayCount = dayCount + 1
        if(dayCount == 7):
            dayCount = 1
            weekCount = weekCount + 1
            
        shoppingScheduleObjects.append(ShoppingSchedule(dayCount,weekCount))#Adds days 
        deliveryObjects.append(Delivery(dayCount,weekCount))#Adds days

#creates Shopping and delivery Scedules
def Scedule():
    shoppingCountWeekOne = -1


    for i in houseObjects:
        shoppingCountWeekOne = shoppingCountWeekOne + 1
        
        minimumCombos = houseObjects[shoppingCountWeekOne].getMinimalCombinations()
        
        minimumCombosCount = -1
        
        comboA = False
        comboB = False
        comboC = False
        
        for x in minimumCombos: 
            minimumCombosCount = minimumCombosCount + 1
            if(minimumCombos[minimumCombosCount] == 'A'):
                comboA = True
            elif(minimumCombos[minimumCombosCount] == 'B'): 
                comboB = True
            elif(minimumCombos[minimumCombosCount] == 'C'):
                comboC = True
                
        if(comboA == True and comboB == True or comboA == True or comboB == True):
            # Week 1 timetabling
            if(shoppingCountWeekOne <= 3):
                if (comboA == True):
                    shoppingScheduleObjects[0].setShopToBuyFrom("A")
                    shoppingScheduleObjects[0].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopA())
                if (comboB == True):
                    shoppingScheduleObjects[1].setShopToBuyFrom("B")
                    shoppingScheduleObjects[1].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                deliveryObjects[1].setDeliverySchedule(houseObjects[shoppingCountWeekOne].getHouseName())
           
            elif(shoppingCountWeekOne < 7):
                if (comboA == True):
                    shoppingScheduleObjects[2].setShopToBuyFrom("A")
                    shoppingScheduleObjects[2].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                if (comboB == True):
                    shoppingScheduleObjects[3].setShopToBuyFrom("B")
                    shoppingScheduleObjects[3].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                deliveryObjects[3].setDeliverySchedule(houseObjects[shoppingCountWeekOne].getHouseName())
                
            # Week 2 timetabling
            elif(shoppingCountWeekOne >= 7):
                 if (comboA == True):
                   shoppingScheduleObjects[8].setShopToBuyFrom("A")
                   shoppingScheduleObjects[8].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                 if (comboB == True):
                    shoppingScheduleObjects[9].setShopToBuyFrom("B")
                    shoppingScheduleObjects[9].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                 deliveryObjects[9].setDeliverySchedule(houseObjects[shoppingCountWeekOne].getHouseName())
            
            elif(shoppingCountWeekOne < 7):
                if (comboA == True):
                    shoppingScheduleObjects[11].setShopToBuyFrom("A")
                    shoppingScheduleObjects[11].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                if (comboB == True):
                    shoppingScheduleObjects[12].setShopToBuyFrom("B")
                    shoppingScheduleObjects[12].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                deliveryObjects[12].setDeliverySchedule(houseObjects[shoppingCountWeekOne].getHouseName())
        
        comboA = False
        comboB = False
        comboC = False

#outputs Shopping scedule
def outputScedule():
    shoppingSceduleCount = -1
    print("Shopping Scedule")
    for i in shoppingScheduleObjects:
        shoppingSceduleCount = shoppingSceduleCount + 1
        
        shopToBuyFrom = shoppingScheduleObjects[shoppingSceduleCount].getShopToBuyFrom()
        if(shopToBuyFrom != ""):
            print("===============================================")
            print("Week: " + str(shoppingScheduleObjects[shoppingSceduleCount].getWeekShoppingSchedule()))
            print("Day " + str(shoppingScheduleObjects[shoppingSceduleCount].getDayShoppingSchedule()))
            print("Shop to buy from: " + shopToBuyFrom)
            print("Items to buy: ")
            print(shoppingScheduleObjects[shoppingSceduleCount].getShopingToBuy())
            print("===============================================")
            input("Press enter for next: ")
            print(" ")

#outputs delivery schedule
def outputDelivery():
    deliveryObjectsCount = -1
    print("Delivery Scedule")
    for i in deliveryObjects:
        deliveryObjectsCount = deliveryObjectsCount + 1

        houseToDeliverTo = deliveryObjects[deliveryObjectsCount].getdeliverySchedule()
        if not houseToDeliverTo:
            print("===============================================")
            print("Week: " + str(deliveryObjects[deliveryObjectsCount].getWeekDelivery()))
            print("Day " + str(deliveryObjects[deliveryObjectsCount].getDayDelivery()))
            print("No delivery today")
            print("===============================================")
        else:
            print("===============================================")
            print("Week: " + str(deliveryObjects[deliveryObjectsCount].getWeekDelivery()))
            print("Day " + str(deliveryObjects[deliveryObjectsCount].getDayDelivery()))
            print("Houses to deliver to: ")
            print(houseToDeliverTo)
            print("===============================================")
            input("Press enter for next: ")
            print(" ")

# prints out data from each object in shopObjects FOR TESTING PERPOSES ONLY    
def printshopObjectsTest():
    count = -1
    for x in shopObjects:
        count = count + 1
        print("====================================================") 
        print(shopObjects[count].getItemNumber())
        print(shopObjects[count].getItemName())
        print(shopObjects[count].getItemPrice())
        print(shopObjects[count].getItemStores())
        print("====================================================") 
        print(" ")
        
# prints out data from each object in houseObjects FOR TESTING PERPOSES ONLY    
def printHouseObjects():
    count = -1
    for x in houseObjects:
        count = count + 1
        print("House name: " + houseObjects[count].getHouseName())
        print("Week: " + str(houseObjects[count].getWeek()))
        print(houseObjects[count].getItemList())
        print(houseObjects[count].getMinimalCombinations())
        print(" ")
        print("From shop A:")
        print(houseObjects[count].getNeedToBuyShopA())
        print(" ")
        print("From shop B:")
        print(houseObjects[count].getNeedToBuyShopB())
        print(" ") 
        print("From shop C:")
        print(houseObjects[count].getNeedToBuyShopC())
        print(" ")
        print("From shop D:")
        print(houseObjects[count].getNeedToBuyShopD())
        print(" ")
        print("Item Quantities")
        print("From shop A:")
        print(houseObjects[count].getNeedToBuyShopAQuantities())
        print(" ")
        print("From shop B:")
        print(houseObjects[count].getNeedToBuyShopBQuantities())
        print(" ") 
        print("From shop C:")
        print(houseObjects[count].getNeedToBuyShopCQuantities())
        print(" ") 
        print("From shop D:")
        print(houseObjects[count].getNeedToBuyShopDQuantities())
        print("====================================================")  
        
        
# prints out data from each object in catagories FOR TESTING PERPOSES ONLY       
def outputCategories():
    print(" ")
    print("===================================================================")
    print("Bread") 
    print("Item Numbers")     
    print(catagoryObjects[0].getItemList())
    print("============================================")
    print("Milk")
    print("Item Numbers")  
    print(catagoryObjects[1].getItemList())
    print("============================================")
    print("Rice")
    print("Item Numbers")  
    print(catagoryObjects[2].getItemList())
    print("============================================")
    print("Butter")
    print("Item Numbers")  
    print(catagoryObjects[3].getItemList())
    print("============================================")
    print("Apples")
    print("Item Numbers")  
    print(catagoryObjects[4].getItemList())
    print("============================================")
    print("Onions")
    print("Item Numbers")  
    print(catagoryObjects[5].getItemList())
    print("===================================================================")  
    print(" ")

#runs all other functions    
def main():
    inputCSVShopList() 
    countHouseNamesWeeks = inputCSVHouseNames()
    countHouseNamesWeeks.pop(0)
    inputCSVShoppingList(countHouseNamesWeeks)
    categorySort() # Implement for task 2
    giveItemNumber() 
    replace()    
    proccess()
    #substitutions() # Implement for task 2
    addDays()        
    #Scedule() # Implement for task 2  
            
    #outputScedule()   # Implement for task 2     
    #outputDelivery()   # Implement for task 2     

main()

#outputs class data for testing    
def test():      
    #printshopObjectsTest()
    #outputCategories() 
    printHouseObjects()       
        
test()        
        
        
        
        


     