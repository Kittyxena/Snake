minutes = int(input("Minutes: "))

days = minutes // (24 * 60)

hours = minutes // 60



minutesleftover = minutes - (hours * 60)
hoursleftover = hours - (days * 24)
#hours - number of hours  per day(how many hours 
#are being taken off?)need to remove 
#  the number of hours (24) * number of days




print( str(days) + " days, " + str(hoursleftover) + " hours, " + str(minutesleftover) + " minutes")





