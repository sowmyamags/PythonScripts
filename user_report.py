#!/usr/bin/env python3

def generate_user_report(sorted_users):
   with open('user_statistics.csv', 'w') as csvfile:
      file.write('USERNAME,INFO,ERROR')
   with open('user_stattistics.csv', 'a') as csvfile:
      for user in sorted_users:
         line = ','.join([sorted_users[0],str(sorted_users[1][0]),str(sorted_users[1][1])])
         file.write('\n')
         file.write(line)
