def payg():
	strings = ["105/821.15",
			   "232/1136.97",
			   "150/940.66",
			   "163/974.80",
			   "54/580.44",
			   "171/998.10",
			   "315/1307.20",
			   "198/1071",
			   "127/901.90"]

	for s in strings:
		ls = s.split('/')
		print(s)
		print(float(ls[0]) / float(ls[1]))
		print()

def work(weekday=0, saturday=0, sunday=0, public_holiday=0, rates=None):

	if rates == None:
		print("Error: Provide rates arguments")
		return

	result = 0

	# Allowance
	allowance = (rates['allowance'] * min(38, (weekday + saturday + sunday + public_holiday)))

	# Leave
	leave = (rates['leave'] * (weekday + saturday + sunday))
	leave_pub_hol = (rates['leave_pub_hol'] * (public_holiday))

	# Base
	base = (rates['base'] * (weekday + saturday + sunday))

	# Total hours
	total_hours = weekday + saturday + sunday + public_holiday

	# Weekday
	weekday = rates['weekday'] * weekday

	# Saturday
	saturday = rates['saturday'] * saturday

	# Sunday
	sunday = rates['sunday'] * sunday

	# Public holiday
	public_holiday = rates['public_holiday'] * public_holiday

	result = round(allowance, 2) + round(leave, 2) + round(leave_pub_hol, 2) + round(base, 2) + round(weekday, 2) + round(saturday, 2) + round(sunday, 2) + round(public_holiday, 2)
	result = round(result, 2)

	print("total_hours: " + str(total_hours))
	print("allowance: " + str(allowance))
	print("leave: " + str(leave))
	print("leave_pub_hol: " + str(leave_pub_hol))
	print("weekday: " + str(weekday))
	print("saturday: " + str(saturday))
	print("sunday: " + str(sunday))
	print("public_holiday: " + str(public_holiday))
	
	print("total: " + str(result))
	return result

rates = {
		'base' : 26.33,
		'leave' : 2.74,
		'leave_pub_hol': 2.07,
		'allowance' : 0.42,
		'weekday' : 6.58,
		'saturday' : 13.16,
		'sunday' : 19.75,
		'public_holiday' : 62.2593,
	}

# work(weekday=26, saturday=7.5, sunday=0.5, rates=rates)
# work(weekday=9, saturday=9.5, sunday=4, public_holiday=8.5, rates=rates)
# work(weekday=8+9, saturday=7.5, sunday=7.5, public_holiday=9, rates=rates)
# work(weekday=26.5, saturday=8.5, sunday=0, public_holiday=0, rates=rates)
# work(weekday=4+5+7.5, saturday=8.5, sunday=6, public_holiday=0, rates=rates)

work(weekday=7+9.5+7.5, saturday=8.5, sunday=0, public_holiday=0, rates=rates)
