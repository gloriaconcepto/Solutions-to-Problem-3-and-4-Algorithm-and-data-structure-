#-------------------------------------------------------------------------------
# Name: Set up a random experiment to test the difference between a sequential
#         search and a binary search on a list of integers.
#
# Purpose:Educational
#
# Author:      mmk  and emeka
#
# Created:     06/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import cProfile
import random



def ordered_sequential_search(alist, item):
	    pos = 0
	    found = False
	    stop = False
	    while pos < len(alist) and not found and not stop:
	        if alist[pos] == item:
	            found = True
	        else:
	            if alist[pos] > item:
	                stop = True
	            else:
	                pos = pos+1

	    return found


def binary_search_non_recursive(num_list,item):
   '''  A non recursive approach for a binary search '''
   first_item=0
   last_item= len(num_list)-1
   is_item_found=False
    #whats is the looping conditions
   while first_item<=last_item and not is_item_found:
        #divide it to the middle of  index
        middle_item=(first_item + last_item)//2
        #check if the item is in list
        if num_list[middle_item]==item:
            is_item_found=True
        else:
            #check if the item is greater than middle item or is it less than middle item
            if item > num_list[middle_item]:
                #go toward the right side of the list
                first_item=middle_item+1
            #if otherwise
            else:
                last_item=middle_item-1

   return is_item_found

def main():
    #pass

     data = [p for p in range(0, 1000000)]

     # uncomment CASE 1 FOR TESTING
     #print("sequential search case 1 ",ordered_sequential_search(data, 0))
     #print("binary search  case 1",binary_search_non_recursive(data, 0))

     # uncomment CASE 2 FOR TESTING
    # print("sequential search case 2 ",ordered_sequential_search(data, 500000))
     #print("binary search  case 2",binary_search_non_recursive(data, 500000))


      # uncomment CASE 3 FOR TESTING
     print("sequential search case 3 ",ordered_sequential_search(data,999999))
     print("binary search  case 3",binary_search_non_recursive(data, 999999))




if __name__ == '__main__':
    main()
