#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool
import re

src = "/home/student-00-eecb51d91601/data/prod/"
dest = "/home/student-00-eecb51d91601/data/prod_backup/"
def run(directory):
    src = directory
    print(src)
    print("Moving Datat from {} to dest".format(src))
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    dir_list = []
    for root, dirs, files in os.walk(src, topdown = False):
       for name in dirs:
           dir_list.append(os.path.join(root, name))
    p = Pool(len(dir_list))
    p.map(run, dir_list)


