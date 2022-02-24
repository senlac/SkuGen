##Title: Options Builder
##Description: Turn a list of items and attributes into every possible item
##Author: Harry Calder 2022

import csv
from fileinput import filename
import itertools
import tkinter as tk
from tkinter import filedialog
import sys
import pathlib

window = tk.Tk()
window.withdraw()

tk.messagebox.showinfo(title="Choose File", message="Please Choose a File")
filepath = filedialog.askopenfilename()
appPath = str(pathlib.Path(sys.argv[0]).parent)

OptionsArray = []
ItemArray = []
AttributeArray = []
#Needs to be a 3D Array 1D Item, 2D Attributes, 3D Options 



##Iterate through array
##If item changes, add value to OptionsArray[x][][]
##If attribute changes, add value to OptionsArray[][x][]
##If neither changes, add value to OptionsArray[][][x]

with open(filepath) as sourcefile:
    csv_reader = csv.reader(sourcefile, delimiter=',')
    line_count = 0
    current_item = ""
    current_attribute = ""
    item_count = 0
    option_count = 0
    
    i = -1
    a = -1
    o = -1

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            o += 1
            if row[1] != current_attribute or row[0] != current_item: 
                a += 1
                o = 0
                current_attribute = row[1]
                if row[0] != current_item: 
                    i += 1
                    a = 0
                    o = 0
                    current_item = row[0]
                    ItemArray.append(current_item)
                    AttributeArray.append([])
                    OptionsArray.append([])

                AttributeArray[i].append(row[1])
                OptionsArray[i].append([])
                
            OptionsArray[i][a].append(row[2])
            

newItems = []
i = 0


for items in OptionsArray:
    AllCombos = list(itertools.product(*OptionsArray[i]))
    NewCombos = []

    for Combo in AllCombos:
        AsList = list(Combo)
        AsList.insert(0,ItemArray[i])
        NewCombos.append(AsList)
       

    AttributeArray[i].insert(0,"Item Code")
    NewCombos.insert(0,AttributeArray[i])
    newItems.append(NewCombos)
    i += 1

   
tk.messagebox.showinfo(title="Choose Folder", message="Please choose or create a folder to save results to")
folderPath = filedialog.askdirectory()

for item in newItems:
    fileName = str(item[1][0] + '.csv').replace(" ","_")
    filePath = str(folderPath +"/"+ fileName)
    
    with open(filePath,'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(item)
tk.messagebox.showinfo(title="Job Complete", message="Selected Folder has been populated")