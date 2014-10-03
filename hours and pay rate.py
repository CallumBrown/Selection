#Callum Brown
#30-09-14
#Hours worked and pay rate

hours = int(input("Please enter the amount of hours you have worked the week: "))
pay_rate = int(input("Please enter your hourly rate of pay: "))
no_overtime = hours*pay_rate
if hours < 61:
    if hours > 40:
        over_time = hours - 40
        over_pay = over_time*1.5
        pay = (hours - over_time)*pay_rate
        overall_pay = over_pay+pay
        print("Your overall pay is £{0}!".format(overall_pay))
    else:
        print("Your overall pay is £{0}!".format(no_overtime))
        

