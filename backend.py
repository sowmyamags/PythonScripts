#!/usr/bin/env python3

import re
text = "abcabcdc"
count = 0
print("c",count)
newtext = ""
for i in text:
  if i in text:
    newtext = newtext+i
    text = text.replace(i,"")
    count += 1
    print(count, newtext)



