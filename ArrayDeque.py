# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 13:04:23 2023

@author: Justus v. Samson-Himmelstjerna, Niklas Pawelzik, Benedikt Korbach, Alvaro Guijarro May
"""


class Empty(Exception):
    pass


class ArrayDequeMaxlen():

    start_size = 10

    def __init__(self, max_len):
        """Create an empty Array-based deque with a maximum capacity"""
        self._data = [None] * ArrayDequeMaxlen.start_size  # create an list of None with given size
        self._size = 0  # number of elements in the deque initially set to 0
        self._oldest = 0  # the position of the first element initially set to 0
        self._ = 0
        self.max_len = max_len

    def add_first(self, e):
        """Add element 'e' to the front of deque D."""
        # if the number of elements reaches the maximum capacity of the array
        # the array has to be resized using Fi-Fo Method
        if self._size == self.max_len:
            self.delete_last()
            for i in range(len(self._data)):
                self._data[(self._oldest + i -1  ) % len(self._data)] = self._data[(self._oldest + i) % len(self._data)]
            self._oldest += 1
        # If deque not at maximum length but at maximum capacity than resize
        elif self._size == len(self._data):
            self._resize(2 * len(self._data))
        # position of new element calculated
        # by moving the front pointer one step backwards
        avail = (self._oldest - 1) % len(self._data)
        # assign new value to this position
        self._data[avail] = e
        # adjust the _oldest pointer to point at the new first element
        self._oldest = avail
        # increase the deque size by 1
        self._size += 1

    def add_last(self, e):
        """Add element 'e' to the back of deque D."""
        # if number of elements reaches maximum capacity then resize the array
        if self._size == self.max_len:
            # using Fi-Fo Method
            self.delete_first()
            for i in range(len(self._data)):
                self._data[(self._oldest + i-1) % len(self._data)] = \
                    self._data[(self._oldest + i) % len(self._data)]
            self._oldest = self._oldest -1
        # If deque not at maximum length but at maximum capacity than resize
        elif self._size == len(self._data):
            self._resize(2 * len(self._data))
        # calculate position of new element by looking at current pointer, size
        avail = (self._oldest + self._size) % len(self._data)
        # assign the new value
        self._data[avail] = e
        # increase the size of deque by 1
        self._size += 1

    def delete_first(self):
        """Remove and return the first element from deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # save the value of the element currently in the first position
        result = self._data[self._oldest]
        # reset the value of first element in order to fill with a new value
        self._data[self._oldest] = None
        # move the pointer forward
        self._oldest = (self._oldest + 1) % len(self._data)
        # reduce the size of deque by 1
        self._size -= 1
        # return the removed first element
        return result

    def delete_last(self):
        """Remove and return the last element from deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # get position of last element by looking at size, current pointer
        back = (self._oldest + self._size - 1) % len(self._data)
        # save the value of the last element
        result = self._data[back]
        # set the last element to None
        self._data[back] = None
        # decrement the size of deque by 1
        self._size -= 1
        # return the removed last element
        return result

    def delete_first_match(self, e):
        """Remove and return the last element from deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # Find the index of the first element that matches 'e'
        match_index = -1
        for i in range(self._size):
            if self._data[(self._oldest + i) % len(self._data)] == e:
                match_index = i
                break
        # If no matching element was found, raise an exception
        if match_index == -1:
            raise ValueError(f"No match found for element '{e}' in deque")
        # Save the value of the matching element and remove it from the deque
        match_value = self._data[(self._oldest + match_index) % len(self._data)]
        for i in range(match_index, self._size - 1):
            # Shift all the elements after the matching element to the left
            self._data[(self._oldest + i) % len(self._data)] = \
                self._data[(self._oldest + i + 1) % len(self._data)]
        # Set the last element to None and decrement the size of deque
        self._data[(self._oldest + self._size - 1) % len(self._data)] = None
        self._size -= 1
        # Return the value of the removed element
        return match_value

    def first(self):
        """Return (but do not remove) the first element of deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # return the value from the first eleemnt's position
        return self._data[self._oldest]

    def last(self):
        """Return (but do not remove) the last element of deque D"""
        if self.is_empty():
            raise Empty('Deque is empty')
        # get position of last element by looking at size, current pointer
        back = (self._oldest + self._size - 1) % len(self._data)
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

    def _resize(self, max_len):
        """Resize the list of Deque D to a capacity of 'cap'"""
        # save old values in order to retain them after the reisding
        old = self._data
        # create a new list with given capacity and fill it with nones
        self._data = [None] * max_len
        # start at the current front-position
        walk = self._oldest
        # loop through all elements starting at the front of the deque
        for k in range(self._size):
            # copy the element in the new list
            self._data[k] = old[walk]
            # move the old pointer
            walk = (1 + walk) % len(old)
        self._
