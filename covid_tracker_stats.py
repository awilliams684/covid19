import csv
from datetime import datetime
import urllib.request
import codecs

url = 'http://covidtracking.com/api/states/daily.csv'

ftpstream = urllib.request.urlopen(url)
input_data = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

# input_file = 'states-daily.csv'
# input_data = csv.reader(open(input_file), delimiter=',')

data = []
dates = []
states = []

line_count = 0
for row in input_data:
    if line_count == 0:
        line_count += 1
    else:
        if row[0] not in dates:
            dates.append(row[0])
        if row[1] not in states:
            states.append(row[1])
        data.append(row)

sorted_states = sorted(states)
sorted_dates = sorted(dates)

cases_output_file = open('cases_output.csv', 'w')
cases_writer = csv.writer(cases_output_file)

deaths_output_file = open('deaths_output.csv', 'w')
deaths_writer = csv.writer(deaths_output_file)

header_row = []
header_row.append("date")

for state in sorted_states:
    header_row.append(state)

cases_writer.writerow(header_row)
deaths_writer.writerow(header_row)

for date in sorted_dates:
    out_row = []

    date_formatted = datetime.strptime(date , '%Y%m%d')
    out_row.append(date_formatted.strftime("%m/%d/%Y"))    
    for state in sorted_states:
        string = '0'
        for x in data:
            if x[0] == date and x[1] == state:
                string = x[2]
        out_row.append(string)

    cases_writer.writerow(out_row)

for date in sorted_dates:
    out_row = []
    date_formatted = datetime.strptime(date , '%Y%m%d')
    out_row.append(date_formatted.strftime("%m/%d/%Y"))     
    for state in sorted_states:
        string = '0'
        for x in data:
            if x[0] == date and x[1] == state:
                if x[6]!= '':
                    string = x[6]

        out_row.append(string)

    deaths_writer.writerow(out_row)

