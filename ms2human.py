def ms2human(ms):
	x = ms // 1000
	seconds = x % 60
	x //= 60
	minutes = x % 60
	x //= 60
	hours = x % 24
	x //= 24
	days = x
	return (days, hours, minutes, seconds)
	
print("Looping. Use CTRL + C to exit.")
days = input("(y/N) result with days?: ")
while True:
	ms = int(input("ms: "))
	
	result = ms2human(ms)
	if days == "y":
		print("(dd:HH:MM:SS): {:02}:{:02}:{:02}:{:02}".format(result[0], result[1], result[2], result[3]))
	else:
		print("(HH:MM:SS): {:02}:{:02}:{:02}".format(result[1], result[2], result[3]))
	
	input()