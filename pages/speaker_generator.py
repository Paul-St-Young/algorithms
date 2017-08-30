#!/usr/bin/env python
import numpy as np

just_presented = ["Paul"]

names = ["Shivesh","Alex M.","Ben P.","Benji V."
  ,"Ali","Kiel","John Lee","Dima","Eli","Brian","Matt"]

shuffled_pres  = np.random.choice( just_presented,len(just_presented), replace=False )
shuffled_names = np.random.choice( names,len(names), replace=False )
print np.append(shuffled_names, shuffled_pres)
