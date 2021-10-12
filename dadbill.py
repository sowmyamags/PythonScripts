#!/usr/bin/env python3

import re
import operator

path = r"/mnt/c/users/sowmya/downloads/febbill.txt"
dict = {}
total = 0

def amount(amount, dict):
  for k,v in dict.items():
    if '-2021' in v:
      print("v; ",v)
      if amount in dict["Amount"][0]:
        #sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[0], reverse = True)}
        #print("sorted,k,v",sorted_dict)
        #print("In the month of october on {} had Service of {} {} for amount of {}".format(dict["date"],dict["Service"],dict["Amount"][0]))
        print("Amount:", dict["Amount"][0])
        price += int(dict["Amount"][0])
        
        return price
     
def gloves(name, dict):
  for k,v in dict.items():
    if '-10-2020' in v:
      if name in dict["Service"]:
        print("gf  on {} for {}".format(dict["date"],dict["Amount"][0]))
      
      return name  

with open(path) as file:
  content = file.readlines()
  for line in content:
    pattern1 = r"(\d{2})-(\d{2})-(\d{4})"
    pattern2 = r"([0-9,]+\.\d{2}) (\d+\.\d{2}) (\d+\.\d{2}) ([0-9,]+\.\d{2})"
    pattern3 = r"[A-Za-z\\-]+"
    try:
      date = re.search(pattern1, line)
      service = re.findall(pattern3, line)
      details = re.search(pattern2, line)
      dict["date"] = date.group(0)
      dict["Service"] = " ".join(service)
      dict["Rate"] = details.group(1)
      dict["Qty"] = details.group(2)
      dict["Tax"] = details.group(3)
      dict["Amount"] = re.sub(r'[,]', r'', details.group(4)).split('.')
    except AttributeError:
      date = None
      service = None
    #print(dict)
    for k,v in dict.items():
      if '-2021' in v:
        value = int(dict["Amount"][0])
        total+=value
        print(dict["date"], dict["Amount"][0])
        print(total)


