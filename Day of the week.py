#Finding Day of the week
from datetime import date

#accepts date month and year from input
d, m, y = [int(x) for x in input("Enter a date:").split('/')]

#store them in class dt
dt= date(y, m, d)

#%w =Day number %A = Day
print(dt.strftime('Day %w of the week. This is %A'))