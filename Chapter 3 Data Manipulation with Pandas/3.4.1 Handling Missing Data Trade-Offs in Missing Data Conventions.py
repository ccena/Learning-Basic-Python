# -*- coding: utf-8 -*-
"""
The difference between data found in many tutorials and data in the real world 
is that real-world data is rarely clean and homogeneous. In particular, many 
interesting datasets will have some amount of data missing. To make matters 
even more complicated, different data sources may indicate missing data 
in different ways.
"""

# Missing data in general is usually given as null, NaN, or NA values.

message = 'Trade-Offs in Missing Data Conventions'
print(message.upper())
# A number of schemes have been developed to indicate the presence of missing
# data in a table or DataFrame
print('Two of the most common strategies are:')
print('1. A mask that globally indicates missing values')
print('\t A mask might be a separate Boolean array, or it may involve')
print('\t appropriation of one bit in the data representation to locally indicate')
print('\t the null status of a value')
message = '\t Cons:a separate mask array requires allocation of additional\n' 
message += '\t \t \t Boolean array, which adds overhead in storage and computation'
print(message)

print('2. Choosing a sentinel value that indicates a missing entry')
print('\t The sentinel approach could be some data-scientific convention')
print('\t such as indicating a missing integer value with -9999')
print('\t or it can be a more global convention, such as indicating a missing')
print('\t floating-point value with NaN')
message = '\t Cons: This method reduces the range of valid values that can be represented \n'
message += '\t \t \t and may require extra logic in CPU and GPU arithmetic.'
print(message)

