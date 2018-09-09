#-------------------------------------------------------------------------------
# Name: Implementing the selection sort using simultaneous assignment.
# Purpose: Education
#
# Author:      mmk and emeka
#
# Created:     07/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
def selection_sort(alist):
   '''The selection sort method using simultaneous assignment for swapping data'''

   for fillslot in range(len(alist)-1,0,-1):

       positionOfMax=0

       for location in range(1,fillslot+1):

           if alist[location]>alist[positionOfMax]:
               positionOfMax = location


       temp,alist[fillslot]=alist[fillslot],alist[positionOfMax]
       alist[positionOfMax] = temp





def main():
   unsorted_list=[200, 30, 28, 9, 150, 60, 53, 68, 10, 11]

   selection_sort(unsorted_list)

   print("THE sorted list : ",unsorted_list)


if __name__ == '__main__':
    main()
