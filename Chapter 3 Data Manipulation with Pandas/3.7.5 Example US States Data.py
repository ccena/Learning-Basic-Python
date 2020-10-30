# -*- coding: utf-8 -*-
"""
Merge and join operations come up most often when one is combining data from
different sources.
"""
import pandas as pd

pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')
print('First five data in Population: '); print(pop.head()); print('')
print('First five data in Area: '); print(areas.head()); print('')
print('First five data in Abbreviation: '); print(abbrevs.head()); print('')

print('Many-to-one merge gives full state name in the population DataFrame.')
merged = pd.merge(pop, abbrevs, how='outer', 
                  left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', axis = 1)
print(merged.head())
print('Checking for Any Mismatches after Merging')
print(merged.isnull().any())
print('Some of the population info is null:') #Subset of the data
null_pop = merged[merged['population'].isnull()]
print(null_pop.head()) 
print('')
null_state = merged.loc[merged['state'].isnull(), 'state/region']
print(null_state.unique())

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
print(merged.isnull().any())

print('Adding the data for area:')
final = pd.merge(merged, areas, on='state', how='left')
print(final.head()); print('')

print('Checking for Any Mismatches after Merging')
print(final.isnull().any()) #The area is mismatched

print('Determining the regions ignored:')
null_area = final['state'][final['area (sq. mi)'].isnull()]
print(null_area.unique()); print('')

# drop the null values because the population density of the entire 
# United States is not relevant
final.dropna(inplace=True)
print('First five data of the DataFrame:')
print(final.head()); print('')
print('Final Check for Mismatches:')
print(final.isnull().any())
print('Now we have all the data we need!'); print('')

# We’ll use the query() function to select the portion of the data
# corresponding with the year 2000, and the total population
data2010 = final.query("year == 2010 & ages == 'total'")
print('Extracting the data from year 2010:')
print(data2010.head()); print('')

data2010.set_index('state', inplace=True)
#Calculating the density for the 2010 dataset
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)
print('First 5 values of the density:')
print(density.head()); print('')
print('Last 5 values of the density:')
print(density.tail())
# We see that the least dense state, by far, is Alaska, averaging slightly 
# over one resident per square mile.
