# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:09:59 2024

@author: sisiphosathula
"""

import pandas 

file = pandas.read_csv("movie_data.csv")

print(file) 
print(file.describe())

print(file['Revenue (Millions)'].mean())
print(file['Rating'].max())
print(file['Title'], file['Year'])
#print(file.sorted_values(by=['Rating'], axis=1))
#print(file[['Title'], file['Rating'] > 9])

sp = file['Title'], file['Year'] 

#move only title and rating into one dataframe called sp and sorting by ranting

sp = file['Title'], file['Rating']
sp_1 = pd.DataFrame(sp)
print(sp_1.sort_values(by=['Rating'], axis=1))

