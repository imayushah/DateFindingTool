def find_dates_in_text(string_input):

	dates_found = {}

	dates = [' 1st', ' 2nd', ' 3rd', ' 4th', ' 5th', ' 6th', ' 7th', ' 8th', ' 9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
	months = ['jan', 'Jan', 'feb', 'Feb', 'mar', 'Mar', 'apr', 'Apr', 'may', 'May', 'jun', 'Jun', 'jul', 'Jul', 'aug', 'Aug', 'sep', 'Sep', 'oct', 'Oct', 'nov', 'Nov', 'dec', 'Dec']
	date_Current = 0
	month_Current = 0
	year_Current = 2016

	for i in range(0, len(dates)):
		while (string_input.find(dates[i]) >= 0):
			for j in range(0, len(months)):
				if (string_input.find(months[j]) >= 0):
					y = string_input.find(months[j])
					string_input = string_input[:y] + 'XXX' + string_input[y+3:]
					month_Current = j/2 + 1
					break
			x = string_input.find(dates[i])
			string_input = string_input[:x] + 'ZZZZ' + string_input[x+4:]
			date_Current = i+1
			string_Current = "%02d-%02d-%d" % (date_Current, month_Current, year_Current)
			dates_found[x] = string_Current
	for j in range(0, len(months)):
		if (string_input.find(months[j]) >= 0):
			y = string_input.find(months[j])
			string_input = string_input[:y] + 'XXX' + string_input[y+3:]
			month_Current = j/2 + 1
			string_Current = "%d-%02d" % (year_Current, month_Current)
			dates_found[y] = string_Current

	return dates_found