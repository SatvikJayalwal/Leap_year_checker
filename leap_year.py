import os;os.system("cls")
year = int(input("ENTER THE YEAR : "))
if ( year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print ( year , " IS A LEAP YEAR ")
else :
    print ( year, " IS NOT A LEAP YEAR ")

