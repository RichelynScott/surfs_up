# Mod 9 – Advanced Data Storage & Retrieval W/ SQLite & SQLAlchemy – Surf’s Up
Program In Use: Jupyter Notebook, VS Code, GitHub
### Overview of Analysis 
The purpose of this analysis was to determine temperature trends from all years in our data for the months of June and December. That data was converted to a dataframe that we pulled the summary statistics from for each to identify the key differences in weather between June and December.
### Results
-In deliverable 1, we were able to take data from the Hawaii.sqlite to produce a local database using SQLite and SQLAlchemy to pull the relevant data for June (date and temperature data) via a query to create a new list to then convert into a dataframe via panda, and then pull the summary statistics for June. 

![June Temps](https://github.com/RichelynScott/surfs_up/blob/main/June%20Summary%20Statistics%20.png)


-In deliverable 2, we did the same as in deliverable 1 to take data from the Hawaii.sqlite to produce a local database using SQLite and SQLAlchemy to pull the relevant data for December (date and temperature data) via a query to create a new list to then convert into a dataframe via panda, and then pull the summary statistics for December. 

![Dec Temps](https://github.com/RichelynScott/surfs_up/blob/main/December%20Summary%20Statistics.png)


* June had a higher average temperature by about 4 degrees with December’s average being 71.04 and Junes average being 74.94.
* Both June and December were able to produce maximum temperatures and an upper quartile range of temperatures that did not vary much and were from mid 70’s to mid 80’s
* December had the lower set of temperatures from minimum to the lower quartile range by about 4-10 degrees.

### Summary

The goal of this analysis was to determine if a surf shop/ice cream shop would be viable to open in Oahu, Hawaii based on temperatures and other weather data. Based on the statistics we gathered in this analysis we can definitively determine that from the summer months of June to winter months of December, the temperatures do not vary all too much and can consistently provide an appropriate range of temperature to have a viable year round shop that is warm, rarely too cold or too hot as temperatures usually ranged from the 60’s to the low 80’s. 
