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
import cProfile
import SearchingAndSortingG





def main():
   # pass
    cProfile.run('SearchingAndSortingG.main()')

if __name__ == '__main__':
    main()
