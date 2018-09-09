#-------------------------------------------------------------------------------
# Name:  Implementing the len method (__len__) for the hash table Map ADT
# Purpose:  Education
#
# Author:      mmk and emeka
#
# Created:     07/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class HashTable:
   ''' The map abstract data type implements the simple Remainder method
       and the collision resolution technique use is Linear Probing method'''

   def __init__(self,size):
        ''' The hash map size must be a odd number to help avoid collision'''
         #class attributes
        self.size = size
        self.slots = [None] *self.size
        self.data = [None] *self.size

   def put(self, key, data):
       hash_value = self.hash_function(key,len(self.slots))

       if self.slots[hash_value] == None:
          self.slots[hash_value] = key
          self.data[hash_value] = data
       else:
         if self.slots[hash_value] == key:
           self.data[hash_value] = data #replace
         else:
          next_slot = self.rehash(hash_value, len(self.slots))

          while self.slots[next_slot] != None and   self.slots[next_slot] != key:
             next_slot = self.rehash(next_slot, len(self.slots))

          if self.slots[next_slot] == None:
               self.slots[next_slot] = key
               self.data[next_slot] = data
          else:
               self.data[next_slot] = data #replace

   def hash_function(self, key, size):
        return key % size

   def rehash(self, old_hash, size):
       return (old_hash + 1) % size


   def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
            if position == start_slot:
                stop = True
        return data

   def __getitem__(self, key):
        return self.get(key)

   def __setitem__(self, key, data):
        self.put(key, data)



   def len(self) :
         '''' Implementing a method that determined the length of hash map '''
         #get the length and return the value.
         length =len(self.data)

         return length


   def __len__(self):

      '''  Implementing the len method (__len__) for the hash table Map ADT '''
      self.len(self)




def main():
    #pass
    h=HashTable(11)


    h[54]="cat"
    h[26]="dog"
    h[93]="lion"
    h[17]="tiger"
    h[77]="bird"
    h[31]="cow"
    h[44]="goat"
    h[55]="pig"
    h[20]="chicken"

    print(h.len())


if __name__ == '__main__':
    main()
