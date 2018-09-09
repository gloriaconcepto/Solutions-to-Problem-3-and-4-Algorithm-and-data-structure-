#-------------------------------------------------------------------------------
# Name:        Fibonacci recursive and iterative  method
# Purpose:       Education
#
# Author:      mmk and emeka
#
# Created:     04/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
#===============================================================================
#FIBONACCI RECURSIVE FUNCTION
#===============================================================================
def fibonacci_recursive(num):
    '''Takes and integer and return it fibonacci sequence.it return
        fibonacci sum(integer)'''

        #a boolean to print the fibonacci sequence.

    isprint_fibo_sequence=False

         # declare a base case
    if num==0 or num==1:

        return 1

    else:

        #make the recursive call
      return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


#===============================================================================
# AN ITERATIVE  METHOD TO ANALYSE FIBONACCI SEQUENCE
#===============================================================================
def iterative_fibonacci(num):
    ''' This functions takes in an intege and return interge '''
    #iterative method
    index_1=1
    index_2=1

    for i in range(num-1):
        index_1=index_2
        index_2= index_1 + index_2

    return index_1





#===============================================================================
# A FUNCTION TO PRINT THE FIBONACCI SEQUENCE
#===============================================================================
def print_fibon_sequence(num):
    '''This print_fibon_sequence(2) and it's return a string'''
    index_1=0

    index_2=1

    count=0
        #Check  if the count is zero and one
    if  num==1:
        print("Fibonacci sequence upto",num,":")
        print(index_1)

    else:
         print("Fibonacci sequence upto",num,":")

         while count<num+1:


             print(index_1,end=' , ')

             nth= index_1 + index_2

             index_1 =index_2

             index_2 = nth

             count +=1












def main():
    #pass
    print(fibonacci_recursive(5))

    #to print the fibonacci sequences

    print_fibon_sequence(5)

    print(iterative_fibonacci(5))
if __name__ == '__main__':
    main()
