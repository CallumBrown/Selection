#Callum Brown
#03-10-14
#Month exercise

month = int(input("Please enter a month by using 1-12 (January - December): "))

year = int(input("Please enter a year: "))

if month == 1:
    month = "January"
elif month == 2:
    month = "Febuary"
elif month == 3:
    month ="March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month ==8:
    month = "August"
elif month == 9:
    month = "September"
elif month ==10:
    month = "October"
elif month ==11:
    month = "November"
elif month == 12:
    month = "December"
else:
    print("This isn't a month")

if year % 4 == 0:
    print("It's a leap year")
else:
    print("It isn't a leap year")


day = int(input("Please enter a day: "))

if day ==1:
    print("1st {0} {1}".format(month,year))
elif day ==21:
    print("21st {0} {1}".format(month,year))
elif day ==31:
    print("31st {0} {1}".format(month,year))
elif day ==2:
    print("2nd {0} {1}".format(month,year))
elif day ==22:
    print("22nd {0} {1}".format(month,year))
elif day ==3:
    print("3rd {0} {1}".format(month,year))
elif day ==23:
    print("23rd {0} {1}".format(month,year))
else:
    print("{0}th {1} {2}".format(day,month,year))
    

    
