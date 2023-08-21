# Diabetes calculator
import matplotlib.pyplot as plt # Needed to graph results through the day
import json # Operates as a savefile for the previous day's data
import os # Checks if a savefile exists to avoid crashing

path = "savefile.json" # This code checks if the savefile previously exists or it notifies the user to use the program at least once 
if os.path.exists(path) == True:
    with open("savefile.json", "r") as savedata:
        prevSaveData = json.load(savedata)
else:
    print("No save file exists, use this program once for a save file")

firstValue = float(input("Enter your first test result of the day:\n")) # Variables saving user input for calculating average
secondValue = float(input("Enter your second test result of the day:\n"))
thirdValue = float(input("Enter your third test result of the day:\n"))
fourthValue = float(input("Enter your fourth test result of the day:\n"))
print("Average result of the day is:", (firstValue + secondValue + thirdValue + fourthValue) / 4)

jsonSavingData = { # Dictionary to save data to json for later use 
    "First Value": firstValue,
    "Second Value": secondValue,
    "Third Value": thirdValue,
    "Fourth Value": fourthValue
}

f = plt.figure(1) # Creates graph for this current program's data
yAxis = [firstValue, secondValue, thirdValue, fourthValue]
xAxis = ["Breakfast", "Lunch", "Snack", "Dinner"]
plt.title("Test results over the day")
plt.ylabel("Test Result in Blood Sugar Levels")
plt.xlabel("Time of Test")
plt.plot(xAxis,yAxis)
plt.annotate(firstValue, xy =("Breakfast", firstValue))
plt.annotate(secondValue, xy =("Lunch", secondValue))
plt.annotate(thirdValue, xy =("Snack", thirdValue))
plt.annotate(fourthValue, xy =("Dinner", fourthValue))
plt.grid(True)

if os.path.exists(path) == True:
    f = plt.figure(2) # Creates graph for the previous program's data/savefile
    yAxis = [prevSaveData["First Value"], prevSaveData["Second Value"], prevSaveData["Third Value"], prevSaveData["Fourth Value"]]
    xAxis = ["Breakfast", "Lunch", "Snack", "Dinner"]
    plt.title("Test results over yesterday/last test")
    plt.ylabel("Test Result in Blood Sugar Levels")
    plt.xlabel("Time of Test")
    plt.plot(xAxis,yAxis)
    plt.annotate(prevSaveData["First Value"], xy =("Breakfast", prevSaveData["First Value"]))
    plt.annotate(prevSaveData["Second Value"], xy =("Lunch", prevSaveData["Second Value"]))
    plt.annotate(prevSaveData["Third Value"], xy =("Snack", prevSaveData["Third Value"]))
    plt.annotate(prevSaveData["Fourth Value"], xy =("Dinner", prevSaveData["Fourth Value"]))
    plt.grid(True)

with open("savefile.json", "w") as savefile: # Saving dictionary to json file
    json.dump(jsonSavingData, savefile)

plt.show() 