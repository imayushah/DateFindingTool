from find_dates_rules import find_dates_in_text

x = raw_input("Input string: \n")
y = find_dates_in_text(x)
n = -1
output = ''
while (x.find('between') >= 0):
	count = 0
	m = x.find('between')
	while (count < 2):
		for date_index in y:
			if (date_index > m):
				if (count == 0):
					date_index_1 = date_index
				else:
					date_index_2 = date_index
				count = count + 1
			else:
				date_exact = y[date_index]
				output = output + "{'type':'date', 'value':{'exact':'%s', 'min':'', 'max': ''}," % (date_exact)
	date1 = y[date_index_1]
	date2 = y[date_index_2]
	n = date_index_2
	if (date_index_1 > date_index_2):
		date1 = y[date_index_2]
		date2 = y[date_index_1]
		n = date_index_1
	output = output + "{'type':'date', 'value':{'exact':'', 'min':'%s', 'max': '%s'}," % (date1, date2)
	x = x[:m] + x[m+7:]

for date_index in y:
	if (date_index > n):
		date_exact = y[date_index]
		output = output + "{'type':'date', 'value':{'exact':'%s', 'min':'', 'max': ''}," % (date_exact)

output = output[:len(output)-1]
print output