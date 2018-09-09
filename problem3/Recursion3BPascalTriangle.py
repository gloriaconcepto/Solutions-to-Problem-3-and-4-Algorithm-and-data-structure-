#-------------------------------------------------------------------------------
# Name:     Pascal Triangle recursively
# Purpose:  Education
#
# Author:      mmk and emeka
#
# Created:     04/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import sys

# Recursive method to create the mathematical series
def pascal(col,row):
    if(col == 0) or (col == row):
        return 1
    else:
        return pascal(col-1,row-1) + pascal(col,row-1)

# Method returns the results of n rows in the triangle
def pascal_triangle(num):
    if (num <= 0):
        print('Number must be greater than zero')

    for r in range(num):
        for c in range(r+1):
            sys.stdout.write(str(pascal(c,r))+' ')
            #print('{:15}'.format(str(pascal(c,r))+' '))
        sys.stdout.write('\n')

def main():
    #pass
    pascal_triangle(10)

if __name__ == '__main__':
    main()
