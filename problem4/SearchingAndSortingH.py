#-------------------------------------------------------------------------------
# Name:       Implement the median-of-three method for selecting a pivot value as a
#              modification to quickSort
# Purpose:Education
#
# Author:      mmk and emeka
#
# Created:     10/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------

def quick_sort(alist):
    # performed the median for the pivot here

    quick_sort_helper(alist,0,len(alist)-1)

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1,last)


def partition(alist,first,last):
    #using median methods to calculate the pivot point.
   first_value=alist[0]
   middle_value=alist[len(alist)//2]
   last_value=alist[len(alist)-1]


   median_list=[first_value,middle_value,last_value]

    #sort to get the list
   median_list.sort()

   pivotvalue = median_list[1]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark




def main():

    alist = [54,26,93,17,77,31,44,55,20]
    quick_sort(alist)
    print(alist)


if __name__ == '__main__':
    main()
