import calendar
print("enter the year and Month to generate the calendar.....")
year = int(input("Year : "))
month =int(input("Number of Month like 1 : jan || 2 : feb || 3 : mar || 4 : apr || 5 : may || 6 : jun || 7 : jul || 8 : aug || 9 : sept || 10 : oct || 11 : nov || 12 : dec : "))
x=calendar.month(year,month)
print(x)