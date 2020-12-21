This is the analytics project code of Aishwarya Manojkumar's (amm1559) and Emily Liang's (sl6325) Processing Big Data for Analytics Applications final project.

The raw US president and US economy data are located in the "Raw Econ and President Data" folder. The source code to run is in the "Source Code" folder. The screen shots of our analytics running is in the "Screen Shots" folder. 

Before running the code in the "Code" folder, please change the file paths for the data being read in to the appropriate file path on your computer. Please also have pandas for Python imported.

The commands to ingest the data are also located in the "Code" file as a text file.

To run the source code, please run on a Python IDE (ex. IDLE or PyCharm). There is no user input required. The program will first output "input1.txt". This is the cleaned data that will then be put into the MapReduce code to output our analytics results in mapper.txt and reducer.txt (the results of our mapper and reducer respectively).

All of the data was found from the following websites:

https://qrc.depaul.edu/Excel_Files/Presidents.xls
https://fred.stlouisfed.org/series/GDPC1
https://fred.stlouisfed.org/series/CPIAUCSL
https://fred.stlouisfed.org/series/UNRATE

