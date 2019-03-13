#check if AM or PM
#if AM return string without last two char
#if PM return new string with first two char + 12 without last two char
#
def timeConversion(s):
	hour = int(s[0:2])
	minute = int(s[3:5])
	second = int(s[6:8])

	if hour == 12 and "AM" in s:
		hour = "00"
		return(hour + s[2:-2])
	if hour == 12 and "PM" in s:
		return(str(hour)+s[2:-2])

	if "PM" in s:
		hour += 12
		return (str(hour)+s[2:-2])
	else:
		return(s[0:-2])

print(timeConversion("06:40:03AM"))







