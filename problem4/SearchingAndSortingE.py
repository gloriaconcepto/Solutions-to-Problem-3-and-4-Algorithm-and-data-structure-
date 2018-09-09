#-------------------------------------------------------------------------------
# Name: Implementing the bubble sort using simultaneous assignment.
# Purpose:   Education
#
# Author:      mmk and emeka
#
# Created:     07/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------


def bubble_sort(a_list):
    '''The bubble sort method using simultaneous assignment for swapping data'''

    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):


            if a_list[i] > a_list[i + 1]:


               #swapping effect using simultaneous assignment
                temp,a_list[i] = a_list[i], a_list[i + 1]

                a_list[i + 1] = temp






def main():

    unsorted_list=[200, 30, 28, 9, 150, 60, 53, 68, 10, 11]

    bubble_sort(unsorted_list)

    print("THE sorted list : ",unsorted_list)


if __name__ == '__main__':
    main()
