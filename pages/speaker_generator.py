#!/usr/bin/env python
import numpy as np

just_presented = ["Paul", "Dima", "Eli", "Brian","Matt"]

names = ["Dot", "Juha", "Pratik", "Pathak", "Shivesh" 
    ,"Alex M.","Jyoti","Ben P.","Benji C.", "Alex L."
    , "WooYoung", "Will","Kiel", "Xiongjie"]

shuffled_pres  = np.random.choice( just_presented,len(just_presented), replace=False )
shuffled_names = np.random.choice( names,len(names), replace=False )
print np.append(shuffled_names, shuffled_pres)
