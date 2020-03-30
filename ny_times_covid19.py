import csv
from datetime import datetime
import urllib.request
import codecs
import ssl

url = 'http://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
context = ssl._create_unverified_context()

web_data = urllib.request.urlopen(url, context=context)
input_data = csv.reader(codecs.iterdecode(web_data, 'utf-8'))

data = []
dates = []
states = []

line_count = 0
for row in input_data:
    if line_count == 0:
        line_count += 1
    else:
        line_count += 1
        if row[0] not in dates:
            dates.append(row[0])
        if row[1] not in states:
            states.append(row[1])
        data.append(row)

sorted_states = sorted(states)

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

for date in dates:
    out_row = []
    out_row.append(date)    
    for state in sorted_states:
        string = '0'
        for x in data:
            if x[0] == date and x[1] == state:
                string = x[3]
        out_row.append(string)
        
    cases_writer.writerow(out_row)

for date in dates:
    out_row = []
    out_row.append(date)    
    for state in sorted_states:
        string = '0'
        for x in data:
            if x[0] == date and x[1] == state:
                string = x[4]
        out_row.append(string)

    deaths_writer.writerow(out_row)

