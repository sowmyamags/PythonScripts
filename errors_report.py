#!/usr/bin/env python3

import csv

def generate_errors_report(sorted_errors):
   with open('error_message.csv', 'w') as csvfile:
      csvfile.write('ERROR,COUNT')
   with open('error_message.csv', 'a') as csvfile:
      for error in sorted_errors:
         line = ','.join([error[0],str(error[1])])
         csvfile.write('\n')
         csvfile.write(line)
