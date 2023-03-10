# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:04:23 2023

@author: Justus v. Samson-Himmelstjerna, Niklas Pawelzik and Benedikt Korbach
"""


from ArrayDeque import ArrayDequeMaxlen


AQM = ArrayDequeMaxlen(20)


print('Adding last')
for i in range(100):
    AQM.add_last(i)
    print(i, AQM._data)

print('\nDelete 80', AQM.delete_first_match(80), AQM._data, AQM._front)


print('\nAdding first')
for i in range(20, 10, -1):
    AQM.add_first(i)
    print(i, AQM._data)


print(AQM._front)


print('\nPerforming the removals')
while not AQM.is_empty():
    print('Remove first', AQM.first(), AQM.delete_first(),
          'Remove last', AQM.last(),  AQM.delete_last())
