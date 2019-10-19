"""
this script, just like example.py, was designed to be run in ipython
after running it you end up with a bunch of bins
in the ith bin (bin[i]) is a list of names,
none of which share the first or last letters

this procedure is equivalent to the 'naive' greedy method of coloring
and the order in which the names are sorted into bins is random
so during the demo i would
    %run nongraphical.py
multiple times, yielding slightly different results some of the time
"""
from random import shuffle

#get names
with open("elements.txt", "r") as f:
    lines = f.readlines()
names = []
for line in lines:
    names.append(line.split()[0])

#put names in random order and start with first name
shuffle(names)
bins = [[names[0]]]

def checkBin(name, bn):
    #determine if name can be placed in bn
    compatible = True
    for n in bn:
        if (name[0] == n[0]) or (name[-1] == n[-1]):
            compatible = False
            break
    return compatible

def placeBin(name):
    placed = False
    bin_num = 0
    while not placed:
        if checkBin(name, bins[bin_num]):
            bins[bin_num].append(name)
            placed = True
        bin_num += 1 #try next bin
        if bin_num == len(bins):
            #unless there are no more bins...
            bins.append([name])
            placed = True

for i in range(1, len(names)):
    placeBin(names[i])
