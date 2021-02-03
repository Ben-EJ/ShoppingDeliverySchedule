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
1. display item quantitys 
2. 

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
    
    def getNeedToBuyShopA(self):
        return self.needToBuyShopA
    def getNeedToBuyShopB(self):
        return self.needToBuyShopB
    def getNeedToBuyShopC(self):
        return self.needToBuyShopC 
    
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
    
    def replaceNeedToBuyShopA(self, needToBuyShopA):
        self.needToBuyShopA = needToBuyShopA
    def replaceNeedToBuyShopB(self, needToBuyShopB):
        self.needToBuyShopB = needToBuyShopB
    def replaceNeedToBuyShopC(self, needToBuyShopC):
        self.needToBuyShopC = needToBuyShopC

    def replaceMinimalCombinations(self, minimalCombinations):
        self.minimalCombinations = minimalCombinations

    def setNeedToBuyShopAQuantities(self, needToBuyShopAQuantities):
        self.needToBuyShopAQuantities.append(needToBuyShopAQuantities)
    def setNeedToBuyShopBQuantities(self, needToBuyShopBQuantities):
        self.needToBuyShopBQuantities.append(needToBuyShopBQuantities)
    def setNeedToBuyShopCQuantities(self, needToBuyShopCQuantities):
        self.needToBuyShopCQuantities.append(needToBuyShopCQuantities)
    
    def replaceNeedToBuyShopAQuantities(self, needToBuyShopAQuantities):
        self.needToBuyShopAQuantities = needToBuyShopAQuantities
    def replaceNeedToBuyShopBQuantities(self, needToBuyShopBQuantities):
        self.needToBuyShopBQuantities = needToBuyShopBQuantities
    def replaceNeedToBuyShopCQuantities(self, needToBuyShopCQuantities):
        self.needToBuyShopCQuantities = needToBuyShopCQuantities

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

def inputCSVShopList():
    with open('DADSA CWK SHOPPING DATA WEEK 1 File A.csv', 'r') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        next(csv_reader1)
        for row1 in csv_reader1:       
            itemNumber = 0
            shopList = []
        
            itemNumber = itemNumber + 1
        
            tempShopStorageA = row1[3] 
            tempShopStorageB = row1[4]
            tempShopStorageC = row1[5]
        
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
            
            shopObjects.append(Item(row1[1],row1[2],shopList))
        
 
          
def inputCSVHouseNames():
    with open('DATA CWK SHOPPING DATA WEEK 1 FILE B.csv', 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)   
        gotFirstLine = False # if set true python has obtained the first line from the csv file
        output = [] # Stores the output of this func to be returned
        
        for line2 in csv_reader2:
        
            if (gotFirstLine == False): # if the first line of the csv file has not been obtained do:
                countColumn = []  
                countInrange = 0
            
                for i in range(0,14): # for each column 
                    countInrange = countInrange + 1 
                    countColumn.append(line2[countInrange]) # Add obtained data from field in csv file to a tempary storage array
                
                    
                    output = countColumn # store contence in output
                gotFirstLine = True # One the first line from csv has been obtained set to true
    return output         

            
def inputCSVShoppingList(countHouseNamesWeeks):
    count = 0     
    dayCounter = 0
    weekCounter = 1
    
    for i in countHouseNamesWeeks: # for each house name in countHouseNamesWeeks
        count = count + 1
    
        tempStorageItemQuantity = []
        if (dayCounter < 7): # day counter is smaller than 7 days
            dayCounter = dayCounter + 1 #add day 
        else:
            weekCounter = weekCounter + 1 # add week
            dayCounter = 0 
        
        with open('DATA CWK SHOPPING DATA WEEK 1 FILE B.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
        
            next(csv_reader) # dont include row one of csv
            next(csv_reader) # dont include row two of csv
        
            for line in csv_reader: 
                tempStorageItemQuantity.append(line[count])# append column to tempStorageItemQuantity
        
            houseObjects.append(ShoppingLists(countHouseNamesWeeks[count - 1],weekCounter, tempStorageItemQuantity)) # create object and add data
            


#this function splits an items name into a selection of key words stored in a list
#the keywords are then looped through to 
#this function splits an items name into a selection of key words, those key words are analised and then the item is catagorised and stored in a list(category)
def categorySort():
    print("Category Sort")
    itemNumber = -1
    splitElementCount = -1
    splitItemName = []
    
    categoryTempStoreage = { "Bread" : [], "Milk" : [], "Cheese" : [], "Tomatoes" : [], "Carrots" : [],
    "Potatoes" : [], "Rice" : [], "Butter" : [], "Spread" : [],"Eggs" : [],"Apples" : [],"Onions" : [],
    "Oranges" : [],"Kiwi" : [], "Kitchen" : [], "Toilet" : [], "Tea" : [], "Coffee" : [],"NoSubstatutes" : []}
    
    categoryTempStoreageKey = ["Bread", "Milk", "Cheese", "Tomatoes", "Carrots",
    "Potatoes", "Rice", "Butter", "Spread", "Eggs", "Apples", "Onions",
    "Oranges", "Kiwi", "Kitchen", "Toilet", "Tea", "Coffee","NoSubstatutes"]

    categoryTempStoreageLower = ["bread", "milk", "cheese", "tomatoes", "carrots",
    "potatoes", "rice", "butter", "spread", "eggs", "apples", "onions",
    "oranges", "kiwi", "kitchen", "toilet", "tea", "coffee","NoSubstatutes"]

    for i in shopObjects: # for each item
        itemNumber = itemNumber + 1
        itemName = shopObjects[itemNumber].getItemName() # Gets an items name
        splitItemName = itemName.split(' ') #Splits the item name into keywords
        foundCatagory = False
        for x in splitItemName: #For each keyword 

            splitElementCount = splitElementCount + 1 
            # This next section of code tries to match one of those key words to a catagory.
            #for example if an item has bread as a keyword it's item number will be added to the bread category
            catagoryTmpStoreKeyCount = -1
            
            for i in categoryTempStoreageKey:
                catagoryTmpStoreKeyCount = catagoryTmpStoreKeyCount + 1
                if (splitItemName[splitElementCount] == categoryTempStoreageKey[catagoryTmpStoreKeyCount] or splitItemName[splitElementCount] == categoryTempStoreageLower[catagoryTmpStoreKeyCount]):
                    #categoryTempStoreage[categoryTempStoreageKey[catagoryTmpStoreKeyCount]].append(itemNumber)                               
                    #this next line is for testing
                    categoryTempStoreage[categoryTempStoreageKey[catagoryTmpStoreKeyCount]].append(shopObjects[itemNumber].getItemName())
                    foundCatagory = True
       
        if(foundCatagory == False):# If in no catagory put in NoSubstatutes
            categoryTempStoreage["NoSubstatutes"].append(shopObjects[itemNumber].getItemName()) 
         
        splitElementCount = -1    
    countClassInput = -1 
    for i in categoryTempStoreageKey:# for each catagory
        countClassInput = countClassInput + 1
        catagoryObjects.append(Catagories(categoryTempStoreageKey[countClassInput], categoryTempStoreage[categoryTempStoreageKey[countClassInput]]))# add each catagory from dictionary to class object 

# gives items there item numbers    
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
    return inShops  

# Will combine output of inStore so, for house A1 you may have A,B,A,A,B,A,B,B,A and this function will reduce it to A,B
def minimumStores(StoreShopChoice): # This function finds out what shops each house hold will need to visit
    StoreStoreAmmountA = 0
    StoreStoreAmmountB = 0
    StoreStoreAmmountC = 0
    
    count = 0
    
    logicalChoice = []
    for i in StoreShopChoice:
        if(StoreShopChoice[count] == 'A'):
            StoreStoreAmmountA = StoreStoreAmmountA + 1
           
        elif(StoreShopChoice[count] == 'B'):
            StoreStoreAmmountB = StoreStoreAmmountB + 1
           
        elif(StoreShopChoice[count] == 'C'):
            StoreStoreAmmountC = StoreStoreAmmountC + 1  
            
        count = count + 1
    
    if(StoreStoreAmmountA >= 1):
        logicalChoice.append('A')
    if(StoreStoreAmmountB >= 1):
        logicalChoice.append('B')
    if(StoreStoreAmmountC >= 1):
        logicalChoice.append('C')
    
    return logicalChoice

def proccess():
    print("DADSA Assignment one TASK 1") #Prints project title
    print(" ")
    
    mainCounter = -1
    itemListCounter = -1
    
    tempProccessed = []
    combination = []
    
    for i in houseObjects:# for all houses
        mainCounter = mainCounter + 1
        tempItemListStorage = houseObjects[mainCounter].getItemList()# item required items list
        tempItemListStorage.pop()# Pops the strange ellipsis thing
        for i in tempItemListStorage:# for each item
            itemListCounter = itemListCounter + 1
            
            if (int(tempItemListStorage[itemListCounter]) > 0):# if need to buy item I.E the quantity is greater than 0
               canBeFoundInStore = inStore(itemListCounter)# get the store the item can be bought from
               tempProccessed.append(canBeFoundInStore)# append store to list
               
               itemName = shopObjects[itemListCounter].getItemName()# get the items name
               
               if (canBeFoundInStore == "A"):# if it can be found in store A                  
                   houseObjects[mainCounter].setNeedToBuyShopA(itemName) # add item to the list if items needed to buy from shop A 
                   houseObjects[mainCounter].setNeedToBuyShopAQuantities(tempItemListStorage[itemListCounter])# add quantity to the list if items needed to buy from shop A
                 # each of these if statements is the same as for shop A but obviously appends to there diffrent respective item lists 
               elif(canBeFoundInStore == "B"):
                   houseObjects[mainCounter].setNeedToBuyShopB(itemName) 
                   houseObjects[mainCounter].setNeedToBuyShopBQuantities(tempItemListStorage[itemListCounter])
                   
               elif(canBeFoundInStore == "C"):
                   houseObjects[mainCounter].setNeedToBuyShopC(itemName)
                   houseObjects[mainCounter].setNeedToBuyShopCQuantities(tempItemListStorage[itemListCounter])
                   
                   
        combination = minimumStores(tempProccessed)# find minimum combination
        houseObjects[mainCounter].setStoreCombinations(combination)# set a houses minimum store combinations
        tempProccessed = []# reset list
        itemListCounter = -1
    combination = []

def getItemNumber(item):
    ShopItemNumber = -1
    for m in shopObjects:# for all items
        ShopItemNumber =  ShopItemNumber + 1 # this number is the item number
        if (shopObjects[ShopItemNumber].getItemName() == item):# if items name found in shops is the same as the item being tested
            return ShopItemNumber # return its item number
            
#Handles Substitutions: item swapping
def Swap(itemsRequired,toAvoid,biggestShopItemList):
    newItem = ""
    catagoryCount = -1
    aBiggestShop = ""
    bBiggestShop = ""
    cBiggestShop = ""
    if(biggestShopItemList == "A"): # if house requires the most items from A
        aBiggestShop = "Y"
    elif(biggestShopItemList == "B"): # if house requires the most items from B
        bBiggestShop = "Y"
    elif(biggestShopItemList == "C"): # if house requires the most items from C
        cBiggestShop = "Y"

    for x in catagoryObjects:#for each catagory
        catagoryCount = catagoryCount + 1
        eachItemCountCat = -1
        for z in catagoryObjects[catagoryCount].getItemList(): #for each item in catagory
            eachItemCountCat = eachItemCountCat + 1            
            if(itemsRequired == catagoryObjects[catagoryCount].getItemList()[eachItemCountCat]): # if the item is found in that catagory 
                if(catagoryObjects[catagoryCount].getCatagoryName() == "NoSubstatutes"): # if the item does not have a catagory just return it to be re sorted
                    return itemsRequired # Return same item
                catagoryItemToSwapWith = -1 
                for n in catagoryObjects[catagoryCount].getItemList(): # loops through items finds a diffrent item in that catagory
                    catagoryItemToSwapWith = catagoryItemToSwapWith + 1
                    newItemStores = shopObjects[getItemNumber(catagoryObjects[catagoryCount].getItemList()[catagoryItemToSwapWith])].getItemStores() # gets items stores of new item
                    if(catagoryObjects[catagoryCount].getItemList()[catagoryItemToSwapWith] !=  itemsRequired and newItemStores[0] == aBiggestShop or newItemStores[1] == bBiggestShop or newItemStores[2] == cBiggestShop): # If can be bought from the shop with the most ammount of items
                        return catagoryObjects[catagoryCount].getItemList()[catagoryItemToSwapWith] # return new item

                        
                        
# Called to update required item lists for a given house hold                
def updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC):
     houseObjects[houseCount].replaceNeedToBuyShopA(itemsRequiredA)
     houseObjects[houseCount].replaceNeedToBuyShopB(itemsRequiredB)
     houseObjects[houseCount].replaceNeedToBuyShopC(itemsRequiredC)

# Called to update item quantities for a given house hold
def updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities):
     houseObjects[houseCount].replaceNeedToBuyShopAQuantities(itemsRequiredAQuantities)
     houseObjects[houseCount].replaceNeedToBuyShopBQuantities(itemsRequiredBQuantities)
     houseObjects[houseCount].replaceNeedToBuyShopCQuantities(itemsRequiredCQuantities)
  
#comment
def smallestGreaterThanZero(num1,num2,num3):
    constHigh = 1000 # high value to be set
    if(num1 == 0):
        num1 = constHigh # sets high value so will never be picked
    if(num2 == 0):
        num2 = constHigh # sets high value so will never be picked
    if(num3 == 0):
        num3 = constHigh # sets high value so will never be picked
    
    minimum = min(num1,num2,num3)
    return minimum

def biggestShop(num1,num2,num3):
   biggestValue = max(num1,num2,num3)
   return biggestValue

#This function deals with selecting which item lists need to be substatuted 
"""
Note:
Unfortunetly the code in these if statements (if (smallestA == True), if (smallestB == True), if (smallestC == True))
cant be put into functions as it appends to spesific lists. 
"""
def substitutions(houseCount):
       
    itemsRequiredA = houseObjects[houseCount].getNeedToBuyShopA()
    itemsRequiredB = houseObjects[houseCount].getNeedToBuyShopB()
    itemsRequiredC = houseObjects[houseCount].getNeedToBuyShopC()
    
    itemsRequiredAQuantities = houseObjects[houseCount].getNeedToBuyShopAQuantities()
    itemsRequiredBQuantities = houseObjects[houseCount].getNeedToBuyShopBQuantities()
    itemsRequiredCQuantities = houseObjects[houseCount].getNeedToBuyShopCQuantities()

    biggestShopItemList = ""

    smallestA = False
    smallestB = False
    smallestC = False

    sizeOfA = len(itemsRequiredA)
    sizeOfB = len(itemsRequiredB)
    sizeOfC = len(itemsRequiredC)

    biggestNumber = biggestShop(sizeOfA,sizeOfB,sizeOfC)#gets the shopping list with the highest ammount of items that need to be bought 
    smallestNumber = smallestGreaterThanZero(len(itemsRequiredA),len(itemsRequiredB),len(itemsRequiredC))#gets the shopping list with the smallest ammount of items that need to be bought 

    if(sizeOfA == smallestNumber):# if a shopping list is the smallest then;
        smallestA = True
    elif(sizeOfB == smallestNumber):# if b shopping list is the smallest then;        
        smallestB = True
    elif(sizeOfC == smallestNumber):# if c shopping list is the smallest then;
        smallestC = True

    
    if(sizeOfA == biggestNumber):# if a shopping list is the biggest then;
        biggestShopItemList = "A"
    elif(sizeOfB == biggestNumber):# if b shopping list is the biggest then;         
        biggestShopItemList = "B"
    elif(sizeOfC == biggestNumber):# if c shopping list is the biggest then;
        biggestShopItemList = "C"

    if (smallestA == True):# if a is the smallest
        oldItemAmmountA = -1 
        newItemsA = []
        for i in itemsRequiredA:#for all items required from shop a 
            oldItemAmmountA = oldItemAmmountA + 1
            newItemsA.append(Swap(itemsRequiredA[oldItemAmmountA],"A",biggestShopItemList))# send the item to swap item for a new item to be found and append to new items list
        newItemCountA = -1
        for x in newItemsA: # for each new item found (sort into new shopping list)
            newItemCountA = newItemCountA + 1
            
            itemNumberNewItemA = getItemNumber(str(newItemsA[newItemCountA])) # gets item number of new item
            if(shopObjects[itemNumberNewItemA].getItemStores()[1] == "Y"):# if the item is in store B
                itemsRequiredB.append(newItemsA[newItemCountA])# add item to Store B shopping list
                itemsRequiredBQuantities.append(itemsRequiredAQuantities[newItemCountA])# add item quantity to Store D shopping list
            
            
            elif(shopObjects[itemNumberNewItemA].getItemStores()[2] == "Y" and len(itemsRequiredA) > 0):# if the item is in store C
                itemsRequiredC.append(newItemsA[newItemCountA])# add item to Store C shopping list
                itemsRequiredCQuantities.append(itemsRequiredAQuantities[newItemCountA])# add item quantity to Store C shopping list
        itemsRequiredA = []# Wipe items required from shop A
        itemsRequiredAQuantities = []# Wipe item quantities required from shop A quantities
        updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC)# update these lists  
        updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities)# update these lists

    # Most of the code is repeated from here in this function, read note above function why this can't be put into functions
    if (smallestB == True):# if b is the smallest
        oldItemAmmountB = -1 
        newItemsB = []
        for i in itemsRequiredB:
            oldItemAmmountB = oldItemAmmountB + 1
            newItemsB.append(Swap(itemsRequiredB[oldItemAmmountB],"B",biggestShopItemList))
        newItemCountB = -1
        for x in newItemsB:
            newItemCountB = newItemCountB + 1
            
            itemNumberNewItemB = getItemNumber(str(newItemsB[newItemCountB]))
                
            if(shopObjects[itemNumberNewItemB].getItemStores()[0] == "Y"):
                itemsRequiredA.append(newItemsB[newItemCountB])
                itemsRequiredAQuantities.append(itemsRequiredBQuantities[newItemCountB])
            
            
            elif(shopObjects[itemNumberNewItemB].getItemStores()[1] == "Y" and len(itemsRequiredC) > 0):
                itemsRequiredB.append(newItemsB[newItemCountB])
                itemsRequiredBQuantities.append(itemsRequiredBQuantities[newItemCountB])
        itemsRequiredB = []
        itemsRequiredBQuantities = []
        updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC)
        updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities)

    if (smallestC == True):# if c is the smallest
        oldItemAmmount = -1 
        newItems = []
        for i in itemsRequiredC:
            oldItemAmmount = oldItemAmmount + 1
            newItems.append(Swap(itemsRequiredC[oldItemAmmount],"C",biggestShopItemList))
        newItemCount = -1
        for x in newItems:
            newItemCount = newItemCount + 1
            itemNumberNewItem = getItemNumber(newItems[newItemCount])
                
            if(shopObjects[itemNumberNewItem].getItemStores()[0] == "Y"):
                itemsRequiredA.append(newItems[newItemCount])
                itemsRequiredAQuantities.append(itemsRequiredCQuantities[newItemCount])
            
            elif(shopObjects[itemNumberNewItem].getItemStores()[1] == "Y"):
                itemsRequiredB.append(newItems[newItemCount])
                itemsRequiredBQuantities.append(itemsRequiredCQuantities[newItemCount])
        itemsRequiredC = []
        itemsRequiredCQuantities = []
        updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC)
        updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities)

#This function re-calculates the minimum shops required to visit by each house hold after the subsitution function has been run                                                    
def recalculateMinShops():
    houseCount = -1
    for i in houseObjects:
        houseCount = houseCount + 1
        completeMinimumStores = []
        if (len(houseObjects[houseCount].getNeedToBuyShopA()) > 0):# if house requires items from shop A
            completeMinimumStores.append("A") # add A to shop required list
        if (len(houseObjects[houseCount].getNeedToBuyShopB()) > 0):
            completeMinimumStores.append("B")
        if (len(houseObjects[houseCount].getNeedToBuyShopC()) > 0):
            completeMinimumStores.append("C")
        houseObjects[houseCount].replaceMinimalCombinations(completeMinimumStores)# update each house hold object to reflect these changes
#This function finds out if a houses minimum combination is already in combinations.      
def matchCombinations(combinations, minimumCombos):
    combinationCount = -1
    for n in combinations:# for all combinations
        combinationCount = combinationCount + 1
        combinationShopCount = -1
        match = 0
        for x in combinations[combinationCount]:# for each shop in combination
            combinationShopCount = combinationShopCount + 1
            if (minimumCombos[combinationShopCount] == combinations[combinationCount][combinationShopCount]):# if a shop is in both minimum combination and combination
                    match = match + 1 # increment how many matches there have been
            if(match == len(combinations[combinationCount])):# if both shops match 
                return True # return true
    return False # if it goes through all combinations and does not find a match return false

#finds shops that will need to be visited by all houses
def commonShopCombinations(getWeek):
    shoppingCountWeekOne = -1
    combinations = []
    for i in houseObjects:# for all houses
        shoppingCountWeekOne = shoppingCountWeekOne + 1
        if (houseObjects[shoppingCountWeekOne].getWeek() == getWeek):
            minimumCombos = houseObjects[shoppingCountWeekOne].getMinimalCombinations()# get minimum combinations        
            if(len(combinations) == 0):# if there are no shopping combinations in combination list
                combinations.append(minimumCombos)# add first combination 
            else:
                matchCondition = False
                matchCondition = matchCombinations(combinations, minimumCombos)# find a match 
                if(matchCondition == True):# the moment it finds a match end iterate the loop by 1
                    continue
                if(matchCondition == False):# if it never finds a match add to combinations
                    combinations.append(minimumCombos)
                    continue
    return combinations  

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
#function merges all shops required to visit into one list
# each week is split into two week periods 
#Appends all shops in given shop combinations for a week into one list I.E [[A,B],[D,B]] to [A,B,D,B]    
def mergeShopList(week, weekCombinations):
    listOfShops = []
    weekCombinationsCount = -1
    for i in weekCombinations:# for each shop set
        weekCombinationsCount =  weekCombinationsCount + 1
        weekCombinationsShopCount = -1
        for x in weekCombinations[weekCombinationsCount]:# for each shop in set
            weekCombinationsShopCount = weekCombinationsShopCount + 1
            listOfShops.append(weekCombinations[weekCombinationsCount][weekCombinationsShopCount]) # append to new list
    return listOfShops
# this function pre adds all shops to the shopping list
def shoppingSceduleAddShops(week, listOfShops):
    listOfshopCount = -1
    for z in listOfShops: # for each shop 
        listOfshopCount = listOfshopCount + 1
        shoppingScheduleCount = -1
        for b in shoppingScheduleObjects:# for each day in shopping list
            shoppingScheduleCount = shoppingScheduleCount + 1
            if(shoppingScheduleObjects[shoppingScheduleCount].getWeekShoppingSchedule() == week):# only append to the shopping list in the week spesified 
                if(shoppingScheduleObjects[shoppingScheduleCount].getShopToBuyFrom() == ""): # if the shop to buy field is blank then
                    shoppingScheduleObjects[shoppingScheduleCount].setShopToBuyFrom(listOfShops[listOfshopCount])# set shop
                    break

# gets shopping list from shop class based on which shop is parsed in 
def getShoppingFromShop(shop, houseCount):
    if (shop == "A"):
       return houseObjects[houseCount].getNeedToBuyShopA()
    elif (shop == "B"):
       return houseObjects[houseCount].getNeedToBuyShopB()
    elif (shop == "C"):
       return houseObjects[houseCount].getNeedToBuyShopC()
    else:
        print("Error no shop selected in 'getShoppingFromShop' function")
# gets shopping quantity list from shop class based on which shop is parsed in 
def getShoppingFromShopQuantities(shop, houseCount):
    if (shop == "A"):
       return houseObjects[houseCount].getNeedToBuyShopAQuantities()
    elif (shop == "B"):
       return houseObjects[houseCount].getNeedToBuyShopBQuantities()
    elif (shop == "C"):
       return houseObjects[houseCount].getNeedToBuyShopCQuantities()
    else:
        print("Error no shop selected in 'getShoppingFromShop' function")

#creates shopping list using all data gathered
def shoppingSceduleShoppingSort(week):
    houseObjectsCount = -1
    for i in houseObjects:# for each house
        houseObjectsCount = houseObjectsCount + 1
        shoppingScheduleObjectsCount = -1
        if (houseObjects[houseObjectsCount].getWeek() == week):# if the house is in the week spesified 
            for x in shoppingScheduleObjects:# for each day in shopping scedule
                shoppingScheduleObjectsCount = shoppingScheduleObjectsCount + 1
                if (shoppingScheduleObjects[shoppingScheduleObjectsCount].getWeekShoppingSchedule() == week):# if shoppng scedule day is in the week spesified 
                     # (code bellow this) if shop required for each house match the shopping schedule shop then add both the items and item quantity to it do this also for the next shop in the minimum shops list for a given house
                    if(houseObjects[houseObjectsCount].getMinimalCombinations()[0] == shoppingScheduleObjects[shoppingScheduleObjectsCount].getShopToBuyFrom() and houseObjects[houseObjectsCount].getMinimalCombinations()[1] == shoppingScheduleObjects[shoppingScheduleObjectsCount + 1].getShopToBuyFrom()):
                        shoppingScheduleObjects[shoppingScheduleObjectsCount].setShopingToBuy(getShoppingFromShop(houseObjects[houseObjectsCount].getMinimalCombinations()[0], houseObjectsCount))
                        shoppingScheduleObjects[shoppingScheduleObjectsCount + 1].setShopingToBuy(getShoppingFromShop(houseObjects[houseObjectsCount].getMinimalCombinations()[1], houseObjectsCount))

                        shoppingScheduleObjects[shoppingScheduleObjectsCount].setShoppingQuantities(getShoppingFromShopQuantities(houseObjects[houseObjectsCount].getMinimalCombinations()[0], houseObjectsCount))
                        shoppingScheduleObjects[shoppingScheduleObjectsCount + 1].setShoppingQuantities(getShoppingFromShopQuantities(houseObjects[houseObjectsCount].getMinimalCombinations()[1], houseObjectsCount))
            
                        deliveryObjects[shoppingScheduleObjectsCount + 1].setDeliverySchedule(houseObjects[houseObjectsCount].getHouseName())# add house name to delivery scedule for next day.
                        break
     
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
            shopping = []
            shoppingAmmount = [] 
            
            shopping =  shopping + shoppingScheduleObjects[shoppingSceduleCount].getShopingToBuy()
            shoppingAmmount = shoppingAmmount + shoppingScheduleObjects[shoppingSceduleCount].getShoppingQuantities()
            
            shoppingCount = -1
            for i in shopping:
                shoppingCount = shoppingCount + 1
                print("Item: " + str(shopping[shoppingCount]))
                print("Ammount: " + str(shoppingAmmount[shoppingCount]))
                print(" ")
            print(" ")
            print("===============================================")
            input("Press enter for next: ")
            print(" ")

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
             
      
def main():
    print("DADSA Assignment one TASK 1") #Prints project title
    print(" ")
    # ==================== this section of function calls handles data intake and sorting ===================================
    inputCSVShopList() 
    countHouseNamesWeeks = inputCSVHouseNames()
    inputCSVShoppingList(countHouseNamesWeeks)
    categorySort() # Implement for task 2
    giveItemNumber() 
    replace()    
    proccess()
    #===========================Section End============================
    
    #===============each time this section of code is run in removes one shop from each houses minimum shop list by substituting ===============
    for x in range(0, 2):
        houseCount = -1
        for i in houseObjects:
            houseCount = houseCount + 1
            if (len(houseObjects[houseCount].getMinimalCombinations()) > 2):  # if house already has 2 shops only skip this itteration
                substitutions(houseCount) # Implement for task 2
        recalculateMinShops()
    #==================================================================Section End==========================================================================
    
    # ===================this next section of function calls deals with schedule creation =======================
    addDays()
    shoppingSceduleAddShops(1,mergeShopList(1,commonShopCombinations(1))) 
    shoppingSceduleAddShops(2,mergeShopList(2,commonShopCombinations(2))) 

    shoppingSceduleShoppingSort(1)
    shoppingSceduleShoppingSort(2)
    #==============Section End===================

    #================= outputs results ======================        
    outputScedule()     
    outputDelivery()  
    #==============Section End===================      
main()
     
        
        
        
        
        
        


     