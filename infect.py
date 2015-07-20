# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


path = os.path.join(dir_name, str(locations[n]))
    
    try:
        os.makedirs(path)

    except OSError as exception:
         if exception.errno != errno.EEXIST:
             raise
"""

import os
import hashlib


locations = ['C:/Users/Michael/Desktop/test/test1.txt', 
             'C:/Users/Michael/Desktop/test/test2.txt', 
             'C:/Users/Michael/Desktop/test/test3.txt']

      
for i in locations:
    print(hashlib.md5(open(i, 'rb').read()).hexdigest())
    os.remove(i)


print("Great success!")
    
