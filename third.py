from collections import OrderedDict
duplicate= [12,24,55,55,67,35,24,989,987,88,120,155,88,120,155]
nodups=list(set(duplicate))

nodups.sort(key=duplicate.index)
print(nodups)
        


