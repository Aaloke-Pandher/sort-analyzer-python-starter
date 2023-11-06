# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# Functions 
def main():
    print("Goat Lunch")
# Insertion Sort
def insertionSort(list):
    for i in range(1, len(list)):
        insertVal = list[i] 
        insertPos = i - 1  

        while(insertPos >= 0 and list[insertPos] > insertVal):
            list[insertPos + 1] = list[insertPos]
            insertPos -= 1
        list[insertPos + 1] = insertVal 

# Selection Sort 
def selectionSort(list):
    for i in range(len(list)):
        minPosition = i 
        for j in range(minPosition + 1, len(list)): 
            if list[j] < list[minPosition]:
                minPosition = j
        list[minPosition], list[i] = list[i], list[minPosition]  

# Bubble Sort 
def bubbleSort(list):
    listLength = len(list)
    for i in range(listLength - 1): 
        for j in range(listLength - i - 1): 
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j] 

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])

main()

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
