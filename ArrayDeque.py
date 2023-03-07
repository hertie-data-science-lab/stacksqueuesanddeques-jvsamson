# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:04:23 2023

@author: Justus v. Samson-Himmelstjerna
"""


class Empty(Exception):
    pass


class ArrayDequeMaxlen():
    def __init__(self, size):
        """Create an empty Array-based deque with a maximum capacity"""
        self._data = [None] * size  # create an list of None with given size
        self._size = 0  # number of elements in the deque initially set to 0
        self._front = 0  # the position of the first element initially set to 0
        self._ = 0

    def add_first(self, e):
        """Add element 'e' to the front of deque D."""
        # if the number of elements reaches the maximum capacity of the array
        # the array has to be resized
        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        # position of new element calculated
        # by moving the front pointer one step backwards
        avail = (self._front - 1) % len(self._data)
        # assign new value to this position
        self._data[avail] = e
        # adjust the _front pointer to point at the new first element
        self._front = avail
        # increase the deque size by 1
        self._size += 1

    def add_last(self, e):
        """Add element 'e' to the back of deque D."""
        # if number of elements reaches maximum capacity then resize the array
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        # calculate position of new element by looking at current pointer, size
        avail = (self._front + self._size) % len(self._data)
        # assign the new value
        self._data[avail] = e
        # increase the size of deque by 1
        self._size += 1

    def delete_first(self, e):
        """Remove and return the first element from deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # save the value of the element currently in the first position
        result = self._data[self._front]
        # reset the value of first element in order to fill with a new value
        self._data[self._front] = None
        # move the pointer forward
        self._front = (self._front + 1) % len(self._data)
        # reduce the size of deque by 1
        self._size -= 1
        # return the removed first element
        return result

    def first(self):
        """Return the first element of deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # return the value from the first eleemnt's position
        return self._data[self._front]

    def last(self):
        """Return the last element of deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # get position of last element by looking at size, current pointer
        back = (self._front + self._size - 1) % len(self._data)
        # return the value in this position
        return self._data[back]

    def is_empty(self):
        """Return True if deque D does not contain any elements."""
        # Simple condition check
        return self._size == 0

    def __len__(self):
        """Return the number of elements in deque D"""
        # Just return the size of deque
        return self._size

    def _resize(self, cap):
        """Resize the list of Deque D to a capacity of 'cap',
        which must be greater than/equal to the current length of the deque."""
        # save old values in order to retain them after the reisding
        old = self._data
        # create a new list with given capacity and fill it with nones
        self._data = [None] * cap
        # start at the current front-position
        walk = self._front
        # loop through all elements starting at the front of the deque
        for k in range(self._size):
            # copy the element in the new list
            self._data[k] = old[walk]
            # move the old pointer
            walk = (1 + walk) % len(old)
        self._
