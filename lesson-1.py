#To make things easier, I saved the data file and raw code file in the same folder (or working directory).
#Once the file is saved to the same file, it makes it easy to right-click and copy file path when impoorting.
#Instal pandas function to allow for data importation.
"""To install pandas, create a new terminal and type 'python -m pip install pandas' after the file path."""
#I am importing the 'Living Costs and Food Survey 2013' dataset.
#File name is saved as file.


import pandas as pd
file = pd.read_csv(r'C:/Users/OWNER/Documents/Python/Lesson-1/lcfs_2013.csv') 
"""Ensure to convert '\' to '/' before running the code."""

print(file)

#select the code and run; the file should show up in the output tab.