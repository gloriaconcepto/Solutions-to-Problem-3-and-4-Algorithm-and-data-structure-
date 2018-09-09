#-------------------------------------------------------------------------------
# Name:Perform a benchmark analysis for a shell sort, using different increment sets
#      on the same list

# Purpose:Education
#
# Author:      mmk and emeka
#
# Created:     07/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import random


def create_data():
       '''This is used mainly to generated a database that will be used to performe
       the experiment'''
       #please use this function only once  just to create a database....
       unsorted_list = [random.randint(0,200) for p in range(0, 1000000)]
       with open('unsorteddata.txt', 'w') as file:
          file.write('\n'.join(str(data) for data in unsorted_list))


      # data=open("unsorteddata.txt","w")

       #for num in unsorted_list :
        #    data.write(str(num))

       #data.close()


def load_data():
    ''' This function is load the unsorted data for experiment '''

    print("Loading word list from file...")
    f= open('unsorteddata.txt')
    content=f.read()
    f.close()
    words=content.split()
    return words


def shell_sort1(alist,n):
    sublistcount = len(alist)//n
    #sublistcount = len(alist)//3
    while sublistcount > 0:

      for startposition in range(sublistcount):

        #most important point to analyse.
        gap_insertion_sort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // n


def shell_sort2(alist,n):

    sublistcount = len(alist)//n
    while sublistcount > 0:

      for startposition in range(sublistcount):

        #most important point to analyse.
        gap_insertion_sort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // n

def shell_sort3(alist,n):

    sublistcount = len(alist)//n
    while sublistcount > 0:

      for startposition in range(sublistcount):

        #most important point to analyse.
        gap_insertion_sort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // n


def shell_sort4(alist,n):

    sublistcount = len(alist)//n
    while sublistcount > 0:

      for startposition in range(sublistcount):

        #most important point to analyse.
        gap_insertion_sort(alist,startposition,sublistcount)

     # print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // n

def shell_sort5(alist,n):

    sublistcount = len(alist)//n
    while sublistcount > 0:

      for startposition in range(sublistcount):

        #most important point to analyse.
        gap_insertion_sort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // n




def gap_insertion_sort(alist,start,gap):
    ''' it uses the gap to know which list to performed the insertion sorting'''

    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def main():
   # unsorted_list = [random.randint(0,99) for p in range(0, 100000)]
    #unsorted_list=[200, 30, 28, 9, 150, 60, 53, 68, 10, 11]

     #create_data()
     data =  load_data()
     shell_sort1(data,21)

     #shell_sort2(data,5)

    #shell_sort3(unsorted_list,11)

    #shell_sort4(unsorted_list,15)

    #shell_sort5(unsorted_list,21)

    #print("THE sorted list : ",unsorted_list)





if __name__ == '__main__':
    main()
