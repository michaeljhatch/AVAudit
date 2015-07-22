# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:00:07 2015

@author: Michael
"""

import os
import errno

save_path='test'



try:
    os.makedirs(save_path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
        
        
path1 = "test1"

path2 = "test2"

path3 = "test3"

testpath1 = os.path.join(save_path, path1+".txt")

testpath2 = os.path.join(save_path, path2+".txt")

testpath3 = os.path.join(save_path, path3+".txt")

file1 = open(testpath1, "w")

file1.write("This shouldn't exist!")

file1.close()


file2 = open(testpath2, "w")

file2.write("Neither should this!")

file2.close()



file3 = open(testpath3, "w")

file3.write("Noth this one either!")

file3.close()
