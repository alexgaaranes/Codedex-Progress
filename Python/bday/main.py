import datetime, bday_msg

today = datetime.date.today()
next_bday = datetime.date(2024,3,3)

days_away = today - next_bday

if today == next_bday:
	print(bday_msg.random_message)
else:
	print(f"My next birthday is {days_away} away!")

