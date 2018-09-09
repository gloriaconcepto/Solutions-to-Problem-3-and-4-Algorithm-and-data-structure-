#-------------------------------------------------------------------------------
# Name:        Reverse list recursively
# Purpose:
#
# Authors:      mmk and emeka
#
# Created:     04/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
#===============================================================================
# A FUNCTION THE REVERSE THE ORDER OF A LIST RECURSIVELY
#===============================================================================
def rev_list(enter_list):
     ''' rev_list(list datatype) and it return a reverse string which can then
         be split to list'''

    #is the list lenght 1 the base case

     if len(enter_list) == 1:

          return enter_list[0]

     else:

          #recursive call
          return (rev_list(enter_list[1:]) +" "+ enter_list[0] )

#===============================================================================
#THE MAIN FUNCTION THE RETURN A REVERSE LIST
#================================================================================

def return_reverse_list(enter_list1) :
    '''The purpose of this function is return a list in a reverse order by
       calling "rev_list()" '''
    #pass the parameter to rev_list and convert it to a list

    new_list=rev_list(enter_list1).split()

    #return a list in reverse order

    return new_list



def main():
    #pass

    sea=['shark', 'octopus','blobfish','mantis shrimp', 'anemone']


    print(return_reverse_list(sea))

if __name__ == '__main__':
    main()
