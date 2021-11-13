from fulltimeemployee import FullTimeEmployee
from hourlytimeemployee import HourlyTimeEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add_name(FullTimeEmployee('Naveen', 'Kollu', 30000))
payroll.add_name(FullTimeEmployee('Joe', 'Quinn', 50000))
payroll.add_name(HourlyTimeEmployee('Nick', 'Fury', 150, 250))

payroll.print()