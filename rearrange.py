Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*) ([A-Za-z]\.*)$", name)
    if result == None:
        return "name only"+ name
    return "{} {} {}".format(result[2],result[3], result[1])
