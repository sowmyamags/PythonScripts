#!/usr/bin/env python3

import csv

def generate_users_report(sorted_users):
   with open('user_statistics.csv', 'w') as csvfile:
      csvfile.write('USERNAME,INFO,ERROR')
   with open('user_statistics.csv', 'a') as csvfile:
      for user in sorted_users:
         line = ','.join([user[0],str(user[1][0]),str(user[1][1])])
         csvfile.write('\n')
         csvfile.write(line)
