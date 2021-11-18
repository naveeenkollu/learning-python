from fulltimeemployee import FullTimeEmployee
from hourlytimeemployee import HourlyTimeEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add(FullTimeEmployee('Naveen', 'Kollu', 30000))
payroll.add(FullTimeEmployee('Joe', 'Quinn', 50000))
payroll.add(HourlyTimeEmployee('Nick', 'Fury', 150, 250))

payroll.print()
