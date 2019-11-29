#!/usr/bin/env python3
import sys

l = 0
for line in sys.stdin:
	#Print the first line as a heading
	if l == 0:
		sys.stdout.write(line)
		l = 1
		continue
	#split fields by comma for CSV
	fields = line.split(',')
	#Use the first 6 fields as parameters
	params = fields[:6]
	#Map the rest of the fields to ints
	times = list(map(float, fields[6:]))
	for time in times:
		print(','.join(params + [str(time)]))
	#Sort to get the median
	#times.sort()
	#med = times[int(len(times)/2)]
	#Replace the times with the median time
	#params += [str(med)]
	#print(','.join(params))