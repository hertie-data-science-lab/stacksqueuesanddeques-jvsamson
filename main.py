# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:04:23 2023

@author: Justus v. Samson-Himmelstjerna, Niklas Pawelzik, Benedikt Korbach, Alvaro Guijarro May
"""


from ArrayDeque import ArrayDequeMaxlen


AQM = ArrayDequeMaxlen(20)


print('Adding last')
for i in range(100):
    AQM.add_last(i)
    print(i, AQM._data)


# We have included the following functionality and made it work
# However, technicaly it goes against the intrinsic idea of th Deque functionality.
#print('\nDelete first match with', AQM.delete_first_match(80), AQM._data, AQM._oldest)


print('\nAdding first')
for i in range(20, 10, -1):
    AQM.delete_first()
    AQM.add_first(i)
    print(i, AQM._data)


print(AQM._oldest)


print('\nPerforming the removals')
while not AQM.is_empty():
    print('Remove first', AQM.first(), AQM.delete_first(),
          'Remove last', AQM.last(),  AQM.delete_last())
