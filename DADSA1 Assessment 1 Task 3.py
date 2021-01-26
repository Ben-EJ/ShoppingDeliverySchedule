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
3. tidy up
4. fix bug
5. comment
6.
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
        return self.needToBuyShopDQuantities
    
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
    
    def replaceMinimalCombinations(self, minimalCombinations):
        self.minimalCombinations = minimalCombinations

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
    with open('DATA CWK SHOPPING DATA WEEK 7 FILE A.csv', 'r') as csv_file1:
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
    with open('DATA CWK SHOPPING DATA WEEK 7 FILE B.csv', 'r') as csv_file2:
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
        if (count > 16): # if hits 16 houses sets week counter to week 2
            weekCounter = 2 # add week
    
        with open('DATA CWK SHOPPING DATA WEEK 7 FILE B.csv', 'r') as csv_file:
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
    for i in categoryTempStoreageKey:
        countClassInput = countClassInput + 1
        catagoryObjects.append(Catagories(categoryTempStoreageKey[countClassInput], categoryTempStoreage[categoryTempStoreageKey[countClassInput]]))

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
    if (tempStoreShopList[3] == 'Y'):# if in store D
        return "D" # return store that is in I.E store D
    elif (tempStoreShopList[0] == 'Y'):
        return"A"
    elif (tempStoreShopList[1] == 'Y'):
        return "B"
    elif (tempStoreShopList[2] == 'Y'):
        return "C"
    else:
        print("Error Item not in any stores")

# Will combine output of inStore so, for house A1 you may have A,B,A,A,B,A,B,B,A and this function will reduce it to A,B
def minimumStores(StoreShopChoice): # This function finds out what shops each house hold will need to visit
    StoreStoreAmmountA = 0
    StoreStoreAmmountB = 0
    StoreStoreAmmountC = 0
    StoreStoreAmmountD = 0
    count = 0
    
    logicalChoice = []
    for i in StoreShopChoice: #for each of the shops that have been flag as need to visit
        if(StoreShopChoice[count] == 'D'):# if required to go to store D
            StoreStoreAmmountD = StoreStoreAmmountD + 1 # ADD one to store D counter

        elif(StoreShopChoice[count] == 'A'):
            StoreStoreAmmountA = StoreStoreAmmountA + 1
           
        elif(StoreShopChoice[count] == 'B'):
            StoreStoreAmmountB = StoreStoreAmmountB + 1
           
        elif(StoreShopChoice[count] == 'C'):
            StoreStoreAmmountC = StoreStoreAmmountC + 1          
        count = count + 1
    if(StoreStoreAmmountD >= 1):# if store D counter is greater than one then we definately are required to go to store D
        logicalChoice.append('D')# Append store D to minimum stores list
    if(StoreStoreAmmountA >= 1):
        logicalChoice.append('A')
    if(StoreStoreAmmountB >= 1):
        logicalChoice.append('B')
    if(StoreStoreAmmountC >= 1):
        logicalChoice.append('C')
    
    return logicalChoice # return minimum stores list for a given house

#Main Data proccessing function, uses minimumStores and inStore functionss 
def proccess():    
    mainCounter = -1
    itemListCounter = -1
    
    tempProccessed = []
    combination = []
    
    for i in houseObjects:# for all houses
        mainCounter = mainCounter + 1
        tempItemListStorage = houseObjects[mainCounter].getItemList() # item required items list
        tempItemListStorage.pop()# Pops the strange ellipsis 
        for i in tempItemListStorage:# for each item
            itemListCounter = itemListCounter + 1
            
            if (int(tempItemListStorage[itemListCounter]) > 0): # if need to buy item I.E the quantity is greater than 0
               canBeFoundInStore = inStore(itemListCounter) # get the store the item can be bought from
               tempProccessed.append(canBeFoundInStore)# append store to list
               
               itemName = shopObjects[itemListCounter].getItemName() # get the items name
               if(canBeFoundInStore == "D"): # if it can be found in store D
                   
                   houseObjects[mainCounter].setNeedToBuyShopD(itemName) # add item to the list if items needed to buy from shop D    
                   houseObjects[mainCounter].setNeedToBuyShopDQuantities(tempItemListStorage[itemListCounter])# add quantity to the list if items needed to buy from shop D 
               # each of these if statements is the same as for shop D but obviously appends to there diffrent respective item lists 
               elif (canBeFoundInStore == "A"):                   
                   houseObjects[mainCounter].setNeedToBuyShopA(itemName) 
                   houseObjects[mainCounter].setNeedToBuyShopAQuantities(tempItemListStorage[itemListCounter])

               elif(canBeFoundInStore == "B"):
                   houseObjects[mainCounter].setNeedToBuyShopB(itemName) 
                   houseObjects[mainCounter].setNeedToBuyShopBQuantities(tempItemListStorage[itemListCounter])
                   
               elif(canBeFoundInStore == "C"):
                   houseObjects[mainCounter].setNeedToBuyShopC(itemName)
                   houseObjects[mainCounter].setNeedToBuyShopCQuantities(tempItemListStorage[itemListCounter])
               else:
                   print("Error 1: in proccess")   

        combination = minimumStores(tempProccessed)
        houseObjects[mainCounter].setStoreCombinations(combination)
        tempProccessed = []
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
                    if(catagoryObjects[catagoryCount].getItemList()[catagoryItemToSwapWith] !=  itemsRequired and newItemStores[0] == aBiggestShop or newItemStores[1] == bBiggestShop or newItemStores[3] == cBiggestShop): # If can be bought from the shop with the most ammount of items
                        return catagoryObjects[catagoryCount].getItemList()[catagoryItemToSwapWith] # return new item

                        
                        
# Called to update required item lists for a given house hold                
def updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC,itemsRequiredD):
     houseObjects[houseCount].replaceNeedToBuyShopA(itemsRequiredA)
     houseObjects[houseCount].replaceNeedToBuyShopB(itemsRequiredB)
     houseObjects[houseCount].replaceNeedToBuyShopC(itemsRequiredC)
     houseObjects[houseCount].replaceNeedToBuyShopD(itemsRequiredD)
# Called to update item quantities for a given house hold
def updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities,itemsRequiredDQuantities):
     houseObjects[houseCount].replaceNeedToBuyShopAQuantities(itemsRequiredAQuantities)
     houseObjects[houseCount].replaceNeedToBuyShopBQuantities(itemsRequiredBQuantities)
     houseObjects[houseCount].replaceNeedToBuyShopCQuantities(itemsRequiredCQuantities)
     houseObjects[houseCount].replaceNeedToBuyShopDQuantities(itemsRequiredDQuantities)    
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
def substitutions(runNumber):
    houseCount = -1
     
    for i in houseObjects: #for each house
        
        houseCount = houseCount + 1
        if (len(houseObjects[houseCount].getMinimalCombinations()) == 2):  # if house already has 2 shops only skip this itteration
            continue 

        itemsRequiredA = houseObjects[houseCount].getNeedToBuyShopA()
        itemsRequiredB = houseObjects[houseCount].getNeedToBuyShopB()
        itemsRequiredC = houseObjects[houseCount].getNeedToBuyShopC()
        itemsRequiredD = houseObjects[houseCount].getNeedToBuyShopD()
        
        itemsRequiredAQuantities = houseObjects[houseCount].getNeedToBuyShopAQuantities()
        itemsRequiredBQuantities = houseObjects[houseCount].getNeedToBuyShopBQuantities()
        itemsRequiredCQuantities = houseObjects[houseCount].getNeedToBuyShopCQuantities()
        itemsRequiredDQuantities = houseObjects[houseCount].getNeedToBuyShopDQuantities()

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
                if(shopObjects[itemNumberNewItemA].getItemStores()[3] == "Y"): # if the item is in store D
                    itemsRequiredD.append(newItemsA[newItemCountA])# add item to Store D shopping list
                    itemsRequiredDQuantities.append(itemsRequiredAQuantities[newItemCountA])# add item quantity to Store D shopping list
                    
                elif(shopObjects[itemNumberNewItemA].getItemStores()[1] == "Y"):# if the item is in store B
                    itemsRequiredB.append(newItemsA[newItemCountA])# add item to Store B shopping list
                    itemsRequiredBQuantities.append(itemsRequiredAQuantities[newItemCountA])# add item quantity to Store D shopping list
                   
                   
                elif(shopObjects[itemNumberNewItemA].getItemStores()[2] == "Y" and len(itemsRequiredA) > 0):# if the item is in store C
                    itemsRequiredC.append(newItemsA[newItemCountA])# add item to Store C shopping list
                    itemsRequiredCQuantities.append(itemsRequiredAQuantities[newItemCountA])# add item quantity to Store C shopping list
            itemsRequiredA = []# Wipe items required from shop A
            itemsRequiredAQuantities = []# Wipe item quantities required from shop A quantities
            updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC,itemsRequiredD)# update these lists  
            updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities,itemsRequiredDQuantities)# update these lists

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
                if(shopObjects[itemNumberNewItemB].getItemStores()[3] == "Y"):
                    itemsRequiredD.append(newItemsB[newItemCountB])
                    itemsRequiredDQuantities.append(itemsRequiredBQuantities[newItemCountB])
                    
                elif(shopObjects[itemNumberNewItemB].getItemStores()[0] == "Y"):
                    itemsRequiredA.append(newItemsB[newItemCountB])
                    itemsRequiredAQuantities.append(itemsRequiredBQuantities[newItemCountB])
                   
                   
                elif(shopObjects[itemNumberNewItemB].getItemStores()[1] == "Y" and len(itemsRequiredC) > 0):
                    itemsRequiredB.append(newItemsB[newItemCountB])
                    itemsRequiredBQuantities.append(itemsRequiredBQuantities[newItemCountB])
            itemsRequiredB = []
            itemsRequiredBQuantities = []
            updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC,itemsRequiredD)
            updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities,itemsRequiredDQuantities)

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
                
                if(shopObjects[itemNumberNewItem].getItemStores()[3] == "Y" and len(itemsRequiredB) == 0):
                    itemsRequiredD.append(newItems[newItemCount])
                    itemsRequiredDQuantities.append(itemsRequiredCQuantities[newItemCount])
                    
                elif(shopObjects[itemNumberNewItem].getItemStores()[0] == "Y"):
                    itemsRequiredA.append(newItems[newItemCount])
                    itemsRequiredAQuantities.append(itemsRequiredCQuantities[newItemCount])
                   
                elif(shopObjects[itemNumberNewItem].getItemStores()[1] == "Y"):
                    itemsRequiredB.append(newItems[newItemCount])
                    itemsRequiredBQuantities.append(itemsRequiredCQuantities[newItemCount])
            itemsRequiredC = []
            itemsRequiredCQuantities = []
            updateItems(houseCount,itemsRequiredA,itemsRequiredB,itemsRequiredC,itemsRequiredD)
            updateQuantities(houseCount,itemsRequiredAQuantities,itemsRequiredBQuantities,itemsRequiredCQuantities,itemsRequiredDQuantities)

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
        if (len(houseObjects[houseCount].getNeedToBuyShopD()) > 0):
            completeMinimumStores.append("D")
        houseObjects[houseCount].replaceMinimalCombinations(completeMinimumStores)# update each house hold object to reflect these changes

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
    print(combinations)      
             
def shoppingScedule(week, weekCombinations):
    if(len(weekCombinations) == 2 and len(weekCombinations[0]) == 2):
        houseCount = -1
        for i in houseObjects:# for each house
            houseCount = houseCount + 1
            if(houseObjects[houseCount].getWeek() == week):# if house is in week
                dayCount = -1
                for x in shoppingScheduleObjects:# for each day
                    dayCount =  dayCount + 1
                    
                    if (houseObjects[houseCount].getMinimalCombinations()[0] == weekCombinations[0]):
                            shoppingScheduleObjects[0].setShopToBuyFrom(weekCombinations[0][0])
                            shoppingScheduleObjects[0].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopA())
                            shoppingScheduleObjects[0].setShoppingQuantities(houseObjects[shoppingCountWeekOne].getNeedToBuyShopAQuantities())
                    
                    if (houseObjects[houseCount].getMinimalCombinations()[1] == weekCombinations[1]):
                            shoppingScheduleObjects[1].setShopToBuyFrom("B")
                            shoppingScheduleObjects[1].setShopingToBuy(houseObjects[shoppingCountWeekOne].getNeedToBuyShopB())
                            shoppingScheduleObjects[1].setShoppingQuantities(houseObjects[shoppingCountWeekOne].getNeedToBuyShopBQuantities())
                    deliveryObjects[1].setDeliverySchedule(houseObjects[shoppingCountWeekOne].getHouseName())

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
    count = -1
    for i in catagoryObjects:
        count =  count + 1
        print("===================================================================")
        print("Catagory: " + catagoryObjects[count].getCatagoryName()) 
        print("Item Numbers")     
        print(catagoryObjects[count].getItemList())
        print("===================================================================") 
        print(" ")
#Returns house objects that are in week 1

#runs all other functions    
def main():
    print("DADSA Assignment one TASK 1") #Prints project title
    print(" ")
    inputCSVShopList() 
    countHouseNamesWeeks = inputCSVHouseNames()
    countHouseNamesWeeks.pop(0)
    inputCSVShoppingList(countHouseNamesWeeks)
    categorySort() # Implement for task 2
    giveItemNumber() 
    replace()    
    proccess()
    substitutions(1) # Implement for task 2
    recalculateMinShops()
    substitutions(2)
    recalculateMinShops()
    addDays()
    commonShopCombinations(1)     
    commonShopCombinations(2)
     
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

     
        
        
        


     